import os , re , json , base64 , random , time , threading
from asyncio import sleep
from datetime import datetime, timedelta
from rubpy import Client, filters
from rubpy.types import Updates

game_file = "game.json"
data_file = "data.json"

bot = Client("rubpy",timeout=10000)

def is_owner(author_guid):
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        admin_guid = str(data.get("u0F8dTt0cee5aa71f5a29888ff90d"))
        return str(author_guid) == admin_guid if admin_guid else False

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"[❌] خطا در بارگذاری admin_guid از data.json: {e}")
        return False
        
# ---------------- تبدیل عدد فارسی به انگلیسی ----------------
persian_digits = "۰۱۲۳۴۵۶۷۸۹"
english_digits = "0123456789"
def fa_to_en(text):
    return text.translate(str.maketrans(persian_digits, english_digits))

# ---------------- بارگذاری اطلاعات ----------------
def load_game_data():
    if not os.path.exists(game_file) or os.path.getsize(game_file) == 0:
        with open(game_file, "w", encoding="utf-8") as f:
            json.dump({
                "admins": [],
                "users": {},
                "banned_users": [],
                "game_active": True
            }, f, indent=2, ensure_ascii=False)

    with open(game_file, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {
                "admins": [],
                "users": {},
                "banned_users": [],
                "game_active": True
            }

def save_game():
    with open(game_file, "w", encoding="utf-8") as f:
        json.dump(game_data, f, indent=2, ensure_ascii=False)

# ---------------- مقداردهی اولیه حافظه ----------------
game_data = load_game_data()

# ---------------- بارگذاری owner از data.json و اضافه کردن به admin ----------------
if os.path.exists(data_file):
    with open(data_file, "r", encoding="utf-8") as f:
        try:
            main_data = json.load(f)
            owner_guid = main_data.get("admin_guid")
            if owner_guid and owner_guid not in game_data["admins"]:
                game_data["admins"].append(owner_guid)
                save_game()
        except:
            pass

# ---------------- داده پیش‌فرض کاربر ----------------
def get_user_data(user_guid):
    users = game_data.setdefault("users", {})
    user = users.get(user_guid)
    if not user:
        user = {
            "wallet": 10000,
            "last_spin": None,
            "miner_level": 1,
            "miner_speed": 1000,
            "miner_storage": 0
        }
        users[user_guid] = user
        save_game()
    # اگر ادمین هست، سکه بینهایت کن
    if str(user_guid) in game_data.get("admins", []):
        user["wallet"] = float("inf")
    return user

# ---------------- بررسی ادمین بودن ----------------
def is_admin(user_guid):
    return str(user_guid) in game_data.get("admins", [])
    
def is_game_admin(user_guid):
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return str(user_guid) == str(data.get("admin_game"))
    except:
        return False
# ---------------- بررسی بن بودن ----------------
def is_banned(user_guid):
    return str(user_guid) in game_data.get("banned_users", [])

# ---------------- تبدیل عدد متنی با واحد ----------------

def parse_amount_with_units(text: str):
    units = {
        "هزار": 1_000,
        "هزارتا": 1_000,
        "هزار‌تا": 1_000,
        "میل": 1_000_000,
        "میلیون": 1_000_000,
        "میلیارد": 1_000_000_000,
        "بیل": 1_000_000_000,
        "تیل": 1_000_000_000_000,
        "تریلیارد": 1_000_000_000_000
    }

    text = text.strip().lower().replace("،", "").replace(",", "").replace(" ", "")

    # تبدیل ارقام فارسی به انگلیسی
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    for p, e in zip(persian_digits, english_digits):
        text = text.replace(p, e)

    for unit in units:
        if text.endswith(unit):
            number_part = text[:-len(unit)]
            try:
                number = float(number_part)
                return int(number * units[unit])
            except ValueError:
                return None
    try:
        return int(text)
    except ValueError:
        return None

# تابع شرط‌بندی از متن
def parse_bet_amount(text: str):
    amount = parse_amount_with_units(text)
    if amount is None or amount <= 0:
        return None
    return amount

# ---------------- حلقه ماینر ----------------
async def update_miner_storage_loop():
    while True:
        await asyncio.sleep(1)
        users = game_data.get("users", {})
        for user_guid, user in users.items():
            speed = user.get("miner_speed", 0)
            if not isinstance(user["wallet"], float):
                user["miner_storage"] = user.get("miner_storage", 0) + speed
        save_game()
        
        
############################


@bot.on_message_updates(filters.regex("^موجودی$"), filters.is_group)
async def show_wallet(update: Updates):
    user = get_user_data(update.author_guid)

    if not game_data.get("game_active", True):
        await update.reply("❌ بازی‌ها در حال حاضر خاموش هستند.")
        return

    if user["wallet"] == float("inf"):
        wallet_text = "بی‌نهایت ♾️"
    else:
        wallet_text = f"{user['wallet']:,} سکه"

    await update.reply(f"💰 موجودی شما: {wallet_text}")

#گردونه
@bot.on_message_updates(filters.regex("^گردونه$"), filters.is_group)
async def daily_spin(update: Updates):
    user_guid = update.author_guid
    user = get_user_data(user_guid)
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    if user.get("last_spin") == today:
        tomorrow = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
        remaining = tomorrow - now
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        await update.reply(
            f"⛔️ شما امروز گردونه رو زدید.\n"
            f"⏳ زمان باقی‌مانده تا گردونه بعدی: {hours} ساعت و {minutes} دقیقه"
        )
        return

    prize = random.randint(2000, 1_000_000_000)
    user["wallet"] += prize
    user["last_spin"] = today
    save_game()

    await update.reply(
        f"🎉 شما {prize:,} سکه از گردونه برنده شدید!\n"
        f"💰 موجودی جدید: {user['wallet']:,} سکه"
    )
    
#جمع ماینر
@bot.on_message_updates(filters.regex("^جمع ماینر$"), filters.is_group)
async def collect_miner(update: Updates):
    user = get_user_data(update.author_guid)
    owner = is_owner(update.author_guid)

    earned = user["miner_storage"]
    user["wallet"] += earned
    user["miner_storage"] = 0

    save_game()

    if owner:
        wallet_text = "بی‌نهایت"
    else:
        wallet_text = f"{user['wallet']:,}"

    await update.reply(
        f"⛏ {earned:,} سکه از ماینر به کیف پول منتقل شد!\n"
        f"💰 موجودی: {wallet_text} سکه"
    )
    
#ماینر
@bot.on_message_updates(filters.regex("^ماینر$"), filters.is_group)
async def miner_info(update: Updates):
    user = get_user_data(update.author_guid)
    owner = is_owner(update.author_guid)

    if owner:
        user["miner_level"] = 999999999
        user["miner_speed"] = 999999999
        save_game()

    price = user["miner_level"] * 50000
    await update.reply(
        f"🔧 سطح ماینر: {'بی‌نهایت' if owner else user['miner_level']}\n"
        f"⚡️ سرعت تولید: {user['miner_speed']} سکه/ثانیه\n"
        f"📦 موجودی ماینر: {user['miner_storage']:,} سکه\n"
        f"💸 قیمت ارتقای سطح بعد: {'بی‌نهایت' if owner else f'{price:,}'} سکه"
    )
    
#خرید ماینر
@bot.on_message_updates(filters.regex("^خرید ماینر$"), filters.is_group)
async def buy_miner(update: Updates):
    user = get_user_data(update.author_guid)
    owner = is_owner(update.author_guid)
    price = user["miner_level"] * 50000

    if not owner and user["wallet"] < price:
        await update.reply(f"❌ شما به {price:,} سکه برای ارتقای ماینر نیاز دارید.")
        return

    if not owner:
        user["wallet"] -= price

    user["miner_level"] += 1
    user["miner_speed"] += 1000 if user["miner_speed"] < 10000 else 10000

    if owner:
        user["miner_level"] = 999999999
        user["miner_speed"] = 999999999

    save_game()

    user_wallet=str(user["wallet"])
    await update.reply(
        f"⛏ {earned:,} سکه از ماینر به کیف پول منتقل شد!\n"
        f"💰 موجودی {'بی‌نهایت' if owner else f'{user_wallet:,}'} سکه"
    )


#خرید حداکثر ماینر

@bot.on_message_updates(filters.regex("^خرید حداکثر ماینر$"), filters.is_group)
async def buy_max_miner(update: Updates):
    user = get_user_data(update.author_guid)
    owner = is_owner(update.author_guid)
    wallet = user["wallet"]
    level = user["miner_level"]
    upgrades = 0

    if owner:
        user["miner_level"] = 999999999
        user["miner_speed"] = 999999999
        save_game()
        await update.reply("✅ سطح ماینر شما روی بی‌نهایت تنظیم شد! 🚀")
        return

    # برای کاربران عادی:
    while True:
        price = level * 50000
        if wallet >= price:
            wallet -= price
            level += 1
            upgrades += 1
        else:
            break

    if upgrades == 0:
        await update.reply("❌ موجودی شما برای خرید حتی یک سطح ماینر کافی نیست.")
        return

    user["wallet"] = wallet
    user["miner_level"] = level
    user["miner_speed"] = 100 * level
    save_game()

    await update.reply(
        f"✅ {upgrades} سطح ماینر با موفقیت خریداری شد!\n"
        f"🔧 سطح جدید: {level}\n"
        f"⚡️ سرعت: {user['miner_speed']} سکه/ثانیه\n"
        f"💰 موجودی باقی‌مانده: {wallet:,} سکه"
    )

#پروفیت
@bot.on_message_updates(filters.regex("^پروفیت$"), filters.is_group)
async def miner_stats(update: Updates):
    user = get_user_data(update.author_guid)
    speed = user["miner_speed"] 

    per_sec = speed
    per_hour = per_sec * 3600
    per_day = per_hour * 24
    per_month = per_day * 30
    per_year = per_day * 365

    await update.reply(
        f"📊 آمار استخراج ماینر:\n\n"
        f"⏱ در ثانیه: {per_sec:,} سکه\n"
        f"🕒 در ساعت: {per_hour:,} سکه\n"
        f"📆 در روز: {per_day:,} سکه\n"
        f"🗓 در ماه: {per_month:,} سکه\n"
        f"📅 در سال: {per_year:,} سکه"
    )

#شرط بندی
@bot.on_message_updates(filters.regex(r"^شرط بندی\s+(.+)\s+(فرد|زوج)$"), filters.is_group)
async def bet_even_odd(update: Updates):
    try:
        match = re.match(r"^شرط بندی\s+(.+)\s+(فرد|زوج)$", update.text.strip())
        if not match:
            await update.reply("❌ فرمت اشتباه است. مثال: شرط بندی 5هزار فرد")
            return

        amount_text = match.group(1)
        choice = match.group(2)
        amount = parse_bet_amount(amount_text)

        if amount is None:
            await update.reply("❌ مقدار شرط نامعتبر است.")
            return

        if is_banned(update.author_guid):
            await update.reply("⛔️ شما از انجام بازی محروم شده‌اید.")
            return

        user = get_user_data(update.author_guid)
        owner = is_owner(update.author_guid)

        if not owner and (user["wallet"] < amount or user["wallet"] <= 1000):
            await update.reply("❌ موجودی شما برای این شرط کافی نیست.")
            return

        result = random.choice(["فرد", "زوج"])
        win = (result == choice)

        if win:
            if not owner:
                user["wallet"] += amount
            await update.reply(
    f"🎯 نتیجه: «{result}» آمد!\n"
    f"🎉 تبریک! شما برنده شدید!\n"
    f"━━━━━━━━━━━━━━━\n"
    f"💰 مبلغ برد: +{amount:,} سکه\n"
    f"🏦 موجودی فعلی: {user['wallet']:,} سکه"
)
        else:
            if not owner:
                user["wallet"] = max(user["wallet"] - amount, 1000)
            await update.reply(
    f"🎯 نتیجه: «{result}» آمد!\n"
    f"😓 متأسفانه باختید...\n"
    f"━━━━━━━━━━━━━━━\n"
    f"💸 مبلغ باخت: -{amount:,} سکه\n"
    f"🏦 موجودی فعلی: {user['wallet']:,} سکه"
)

        save_game()

    except Exception as e:
        await update.reply(f"⚠️ خطا در اجرای شرط‌بندی: {str(e)}")
        
#سنگ کاغذ قیچی

@bot.on_message_updates(filters.regex(r"^(سنگ|کاغذ|قیچی)\s+(\d+)( |$)"), filters.is_group)
async def rock_paper_scissors(update: Updates):
    match = re.match(r"^(سنگ|کاغذ|قیچی)\s+(\d+)", update.text)
    user_choice = match.group(1)
    amount = int(match.group(2))
    user = get_user_data(update.author_guid)

    if user["wallet"] < amount or user["wallet"] <= 1000:
        await update.reply("❌ موجودی کافی ندارید.")
        return

    choices = ["سنگ", "کاغذ", "قیچی"]
    bot_choice = random.choice(choices)

    win = {
        "سنگ": "قیچی",
        "کاغذ": "سنگ",
        "قیچی": "کاغذ"
    }

    if bot_choice == user_choice:
        result = "مساوی شد!"
    elif win[user_choice] == bot_choice:
        user["wallet"] += amount
        result = f"🎉 شما بردید!\n+{amount:,} سکه"
    else:
        user["wallet"] = max(user["wallet"] - amount, 1000)
        result = f"❌ شما باختید!\n-{amount:,} سکه"


    save_game()
    await update.reply(f"🤖 ربات: {bot_choice}\n👤 شما: {user_choice}\n\n{result}\n💰 موجودی: {user['wallet']:,}")
        

#گیفت سکه به کاربری دیگر
@bot.on_message_updates(filters.regex(r"^gift\s+(\d+)\s+@(\w+)", flags=re.IGNORECASE), filters.is_group)
async def gift_coins(update: Updates):
    try:
        sender_guid = update.author_guid
        sender = get_user_data(sender_guid)

        match = re.match(r"^gift\s+(\d+)\s+@(\w+)", update.text.strip(), flags=re.IGNORECASE)
        if not match:
            await update.reply("❗️ فرمت درست نیست. مثال: Gift 10000 @username")
            return

        amount = int(match.group(1))
        target_username = match.group(2)

        if amount <= 0:
            await update.reply("❌ مقدار گیفت باید بیشتر از صفر باشد.")
            return

        # پیدا کردن کاربر از روی یوزرنیم
        try:
            target_user_info = await bot.get_object_by_username(target_username)
            target_guid = target_user_info.user.user_guid
        except:
            await update.reply("❌ کاربر موردنظر یافت نشد.")
            return

        if target_guid == sender_guid:
            await update.reply("❌ نمی‌توانید به خودتان سکه گیفت بدهید.")
            return

        target = get_user_data(target_guid)

        if sender["wallet"] < amount:
            await update.reply(f"❌ موجودی شما کافی نیست. موجودی فعلی: {sender['wallet']:,} سکه")
            return

        # انتقال سکه
        sender["wallet"] -= amount
        target["wallet"] += amount
        save_game()

        await update.reply(
            f"✅ {amount:,} سکه به @{target_username} گیفت شد!\n"
            f"💰 موجودی جدید شما: {sender['wallet']:,} سکه"
        )

    except Exception as e:
        await update.reply(f"⚠️ خطا در اجرای گیفت: {str(e)}")

#لیست پولداران
@bot.on_message_updates(filters.regex("^پولداران$"), filters.is_group)
async def richest_users(update: Updates):
    try:
        all_users = game_data.get("users", {})
        if not all_users:
            await update.reply("❌ هیچ کاربری در دیتابیس ثبت نشده است.")
            return

        ranking = []
        for user_guid, info in all_users.items():
            wallet = info.get("wallet", 0)
            level = info.get("miner_level", 1)
            ranking.append((user_guid, wallet, level))

        ranking.sort(key=lambda x: (x[1], x[2]), reverse=True)

        message = "🏆 لیست پولدارترین کاربران:\n\n"

        for i, (guid, wallet, level) in enumerate(ranking[:10], 1):
            try:
                info = await bot.get_info(guid)
                name = info.user.first_name
                if info.user.last_name:
                    name += f" {info.user.last_name}"
            except:
                name = f"نامشخص ({guid[-5:]})"

            message += f"{i}. 🧑‍💼 {name} | 💰 {wallet:,} سکه | 🔧 ماینر لول {level}\n"

        await update.reply(message.strip())

    except Exception as e:
        await update.reply(f"⚠️ خطا: {str(e)}")
        
#دستور مالکیت گیم بات
@bot.on_message_updates(filters.regex(r"^مالک گیم @(\w+)$"), filters.is_private)
async def set_game_admin(update: Updates):
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if update.author_guid != data.get("admin_guid"):
            await update.reply("⛔️ فقط مالک اصلی می‌تواند ادمین گیم را تعیین کند.")
            return

        match = re.match(r"^مالک گیم @(\w+)$", update.text)
        username = match.group(1)

        info = await bot.get_object_by_username(username)
        new_admin_guid = info.user.user_guid

        data["admin_game"] = new_admin_guid
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        await update.reply(f"✅ کاربر @{username} به عنوان ادمین گیم تنظیم شد.")

    except Exception as e:
        await update.reply(f"⚠️ خطا در تنظیم: {str(e)}")
        
def fix_game_json_structure():
    with open("game.json", "r") as f:
        data = json.load(f)

    corrected_users = data.get("users", {})

    for key in list(data.keys()):
        if key not in ["users", "admins", "banned_users"]:
            if isinstance(data[key], dict):
                corrected_users[key] = data[key]
                del data[key]

    data["users"] = corrected_users
    data.setdefault("admins", [])
    data.setdefault("banned_users", [])

    with open("game.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ ساختار game.json با موفقیت اصلاح شد.")
    
@bot.on_message_updates(filters.regex("^پنل مدیریت$"), filters.is_private)
async def game_admin_panel(update: Updates):
    if not is_game_admin(update.author_guid):
        await update.reply("⛔️ فقط ادمین گیم به این بخش دسترسی دارد.")
        return

    total_users = len(game_data["users"])
    total_wallet = sum(user["wallet"] for user in game_data["users"].values() if isinstance(user["wallet"], int))
    await update.reply(
        f"🛠 پنل مدیریت گیم\n\n"
        f"👥 کاربران ثبت‌شده: {total_users}\n"
        f"💰 مجموع سکه‌ها: {total_wallet:,}"
    )

#افزودن سکه
@bot.on_message_updates(filters.regex(r"^افزودن سکه\s+(\d+)\s+@(\w+)$"), filters.is_private)
async def add_wallet(update: Updates):
    if not is_game_admin(update.author_guid):
        await update.reply("⛔️ فقط ادمین گیم اجازه دارد.")
        return

    match = re.match(r"^افزودن سکه\s+(\d+)\s+@(\w+)$", update.text)
    amount, username = int(match.group(1)), match.group(2)

    try:
        info = await bot.get_object_by_username(username)
        target_guid = info.user.user_guid
        user = get_user_data(target_guid)
        user["wallet"] += amount
        save_game()
        await update.reply(f"✅ {amount:,} سکه به @{username} اضافه شد.")
    except:
        await update.reply("❌ کاربر یافت نشد.")
        
# تابع تنظیم ماینر برای کاربر از طریق ادمین گیم
@bot.on_message_updates(filters.regex(r"^تنظیم ماینر\s+(\d+)\s+@(\w+)$"), filters.is_private)
async def set_miner(update: Updates):
    if not is_game_admin(update.author_guid):
        await update.reply("⛔️ فقط ادمین گیم اجازه دارد.")
        return

    match = re.match(r"^تنظیم ماینر\s+(\d+)\s+@(\w+)$", update.text)
    if not match:
        await update.reply("❗️ فرمت درست نیست. مثال: تنظیم ماینر 5 @username")
        return

    level, username = int(match.group(1)), match.group(2)

    try:
        info = await bot.get_object_by_username(username)
        target_guid = info.user.user_guid
        user = get_user_data(target_guid)
        user["miner_level"] = level
        user["miner_speed"] = 1000 * level
        save_game()
        await update.reply(f"✅ سطح ماینر @{username} تنظیم شد به {level}.")
    except:
        await update.reply("❌ کاربر یافت نشد.")

#بازنشانی کاربر
@bot.on_message_updates(filters.regex(r"^بازنشانی @(\w+)$"), filters.is_private)
async def reset_user(update: Updates):
    if not is_owner(update.author_guid):
        await update.reply("⛔️ فقط مالک ربات اجازه دارد.")
        return

    match = re.match(r"^بازنشانی @(\w+)$", update.text)
    if not match:
        await update.reply("❗️ فرمت اشتباه است. مثال: بازنشانی @username")
        return

    username = match.group(1)

    try:
        info = await bot.get_object_by_username(username)
        guid = info.user.user_guid
        game_data["users"].pop(guid, None)
        save_game()
        await update.reply(f"✅ اطلاعات کاربر @{username} با موفقیت بازنشانی شد.")
    except:
        await update.reply("❌ کاربر یافت نشد.")
        
# قفل گیم بات برای کاربر
@bot.on_message_updates(filters.regex(r"^قفل گیم @(\w+)$"), filters.is_private)
async def lock_game_for_user(update: Updates):
    if not is_game_admin(update.author_guid):
        await update.reply("⛔️ فقط ادمین گیم اجازه دارد.")
        return

    match = re.match(r"^قفل گیم @(\w+)$", update.text)
    username = match.group(1)

    try:
        info = await bot.get_object_by_username(username)
        target_guid = info.user.user_guid

        if target_guid not in game_data["banned_users"]:
            game_data["banned_users"].append(target_guid)
            save_game()
            await update.reply(f"✅ گیم بات برای کاربر @{username} قفل شد.")
        else:
            await update.reply(f"⚠️ کاربر @{username} قبلاً قفل شده است.")
    except:
        await update.reply("❌ کاربر یافت نشد.")
        
# خاموش و روشن کردن گیم بات
@bot.on_message_updates(filters.regex("^خاموش/روشن گیم بات$"), filters.is_private)
async def toggle_game_status(update: Updates):
    if not is_game_admin(update.author_guid):
        await update.reply("⛔️ فقط ادمین گیم اجازه دارد.")
        return

    game_active = game_data.get("game_active", True)
    game_data["game_active"] = not game_active
    save_game()

    if game_data["game_active"]:
        await update.reply("✅ گیم بات روشن شد.")
    else:
        await update.reply("⛔️ گیم بات خاموش شد.")
        
#راهنما
@bot.on_message_updates(filters.regex(r"^راهنما$"), filters.is_private | filters.is_group)
async def game_help(update: Updates):
    await update.reply(
        """📘 راهنمای گیم‌بات:

🔹 دستورهای عمومی:

💰 موجودی → نمایش کیف پول شما
 🎰 گردونه → چرخ شانس روزانه
 ⛏ جمع ماینر → انتقال درآمد ماینر به کیف پول
 🛠 ماینر → نمایش اطلاعات ماینر
 💸 خرید ماینر → ارتقاء یک سطح ماینر
 🚀 خرید حداکثر ماینر → ارتقاء تا جایی که سکه دارید
 📈 پروفیت → نمایش درآمد ساعتی و روزانه


🎲 شرط‌بندی:

 🎯 شرط بندی [مقدار] [فرد/زوج]
 🪨 سنگ [مقدار]
 📄 کاغذ [مقدار]
 ✂️ قیچی [مقدار]

🎁 گیفت:

 gift [مقدار] @[یوزرنیم] → ارسال سکه به کاربر دیگر


🏆 سایر:

 پولداران → نمایش ۱۰ کاربر برتر


⚙️ مخصوص ادمین گیم:

 مالک گیم @[یوزرنیم] → تعیین ادمین گیم (فقط برای مالک اصلی)
 پنل مدیریت → مشاهده وضعیت کلی کاربران و سکه‌ها
 افزودن سکه [مقدار] @[یوزرنیم]
 کم کردن سکه [مقدار] @[یوزرنیم]
 تنظیم ماینر [سطح] @[یوزرنیم]
 قفل کاربر @[یوزرنیم]
 بازنشانی کاربر @[یوزرنیم]
خاموش ← غیرفعال کردن گیم‌بات
 روشن ← فعال‌سازی دوباره گیم‌بات

        """.strip()
    )


def fix_game_json_structure():
    with open("game.json", "r") as f:
        data = json.load(f)

    corrected_users = data.get("users", {})


    for key in list(data.keys()):
        if key not in ["users", "admins", "banned_users"]:
            if isinstance(data[key], dict):
                corrected_users[key] = data[key]
                del data[key]

    data["users"] = corrected_users
    data.setdefault("admins", [])
    data.setdefault("banned_users", [])

    with open("game.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ ساختار game.json با موفقیت اصلاح شد.")
    
    
def auto_mine_loop():
    while True:
        time.sleep(1)
        users = game_data.get("users", {})
        for user_guid, user in users.items():
            speed = user.get("miner_speed", 0)
            user["miner_storage"] = user.get("miner_storage", 0) + speed
        save_game()
        
threading.Thread(target=auto_mine_loop, daemon=True).start()
fix_game_json_structure()
bot.run()