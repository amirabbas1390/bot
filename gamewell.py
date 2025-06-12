import logging
import random
import re
import sqlite3
import time
import pytz
import os
from datetime import datetime
from telegram import Update, ChatMember, Chat
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext

# اطلاعات پایه
TOKEN = "8101325163:AAHq7tv46EIHvJ2s1LXi-g-_4DHJRXoOE98"
OWNER_ID = 7412392035
OWNER_RUBIKA = "@Jnjnndowl"
CHANNEL_USERNAME = "bot_free_dino"
CHANNEL_LINK = "https://t.me/bot_free_dino"
RUBIKA_LINK = "https://rubika.ir/www_free_ir"

# محل ذخیره دیتابیس (داخل حافظه گوشی کاربر)
DB_PATH = os.path.join(os.path.expanduser("~"), "dino_full_game_bot.db")
DB = sqlite3.connect(DB_PATH, check_same_thread=False)
CUR = DB.cursor()

CUR.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    coin INTEGER DEFAULT 5000,
    miner_level INTEGER DEFAULT 1,
    miner_last_collect INTEGER DEFAULT 0,
    wheel_time INTEGER DEFAULT 0,
    exp INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    join_date INTEGER DEFAULT 0,
    serial TEXT DEFAULT '',
    is_subscribed INTEGER DEFAULT 1
)""")
CUR.execute("""CREATE TABLE IF NOT EXISTS serials(
    code TEXT PRIMARY KEY,
    amount INTEGER,
    creator_id INTEGER,
    used_by INTEGER DEFAULT NULL
)""")
CUR.execute("""CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    type TEXT,
    detail TEXT,
    amount INTEGER,
    timestamp INTEGER
)""")
DB.commit()

bot_status = {'active': True, 'subscription': False}

def comma(n):
    return "{:,}".format(int(n))

def get_iran_time():
    return datetime.now(pytz.timezone("Asia/Tehran"))

def get_user(user_id, username='', first_name=''):
    CUR.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = CUR.fetchone()
    if not user:
        CUR.execute("INSERT INTO users (user_id, username, first_name, join_date) VALUES (?, ?, ?, ?)",
                    (user_id, username, first_name, int(get_iran_time().timestamp())))
        DB.commit()
        return get_user(user_id)
    return user

def set_coin(user_id, coin):
    CUR.execute("UPDATE users SET coin=? WHERE user_id=?", (coin, user_id))
    DB.commit()

def add_coin(user_id, amount):
    u = get_user(user_id)
    set_coin(user_id, u[3] + amount)

def sub_coin(user_id, amount):
    u = get_user(user_id)
    set_coin(user_id, u[3] - amount)

def log_transaction(user_id, tx_type, detail, amount):
    CUR.execute("INSERT INTO transactions (user_id, type, detail, amount, timestamp) VALUES (?, ?, ?, ?, ?)",
                (user_id, tx_type, detail, amount, int(get_iran_time().timestamp())))
    DB.commit()

def leaderboard():
    CUR.execute("SELECT user_id, username, first_name, coin FROM users ORDER BY coin DESC LIMIT 10")
    rows = CUR.fetchall()
    msg = "🏆 10 نفر برتر پولدار:\n"
    for i, (user_id, username, first_name, coin) in enumerate(rows, 1):
        name = first_name or "بدون نام"
        link = f"<a href='tg://user?id={user_id}'>{name}</a>" if user_id else name
        user_link = f"@{username}" if username else ""
        msg += f"({i}) {link} {user_link} | <code>{user_id}</code> 💰 {comma(coin)} سکه\n"
    return msg

def get_user_by_username(username):
    CUR.execute("SELECT * FROM users WHERE username=?", (username,))
    return CUR.fetchone()

def generate_serial(amount, creator_id):
    while True:
        code = "SERIAL-" + ''.join([str(random.randint(0,9)) for _ in range(6)])
        CUR.execute("SELECT * FROM serials WHERE code=?", (code,))
        if not CUR.fetchone():
            CUR.execute("INSERT INTO serials (code, amount, creator_id) VALUES (?, ?, ?)", (code, amount, creator_id))
            DB.commit()
            return code

def use_serial(code, user_id):
    CUR.execute("SELECT * FROM serials WHERE code=? AND used_by IS NULL", (code,))
    serial = CUR.fetchone()
    if serial:
        CUR.execute("UPDATE serials SET used_by=? WHERE code=?", (user_id, code))
        DB.commit()
        return serial[1]
    return None

async def is_user_subscribed(app, user_id):
    try:
        m = await app.bot.get_chat_member(f"@{CHANNEL_USERNAME}", user_id)
        return m.status in [ChatMember.MEMBER, ChatMember.OWNER, ChatMember.ADMINISTRATOR]
    except:
        return False

def miner_hourly_income(level):
    # فرمول درآمد ساعتی ماینر بر اساس لول
    return 1000 * level ** 2

def miner_upgrade_cost(level):
    # فرمول هزینه ارتقا ماینر به لول بعدی
    return 5000 * level ** 2

def get_miner(user_id):
    u = get_user(user_id)
    return {
        "level": u[4],
        "last_collect": u[5],
        "coin": u[3],
        "first_name": u[2],
        "user_id": u[0]
    }

def set_miner_level(user_id, level):
    CUR.execute("UPDATE users SET miner_level=? WHERE user_id=?", (level, user_id))
    DB.commit()

def set_miner_last_collect(user_id, timestamp):
    CUR.execute("UPDATE users SET miner_last_collect=? WHERE user_id=?", (timestamp, user_id))
    DB.commit()

async def welcome_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    iran_now = get_iran_time()
    await update.message.reply_text(
        f"سلام {update.effective_user.first_name} عزیز 🌚\n"
        f"به گروه {update.effective_chat.title} خوش اومدی 💚\n"
        f"تاریخ » {iran_now.strftime('%Y-%m-%d')} 📆\n"
        f"ساعت » {iran_now.strftime('%H:%M')} ⏱"
    )

async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    app = context.application
    if not await is_user_subscribed(app, user_id):
        await update.message.reply_text(
            f"برای استفاده از ربات باید در چنل زیر عضو شوید.\n ◍⁠ {CHANNEL_LINK}"
        )
        return False
    return True

async def send_help(update: Update):
    help_msg = """
❓ <b>راهنمای ربات داینو گیم تلگرام</b> ❓

<b>دستورات عمومی:</b>
- <b>موجودی</b> : نمایش مقدار سکه شما
- <b>سازنده</b> : نمایش مشخصات سازنده ربات
- <b>پولداران</b> : مشاهده 10 نفر برتر پولدار ربات
- <b>گردونه</b> : دریافت جایزه روزانه از گردونه (هر 24 ساعت یکبار)
- <b>انتقال @ایدی مقدار</b> : انتقال سکه به کاربر دیگر (مثال: انتقال @user123 1000)
- <b>شرط بندی مقدار زوج/فرد</b> : شرط بندی روی تاس (مثال: شرط بندی 50 زوج)
- <b>دست راست مقدار / دست چپ مقدار</b> : بازی گل یا پوچ (مثال: دست راست 100)
- <b>ساخت سریال مقدار</b> : ساخت سریال با توجه به مقدار پول شما
- <b>استفاده SERIAL-xxxxxx</b> : استفاده از سریال هدیه
- <b>دعوت</b> : دریافت لینک دعوت اختصاصی
- <b>ماینر</b> : مشاهده و مدیریت ماینر (درآمدزایی ساعتی)
- <b>جمع ماینر</b> : جمع‌آوری درآمد ساعتی ماینر
- <b>ارتقا ماینر</b> : ارتقا لول ماینر
- <b>راهنما</b> : نمایش این راهنما

<b>توجه:</b>
- برای ساخت سریال، باید به اندازه مبلغ سریال، سکه داشته باشید.
- اطلاعات بازی شما، روی گوشی شما در مسیر home ذخیره می‌شود و امن هست.

<b>ارتباط با سازنده:</b>
{rubika}
""".replace("{rubika}", OWNER_RUBIKA)
    await update.message.reply_text(help_msg, parse_mode="HTML", disable_web_page_preview=True)

async def group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not bot_status['active']:
        return
    user = update.effective_user
    text = update.message.text.strip()
    get_user(user.id, user.username or f"user{user.id}", user.first_name)
    if not await check_subscription(update, context): return

    # ---------------------- ماینر ----------------------
    if text == "ماینر":
        u = get_user(user.id, user.username or f"user{user.id}", user.first_name)
        if u[4] == 1 and u[5] == 0:  # اولین درخواست ماینر
            set_miner_last_collect(user.id, int(get_iran_time().timestamp()))
            await update.message.reply_text("✅ شما به عنوان یک ماینر جدید اضافه شدید!")
            return
        miner = get_miner(user.id)
        income = miner_hourly_income(miner['level'])
        upgrade_price = miner_upgrade_cost(miner['level'])
        next_income = miner_hourly_income(miner['level'] + 1)
        msg = f"""👤 کاربر : {miner['first_name']}
🎟 لول ماینر : {miner['level']}
💵 سکه ساعتی : {comma(income)}💰
🔥 آماده‌ای که ماینرتو به لول بعدی برسونی و درآمدت رو چند برابر کنی؟ بگو ارتقا ماینر💡🔋
⚡️ قیمت لول بعدی : {comma(upgrade_price)} سکه
⚡️ سکه لول بعدی : {comma(next_income)} سکه در هر ساعت
🎉 میخوای بدست بیاریش؟ بگو جمع ماینر💡
"""
        await update.message.reply_text(msg)
        return

    if text == "جمع ماینر":
        miner = get_miner(user.id)
        now = int(get_iran_time().timestamp())
        elapsed = now - miner["last_collect"]
        if elapsed < 3600:
            remain = 3600 - elapsed
            min_ = remain // 60
            sec_ = remain % 60
            await update.message.reply_text(f"❌ هنوز {min_} دقیقه و {sec_} ثانیه تا جمع ماینر بعدی باقی مانده.")
            return
        income = miner_hourly_income(miner["level"])
        add_coin(user.id, income)
        set_miner_last_collect(user.id, now)
        await update.message.reply_text(f"🎉 شما {comma(income)} سکه ماینر جمع‌آوری کردید! 💰 موجودی جدید شما: {comma(get_user(user.id)[3])} سکه")
        log_transaction(user.id, "جمع ماینر", f"سطح {miner['level']}", income)
        return

    if text == "ارتقا ماینر":
        miner = get_miner(user.id)
        upgrade_price = miner_upgrade_cost(miner["level"])
        if miner["coin"] < upgrade_price:
            await update.message.reply_text(f"❌ موجودی کافی برای ارتقا ندارید! قیمت ارتقا: {comma(upgrade_price)} سکه")
            return
        sub_coin(user.id, upgrade_price)
        set_miner_level(user.id, miner["level"] + 1)
        await update.message.reply_text(f"✅ شما به لول {miner['level'] + 1} ارتقا پیدا کردید! هزینه ارتقا: {comma(upgrade_price)} سکه")
        log_transaction(user.id, "ارتقا ماینر", f"ارتقا به سطح {miner['level'] + 1}", -upgrade_price)
        return
    # ---------------------------------------------------

    # راهنما
    if text in ["راهنما", "/help", "help", "/راهنما"]:
        await send_help(update)
        return

    # موجودی
    if text in ["موجودی", "موجودی من", "موجودی؟"]:
        u = get_user(user.id)
        await update.message.reply_text(f"موجودی شما : {comma(u[3])} سکه")
        return

    # سازنده
    if text == "سازنده":
        return await update.message.reply_text(f"ایدی سازنده روبیکا: {OWNER_RUBIKA}")

    # پولداران
    if text == "پولداران":
        await update.message.reply_text(leaderboard(), parse_mode="HTML")
        return

    # گردونه
    if text == "گردونه":
        u = get_user(user.id)
        now = int(get_iran_time().timestamp())
        if now - u[6] < 86400:
            return await update.message.reply_text("شما هر 24 ساعت فقط یکبار می‌توانید گردونه را بچرخانید.")
        prize = random.randint(1000, 100000000000)
        add_coin(user.id, prize)
        CUR.execute("UPDATE users SET wheel_time=? WHERE user_id=?", (now, user.id))
        DB.commit()
        log_transaction(user.id, "گردونه", "گردونه روزانه", prize)
        return await update.message.reply_text(
            f"🎁 شما {comma(prize)} سکه از گردونه دریافت کردید!\n💰 موجودی جدید: {comma(get_user(user.id)[3])} سکه"
        )

    # انتقال سکه
    if text.startswith("انتقال"):
        m = re.findall(r"انتقال\s+@(\w+)\s+(\d+)", text)
        if not m:
            return await update.message.reply_text("فرمت صحیح: انتقال @ایدی مقدار\nمثال: انتقال @user123 1000")
        to_username, amount = m[0]
        amount = int(amount)
        u = get_user(user.id)
        to_user = get_user_by_username(to_username)
        if not to_user:
            return await update.message.reply_text("کاربر مورد نظر یافت نشد.")
        if u[3] < amount:
            return await update.message.reply_text("❌ موجودی کافی برای انتقال ندارید.")
        sub_coin(user.id, amount)
        add_coin(to_user[0], amount)
        log_transaction(user.id, "انتقال", f"به @{to_username}", -amount)
        log_transaction(to_user[0], "دریافت", f"از @{u[1]}", amount)
        return await update.message.reply_text(
            f"✅ شما {comma(amount)} سکه به @{to_username} انتقال دادید."
        )

    # شرط بندی تاس
    if text.startswith("شرط بندی"):
        m = re.findall(r"شرط بندی\s+(\d+)\s+(زوج|فرد)", text)
        if not m:
            return await update.message.reply_text("فرمت صحیح: شرط بندی (مقدار عدد شرط) (زوج/فرد)\nمثال: شرط بندی 50 زوج")
        amount, typ = m[0]
        amount = int(amount)
        u = get_user(user.id)
        if u[3] < amount:
            return await update.message.reply_text("❌ موجودی کافی ندارید.")
        dice = random.randint(1, 6)
        win = (typ == "زوج" and dice % 2 == 0) or (typ == "فرد" and dice % 2 == 1)
        if win:
            add_coin(user.id, amount)
            log_transaction(user.id, "برد تاس", f"تاس {dice}", amount)
            return await update.message.reply_text(
                f"""🎉 بردی! 🎲
🔢 عدد تاس: {dice}
📊 شرط: {comma(amount)} سکه
🏆 جایزه: {comma(2*amount)} سکه
💰 موجودی جدید: {comma(get_user(user.id)[3])} سکه"""
            )
        else:
            sub_coin(user.id, amount)
            log_transaction(user.id, "باخت تاس", f"تاس {dice}", -amount)
            return await update.message.reply_text(
                f"""❌ باختی! 🎲
🔢 عدد تاس: {dice}
📊 شرط: {comma(amount)} سکه
🕳 مبلغ کسر شده: {comma(amount)} سکه
💰 موجودی جدید: {comma(get_user(user.id)[3])} سکه"""
            )

    # گل یا پوچ
    if text.startswith("دست"):
        m = re.findall(r"دست\s+(چپ|راست)\s+(\d+)", text)
        if not m:
            return await update.message.reply_text(
                "لطفاً پیام خود را به شکل 'دست راست 5' یا'دست چپ 10' وارد کنید."
            )
        choice, amount = m[0]
        amount = int(amount)
        u = get_user(user.id)
        if u[3] < amount:
            return await update.message.reply_text("❌ موجودی کافی ندارید.")
        bot_hand = random.choice(["چپ", "راست"])
        if choice == bot_hand:
            add_coin(user.id, amount)
            log_transaction(user.id, "برد گل یا پوچ", f"{choice}", amount)
            return await update.message.reply_text(
                f"""🎮بازی گل یا پوچ
👊دست مورد نظر شما: {choice}
👊دست گل دار ربات: {bot_hand}
🌟  هورا بردی!
 موجودی جدید شما: {comma(get_user(user.id)[3])}💰"""
            )
        else:
            sub_coin(user.id, amount)
            log_transaction(user.id, "باخت گل یا پوچ", f"{choice}", -amount)
            return await update.message.reply_text(
                f"""🎮بازی گل یا پوچ
👊دست مورد نظر شما: {choice}
👊دست گل دار ربات: {bot_hand}
😢 باختی!
 موجودی جدید شما: {comma(get_user(user.id)[3])}💰"""
            )

    # سریال سازی
    if text.startswith("ساخت سریال"):
        m = re.findall(r"ساخت سریال\s+(\d+)", text)
        if not m:
            return await update.message.reply_text("فرمت صحیح: ساخت سریال مقدار")
        amount = int(m[0])
        u = get_user(user.id)
        if u[3] < amount:
            return await update.message.reply_text("❌ موجودی کافی برای ساخت سریال ندارید.")
        sub_coin(user.id, amount)
        code = generate_serial(amount, user.id)
        try:
            await context.bot.send_message(user.id, f"🤯 سریال شما ساخته شد!\n\n🔑 کد سریال: {code}\n💎 مبلغ قابل دریافت: {comma(amount)} سکه\n\n🎁 برای استفاده از سریال، دستور زیر را وارد کنید:\nاستفاده {code}")
            await update.message.reply_text("〔✅〕 سریال شما ساخته شد و به پیوی شما ارسال شد.", reply_to_message_id=update.message.id)
        except Exception:
            await update.message.reply_text("امکان ارسال سریال به پیوی وجود ندارد.")

    # استفاده از سریال
    if text.startswith("استفاده"):
        m = re.findall(r"استفاده\s+(SERIAL-\d{6})", text)
        if not m:
            return await update.message.reply_text("〔⚠️〕 کد سریال وارد نشده است!")
        code = m[0]
        amount = use_serial(code, user.id)
        if not amount:
            return await update.message.reply_text("〔⚠️〕 کد سریال وارد نشده است یا قبلا استفاده شده!")
        add_coin(user.id, amount)
        await update.message.reply_text(f"✅ {comma(amount)} سکه به حساب شما افزوده شد! موجودی جدید شما: {comma(get_user(user.id)[3])} سکه")

    # دعوت
    if text == "دعوت":
        link = f"https://t.me/{context.bot.username}?start={user.id}"
        try:
            await context.bot.send_message(
                user.id,
                f"✨ لینک دعوت اختصاصی شما:\n{link}\n\nهر کسی با این لینک وارد شود، به شما جایزه تعلق می‌گیرد!"
            )
        except Exception:
            await update.message.reply_text("❌ امکان ارسال پیام به پیوی شما وجود ندارد. لطفاً به ربات پیام دهید و دوباره امتحان کنید.")
            return
        await update.message.reply_text("لینک اختصاصی شما به پیویتان ارسال شد ✅")
        return

async def private(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user.id == OWNER_ID:
        text = update.message.text.strip()
        # لیست کاربران
        if text == "کاربران":
            CUR.execute("SELECT user_id, first_name, coin FROM users")
            users = CUR.fetchall()
            msg = ""
            for u in users:
                msg += f"{u[1]} | {comma(u[2])} سکه | {u[0]}\n"
            await update.message.reply_text(msg or "کاربری ثبت نشده است.")
        # افزایش سکه
        elif text.startswith("افزایش سکه"):
            m = re.findall(r"افزایش سکه (\d+) (\d+)", text)
            if m:
                user_id, amount = map(int, m[0])
                add_coin(user_id, amount)
                await update.message.reply_text("افزایش سکه انجام شد.")
        # کاهش سکه
        elif text.startswith("کاهش سکه"):
            m = re.findall(r"کاهش سکه (\d+) (\d+)", text)
            if m:
                user_id, amount = map(int, m[0])
                sub_coin(user_id, amount)
                await update.message.reply_text("کاهش سکه انجام شد.")
        elif text == "خاموش":
            bot_status["active"] = False
            await update.message.reply_text("ᯤ̸ ربات خاموش شد.")
        elif text == "روشن":
            bot_status["active"] = True
            await update.message.reply_text("ᯤ ربات روشن شد.")
        else:
            await update.message.reply_text("دستور مدیریتی نامعتبر است.")
    else:
        return

async def on_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ᯤ ربات گیم تلگرام فعال شد.\nبرای مشاهده راهنما، عبارت راهنما را ارسال کنید.")

def main():
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", on_start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_group))
    app.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.TEXT, private))
    app.add_handler(MessageHandler(filters.ChatType.GROUPS & filters.TEXT, group))
    print("ᯤ ربات روشن شد!")
    app.run_polling()

if __name__ == "__main__":
    main()