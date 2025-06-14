import subprocess
import sys

required_packages = [
    'pyrubi',
    'requests',
    'jdatetime',
    'regex'
]

def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f'در حال نصب {package} ...')
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
package_map = {
    'pyrubi': 'pyrubi',
    'requests': 'requests',
    'jdatetime': 'jdatetime',
    'regex': 'regex'
}

for module_name in required_packages:
    install_package(package_map[module_name])


from pyrubi import Client
from pyrubi.types import Message
import requests
import random
import jdatetime
from datetime import datetime
from datetime import datetime, timedelta
from time import sleep
import os
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import re
import pickle
import threading
import regex
import copy
import base64

# 📦 بارگذاری دیتابیس سخنگو
import pickle
import os
import random

SPEAK_DATA_FILE = "speak_data.pkl"
if os.path.exists(SPEAK_DATA_FILE):
    with open(SPEAK_DATA_FILE, "rb") as f:
        speak_data = pickle.load(f)
else:
    speak_data = {
        "polite": {
            "سلام": ["سلام گلم خوبی؟", "درود بر تو فرزند گلم❤️", "سلام گوگولی😘"],
            "خبی": ["عالییییم", "با وجود تو اره❤️💋", "تو خوب باشی من عالیم"]
        },
        "rude": {
            "سلام": ["سلام و ک/ی/ر", "اه"],
            "بخور": ["نداری", "بدو"]
        },
        "smart": {},
        "enabled": {}
    }
def save_speak():
    with open(SPEAK_DATA_FILE, "wb") as f:
        pickle.dump(speak_data, f)

bot=Client('soroosh_alfo')
first_message_time = None

message_times = []

file_name = "save.pkl"
file_talk = "data.pkl"
file_best_talk = "clean_data.pkl"

# تابع عمومی برای بارگذاری داده‌ها از فایل pickle


def load_data(file_path, default_value=None):
    if os.path.exists(file_path):
        try:
            with open(file_path, "rb") as file:
                return pickle.load(file)
        except (pickle.UnpicklingError, EOFError):
            print(f"خطا در بارگذاری فایل {file_path}. مقدار پیش‌فرض استفاده شد.")
    return default_value or {}

def save_data(file_path, data):
    with open(file_path, "wb") as file:
        pickle.dump(data, file)

# مقداردهی متغیر file_talk
file_talk = "data.pkl"
kos="u0HJ9Hk0cf69cd39c78d2ef194e9fe40"
# بارگذاری داده‌ها
talk = load_data(file_talk, {})
best_talk = load_data(file_best_talk, {})
save = load_data(file_name, {
    "Anonymous_message": True,
    "maker": "",
    "message":0,
    "maker_asl": ["",'u0F8dTt0cee5aa71f5a29888ff90dddd',"u0F8dTt0cee5aa71f5a29888ff90dddd"],
    "chalesh": ['✨1.تو گپ رو کی کراشی و نمیتونی بگی؟', '✨2.کی بیشتر رو مخته؟', '✨3.کدوم اخلاقم گنده؟', '✨4.کدوم اخلاقمو دوس داری؟', '✨5.غذای مورد علاقت؟(فست\u200cفود_خانگی)', '✨6.کنار دریا یا جنگل؟', '✨7.شب یا روز؟', '✨8.بارون یا برف؟', '✨9.دوس داری پیش مرگ کسی بشی؟کی؟', '✨10ـاگه کفنت جیب داشته باشه،باخودت چی میبری؟', '✨21.چنتا خواهر داری؟', '✨22.چنتا برادر داری؟', '✨23.دوست داری تک فرزند باشی؟', '✨24.راجب من یه چیزی بگو؟', '✨25.درس خوندن دوست داری؟', '✨26.هدفت برای اینده؟', '✨27.رشتت چیه؟', '✨28.برادرتو دوست داری؟', '✨30.خواهر دوست داری؟', '✨31.کدوم درست تجدید شدیـ', '✨32.گرما بیشتر دوست داری یا سرما', '✨33.چه مدل گلی دوست داریـ', '✨34.گل و درخت بیشتر دوست داری با حیواناتـ', '✨35.فصل چی بدنیا اومدیـ', '✨36.ماه چی به دنیا اومدیـ', '✨37.از کدوم همکلاسیت متنفریـ', '✨38.از کدوم همکلاسیت خوشت میاد', '✨39.کدوم مدیر تو بیشتر دوس داریـ', '✨40.کدوم یک از سیارات بیشتر دوست داریـ', '✨41.با مامانت راحتی یا بابات؟', '✨42.چنتا بچه\u200cاین؟', '✨43.اخلاقای بدت چیه؟', '✨44.اخلاقای خوبت چیه؟', '✨45.دس رو جنس مخالفت بلند کردی؟', '✨46.سیگار یا قلیون؟', '✨47.بد ترین سوتیت چی بوده؟', '✨48.اهنگ قفلیت؟', '✨49.چ رقصی بلدی؟', '✨50.پارتی یا جداگونه؟', '✨51.افسرده شدی؟', '✨52.پول یا قلب؟', '✨53.قدت؟', '✨54.اگه بهت بگن س تا آرزو کن چه ارزویی میکنی؟', '✨55.جزو س نفر مهم زندگیت هستم؟', '✨56.سنت؟', '✨57.چند کیلویی؟', '✨58.چی بهت ارامش میده؟', '✨59.تاریخ تولدت؟', '✨60.اخلاقم چجوریه؟', '✨61.بوسم میکنی؟', '✨62.رنگ مورد علاقت؟', '✨63.عشق اولت کیه؟', '✨64.دلت برا کی تنگه؟', '✨65. اهنگ مورد علاقت؟\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 \u200c', '✨66.بنظرت من چجور ادمیم؟', '✨67.شکست عشقی خوردی؟', '✨68.بنظرت من چجور ادمیم؟', '✨69.حیوان مورد علاقت؟', '✨70.اصلی\u200cترین چیزی که توی جنس مقابل برای تو جذابه چیه؟', '✨71.معیارهات برای ورود به یک رابطه چی هستن؟', '✨72.در مورد اولین تجربه\u200cی عاشقانه\u200c ات بگو ؟', '✨73.یه قسمت خنده\u200cدار از اولین تجربه\u200cی پرحرارت زندگیت رو تعریف کن؟', '✨74.بدترین ویژگی بغل دستیت چیه؟', '✨75.بدترین قرارت با یه پسر چطوری بوده؟', '✨76.تا به حال از دوست\u200cپسر یا دوست\u200cدختر دوستت خوشت اومده؟', '✨77.تا به حال شده پسری که دوستش داری بفهمه، و بهت جواب منفی بده؟', '✨78.برای اینکه جذاب به نظر برسی چه کار می\u200cکنی؟', '✨79.در حال حاضر از کی خوشت میاد؟', '✨80.اگر می\u200cتونستی یک چیز در بدنت رو تغییر بدی اون چی بود؟', '✨81.به کی حسودی می\u200cکنی؟', '✨82.پنج پسر اولی که به نظرت جذابن رو نام ببر؟', '✨83.اگر می\u200cتونستی نامرئی بشی چکار می\u200cکرد؟', '✨84.جذابترین دختران کلاس (جمع یا مدرسه) کدامند؟', '✨85.چند بار تو مدرسع دعوا کردی', '✨86.چطوری سوتی هات جمع می کنی', '✨87.کدوم امتحانت خیلی خوب دادی', '✨88.امتحان شفایی دوس داری یا کتبی', '✨89.اسکریت از پیام های شخصیت', '✨90.شغلی که دوس داری داشته باشی', '✨91.میری سر کار', '✨92.شغلت چیه', '✨93.روزانه حداقل چند آب میخوری', '✨94.چند تا دفتر داری', '✨95.کلاس زبان میری ترم چندی', '✨96.چند بار بلاک شدی', '✨97.حلقه بلدی بزنی', '✨98.فرش خونه تون چه رنگی', '✨99.درامدت چقدره', '✨100.رخت اویز مامانت پهن میکنه یا تو', '🦋۱ از چه درسی متنفری', '🦋۲ چه درسو بیشتر دوس داری', '🦋۳اخرین باری ک قلیون کشیدی کی\u200cبود', '🦋۴ اولین باری ک قلیون کشیدی چند سالت بود', '🦋۵اخرین باری ک سیگار کشیدی کی بود', '🦋۶ موی بلند دوس داری یا کوتاه', '🦋۷ دختر قد کوتاه یا قد بلند', '🦋۸ دختر اروم یا شی\u200cطون', '🦋۹ پسر اروم و ساکت یا شی\u200cطون و شلوغ', '🦋۱۰ با کی بیشتر بهت خوش میگذره', '🦋۱۱ با کی اصلا بهت خوش نمیگذره', '🦋۱۲ یکی از بهترین فامیلای ک داری و بگو', '🦋۱۳ اگه میتونستی یه نفر و از زندگیت بندازی بیرون کی بود', '🦋۱۴ اگه میتونستی یه نفر و از جمع بندازی بیرون اون کی بود', '🦋۱۵ کیو بیشتر از همه تو جمع دوس داری', '🦋۱۶از چیه خودت بدت میاد', '🦋۱۷\xa0 آخرین نمره ی ریاضی ک گرفتی چند بود', '🦋۱۸ تیکه کلام یکی از بچه های جمع و بگو', '🦋۱۹ ادای یکی از معلمای مدرستو دربیار', '🦋۲۰ بامزه ترین جوکی ک شنیدی و بگو', '🦋۲۱ بی مزه ترین جوکی ک شنیدی و بگو', '🦋۲۲ خزترین تیپی ک دیدی و بگو چجوری بود', '🦋۲۳ بدترین اسم پسر از نظرت چیه', '🦋۲۴\xa0 قشنگترین اسم دختر از نظرت چیه', '🦋۲۵ تا حالا از روی اجبار با کسی بودی', '🦋۲۶ عشق یا پول', '🦋۲۷ کدومش بدتره بی پول خوشحال یا پولدار ناراحت', '🦋۲۸ دوس داری خیا نت کنی یا خیانت ببینی', '🦋۲۹ عشقت خی انت کنه واکنشت چیه', '🦋۳۰ خاطره ای از مامانت ک دعوات کرده', '🦋۳۱ چند بار تا حالا دزدی کردی', '🦋۳۲ مامانت تاحالا مچتو با دختر /پسر گرفته', '🦋۳۳ پسر موهاش فر باشه یا صاف', '🦋۳۴ دختر موهاش فر باشه با صاف', '🦋۳۵ تاکسی بهتره یا اتوبوس', '🦋۳۶ آخرین باری ک با رلت بیرون رفتی کی بود', '🦋۳۷ آخرین چتت با ر لت و شات بده', '🦋۳۸ چه فکری راجب من\u200cمیگنی\u200c', '🦋۳۹ چند بار دعوا کردی', '🦋۴۰ کتک خوردی تا حالا', '🦋۴۱ تشنگی بدتره یا گرسنگی', '🦋۴۲ وقتی خیلی گرمت میشه چیکار میکنی', '🦋۴۳ تو تابستون چی میچسبه', '🦋۴۴ دلیل ر ل زدنت', '🦋۴۵ ر لت چه ویژگی داره ک عاشقش شدی', '💛1.تا ب حال اسب سوار شدی؟', '💛2.تا ب حال پیاده مسافت طولانی طی کردی ؟', '💛3.صداهای بلند اذیتت میکنه؟', '💛4.عصابنی ک میشی چیزی میشکنی؟', '💛5.تحملت چقدر؟', '💛6.از چیه آسمون خوشت میاد روز یا شب؟', '💛7.تا ب حال سر خروس یا گوسفند خودت بریدی؟', '💛8بنظرت زیاد عمر کنی چق عمر میکی؟', '💛9.تا ب حال رفتی کربلا؟', '💛10.بنظرت انق شجاع هسی از حق مظلوم دفاع کنی؟', '💛11.شعر مورد علاقت؟', '💛12.از مرگ میترسی؟', '💛13.مراقب کی هسی خیلی؟', '💛14.کی خیلی مراقبته؟', '💛15.تا ب حال بر چیزی افسوس خوردی؟', '💛16.وطنت رو دوس داری یا میخای از وطنت بری؟', '💛17.هر حرفی روت تاثیر میزاره؟', '💛18.بهترین دوستت ک همیشه هواست بش هس اونم هواسش بت هس؟', '💛19.چراقای چشمک زن اذیتت میکنه؟', '💛20.ت محل زندگیت امکانات زیاده یا کم؟', '💛21.چ نوع درختی دوس داری؟', '💛22.تا ب حال ب کسی آسیب رسوندی؟', '💛23.تا ب حال کسی بت آسیب رسونده؟', '💛24 نهنگ آبی پاندا فیل گرگ گربه کودوم دوس داری؟', '💛25.بدنت کجاش خیلی درد میکنه ؟', '💛26.تفریحت بر اثاث چ تایمایه؟', '💛27.تا ب حال زیر خاکی پیدا کردی؟', '💛28.بنظرت گند ترین آدم گروه؟', '💛29.احساستی هسی یا خیلی سرد بی روح؟', '💛30.اناناس یا موز ؟', '💛31.روشن فکر هسی؟', '💛32.سرمایه خاصی داری ک بتونی ی زندگی نرمال راه بندازی؟', '💛33.اگ مهریه بندازی چقدر میندازی؟', '💛34.ب شیطان درونت ۱۰ از چند میدی؟', '💛35.زمین یا ملک خاصی داری؟', '💛36.بی وفا ترین کسی ک میشناسی؟', '💛37.بگو گوه ت دهنم؟', '💛38.بنظرت آخر عاقبتت چ شکلی؟', '💛39.با کی زیاد مسافرت میری؟', '💛40.اگ گوشت تا ۱ کیلومتر اون ور تر میشنید چیکا میکردی؟', '💛41.هدفت واس زندگیت؟', '💛42.بی توجهی ب اتفاقات دورت؟', '💛43.قدیمی ترین رفیقت؟', '💛44.از چ ابزاری خوب استفاده میکنی؟', '💛45.روستاتون کجای؟', '💛46.کوتاه ترین آدمی ک مشناسی؟', '💛47.ویس بگی نوحه بخون ن هم نداریم؟', '💛48.رنگ آبی تورو یاد چی میندازه؟', '💛49.حاشیه های ک ت زندگیت هس؟', '💛50.از اندامت خودت خوشت میا؟', '💛51 .روش خاصی برای پول دار شدن مشناسی؟', '💛52.میری دریا کنار ساحل میمونی یا نیری شنا؟', '💛53.از ارتفاع میترسی؟', '💛54.خز ترین آدمی ک میشناسی؟', '💛55.با خرس رو در رو بش چیکا میکنی؟', '💛56.شهری ک گرم باشه یا سرد باشه کووم دوس داری ؟', '💛57.تا ب حال خارج رفتی؟', '💛58.از کلاغ خوشت میاد چرا؟', '💛59.دارو های ک مصرف میکنی؟', '💛60.زیر چشی ب کی نگا میکنی؟', '💛61.ماهی دوس داری؟', '💛62.سریعی یا قوی؟', '💛63.از کی تاب حال سر کاری ک نکردی معذرت خاهی کردی؟', '💛64.خوشگلی؟', '💛65.یازده بار بگو عاشقتم ؟😹', '💛66.دلتو کسی شکسه؟', '💛67.از چ چیزای ک دورت خوشت میاو؟', '💛68.تا ب حال ت خاب شده بری دسشوی\xa0 بد پاشی ببینی تو شلوارت ..؟', '💛69.ارومی یا خیلی بی قراری؟', '💛70.حسرت کی میخوری؟', '💛71.از صدات یاصدای من خوشت میا؟', '💛72.تا ب حال تو جمع ضایع شدی؟', '💛73.تا ب حال سگ گازت گرفته؟', '💛74.خصلت رفتار بد من یا خودت؟', '💛75.با کی برای همیشه خدافظی کردی؟', '💛76.چند تا زبان بلدی?', '💛77.تا ب حال کار خوب کردی چی بودا.؟', '💛78.تا ب حال بجه فامیل زدی؟', '💛79.در برابر ظلم سکوت میکنی؟', '💛80.بنظرت جنگنده خوبی هسی؟', '💛81.اسب سواری یا شنا بلدی؟', '💛82.خیلی مسخره میکنی یا مسخره میشی؟', '💛83.اگ الماس پیدا کنی چیکا میکنی؟', '💛84.کودوم سیاره دوس داری؟', '💛85.تا ب حال گم شدی چن ساعت؟', '💛86.ی تیکه بنداز؟', '💛87.شام چی خوردی دیشب یا همین الان؟', '💛88.زندگی سختی داری؟', '💛89.کسی ک دوسش داری؟', '💛90.کسی ک دوست داره؟', '💛91.دیروز چیکارا کردی صفر تا صدش بگو', '🤍\u200c\u200c1.دوسم داری ؟', '🤍2.اگر روزی بخای ازدواج کن با کی؟', '🤍3. یک حسی بهت دارم ؟', '🤍4.چه ماشین دوست داری؟', '🤍5.بازیگر زن ایرانی یا خارجی؟', '🤍6.یکی از دوست نام ببر؟', '🤍7.رل یا خانواده،', '🤍8.از کی ترس داری؟', '🤍9.الان خونه تنهای ؟', '🤍10.الان ساعت چنده؟', '🤍11.خانواده یا دوست دخترت؟', '🤍12.اگر یکی بهت بگه روت کراش چکار میکنی؟', '🤍13.چهارتا فیلم ایران که با (خ)شروع بشه ؟', '🤍14.دختر یا پسر؟', '🤍15.دوست داری با کی بری بیرون؟', '🤍16.اسم مادرت؟', '🤍17.اسم اون که دوسش داری بگو؟', '🤍18.ازچی ترس داری؟', '🤍19.عاشق شدی؟', '🤍20.اگر روزی برای تو باشم؟', '🤍21. اگر فوتبالیست بزرگ بشی با کسی کمک میکنی؟', '🤍22.اصل بده؟', '🤍23.ازیک تا هزار به من چند میدی؟', '🤍24.چقد از دوست نفرت داری؟', '🤍25.اسم اون که بدت بیاد بگو ؟', '🤍26.اگر یکی بیاد زورت کنه چکار میکنی؟', '🤍27.اگر آمریکا با ایران حمله کن میری؟', '🤍28.دوست داری دخترا برن سربازی؟', '🤍29.اگر بهت بگم دوست دارم چکار میکنی؟', '🤍30.از سورنا خوشت میاد یا نیکا؟', '🤍31.ماکارانی یا قرمه سبزی ؟', '🤍32.چقد من میشناسی؟', '🤍33.به نظرت آدم بدی ام؟', '🤍34.دوست داری طوطی\u200c خونه من ببینی؟', '🤍35.دایی یا عمو؟', '🤍36.ویس بده بگو سلام', '🤍37.اسکرین از صفحه روبیکات بده ؟', '🤍38.دوست داری کیو بغل کنی؟', '🤍39.هفتا عکس از خودت برام بفرست؟', '🤍40.استکر که استفاده میکنی چیه؟', '🤍41.تاحال اسکلت کردن؟', '🤍42.هایده یاگوگوش؟', '🤍43.استقلال پرسپولیسی؟', '🤍44.من چقد دوست داری؟', '🤍45.چه ماهی به دنیا اومدی؟', '🤍46.اگر خیانت کنم به تو چکارم میکنی؟', '🤍47.دلت میخاد منو بزنی؟', '🤍48.شبا تا ساعت چند بیداری؟', '🤍49.از گپ رازی هستی؟', '🤍50.دلت میاد از گپ من لف بدی؟', '🤍51.الان ویس بده بگو چقد دوسش داری؟', '🤍52.شمارتو برای ۲۰نفر بفرست بگو زنگ بزن؟', '🤍53.از چی خوشت میاد؟', '🤍54.روی کی کراشی؟', '🤍55.تاحال گریه کردی؟', '🤍56.مهراب صداش خوبه یا تتلو؟', '🤍57.حصت نصبت به من؟', '🤍58.یک اهنگ شاد که دوسش داری چیه؟', '🤍59.کیو دوست داری روت نمیشه بهش بگی؟', '🤍60.دلت پیش کسی گیر کرده؟', '🤍61.دوست داری بری سربازی؟', '🤍62دعوا کردی؟', '🤍63.چند نفر زدی؟', '🤍64.تاحال احساس کردی یک روت کراشه؟', '🤍65.خوشگل ترین پسر یا دختر گپ کیه؟', '🤍66.اسم پسر باحرف(م)بگین؟', '🤍67.اسم دختر با حرف(ب)بگین؟', '🤍68.دوست داری چند تا بچه داشت باشی؟', '🤍69.اگه روزی خانوادت با عشقت به دزدن کدوم اول نجات میدی؟', '🤍70.چقد آرایش میکنی؟', '🤍71.شمارت رو بفرست گپ؟', '🤍72.عروسی ننت رقصیدی؟', '🤍73.دلت چی میخاد؟', '🤍74.کدوم کشور دلت میخاد بری؟', '🤍75.داخل اینستا کسی فالو کردی شات بده؟', '🤍76.زن داداش داری اسمش چیه؟', '🤍77.چند بار سوتی دادی؟', '🤍78.قلقلکی هستی؟', '🤍79.تاحال با رل دوستت پیش نهاد دادی؟', '🤍80.مدرسه یا گوشی؟', '🤍81.از خودت بگو؟', '🤍82.کیو دوس داری؟', '🤍83.میخوای شغل آیندت چی باشه؟', '🤍84.دوس داری مال تو باشم؟', '🤍85.از صفحه گالریت اسکرین بده', '🤍86.تاحالا جلو آینه با خودت حرف زدی؟', '🤍87.دوس داری عشق من باشی؟', '🤍88.تابحال کادو ولنتاین گرفتی؟', '🤍89.من برات مهمم؟', '🤍90.بامامانت راحت تری یا بابات؟', '🤍91.اسم بهترین معلمت؟', '🤍92.اسم بهترین دوستت؟', '🤍93.تابحال پیش کسی گریع کردی؟', '🤍94. در روز\xa0 چن ساعت انلاینی؟', '🤍95.تابحال از مدرسه فرار کردی؟', '🤍96.عشق یا رفیق؟', '🤍97.کدوم درسو بیشتر دوص داری؟', '🤍98.چ نوع تیپ دوص داری؟', '🤍99.چن بار رل زدی؟', '🤍100.تاریخ تولدت', '🤍101.اخلاقم چجوریه', '\u200c\u200c🫐🍎1.افسرده شدی؟', '🫐🍎2.پول یا قلب؟', '🫐🍎3.قدت؟', '🫐🍎4.اگه بهت بگن س تا آرزو کن چه ارزویی میکنی؟', '🫐🍎5.جزو س نفر مهم زندگیت هستم؟', '🫐🍎6.سنت؟', '🫐🍎7.چند کیلویی؟', '🫐🍎8.چی بهت ارامش میده', '🫐🍎9.تاریخ تولدت؟', '🫐🍎10.اخلاقم چجوریه؟', '🫐🍎12.رنگ مورد علاقت؟', '🫐🍎13.عشق اولت کیه؟', '🫐🍎14.دلت برا کی تنگه؟', '🫐🍎15. اهنگ مورد علاقت؟', '🫐🍎16.زشتی یا خوشگل؟', '🫐🍎17.غذای مورد علاقت؟', '🫐🍎18.شکست عشقی خوردی؟', '🫐🍎19.بنظرت من چجور ادمیم؟', '🫐🍎20.حیوان مورد علاقت؟', '🫐🍎21.از چی من خوشت میاد؟', '🫐🍎22.عدد مورد علاقت؟', '🫐🍎23.مغرور یا جذاب؟', '🫐🍎24.چن سالته؟', '🫐🍎25.اسم من؟', '🫐🍎26.کی داخل قلبت هس؟', '🫐🍎27.عاشق شدی؟', '🫐🍎28.اسم عشقت؟', '🫐🍎29.اگه بهت ¹⁰میلیون بدن چیکارمیکنی؟', '🫐🍎30.چه حسی بهم داری', '🫐🍎31.چشات چ رنگیه؟', '🫐🍎32.دوس داری من چی توباشم؟', '🫐🍎33.بزرگترین ارزوت؟', '🫐🍎34.ازچی من بدت میاد؟', '🫐🍎35.الان حالت چطوریه؟', '🫐🍎36.دوستم داری؟', '🫐🍎37.اگه بمیرم آخرین حرفت چیه ؟', '🫐🍎38.بنظرت خوشگلم یا زشت؟', '🫐🍎39.منو تا حالا دیدی؟', '🫐🍎40.اگه بهت بگم عاشقتم چیکار میکنی؟', '🫐🍎41.دوس داری مال توباشم؟', '🫐🍎42.اسممو داخل گوشیت چی نوشتی؟', '🫐🍎43.از چی میترسی؟', '🫐🍎44.دوس داری باهات بحرفم؟', '🫐🍎45.اگه بهت بگم رل من باش قبول میکنی؟', '🫐🍎47.الان دوس داری چ غذایی بخوری؟', '🫐🍎48.رلی یا سینگلی؟', '🫐🍎49.دوس داری ضربان قلبم\xa0 بشی؟', '🫐🍎50.کیو دوس داری؟', '🫐🍎51.میخوای شغل آیندت چی باشه🥳', '🫐🍎52.خجالت آور ترین کاری ک کردی چیه؟🥳', '🫐🍎53.تاحالا کار کردی جایی؟🥳', '🫐🍎53.دوس داری مال تو باشم؟🥳', '🫐🍎54.از صفحه گالریت اسکرین بده🥳', '🫐🍎55.تاحالا جلو آینه با خودت حرف زدی؟🥳', '🫐🍎56.دوس داری عشق من باشی؟🥳', '🫐🍎57.تابحال کادو ولنتاین گرفتی؟🥳', '🫐🍎58.من برات مهمم؟🥳', '🫐🍎59.سیگار میکشی؟🥳', '🫐🍎60.بامامانت راحت تری یا بابات؟🥳', '🫐🍎61.اسم بهترین معلمت؟🥳', '🫐🍎62.اسم بهترین دوستت؟ 🥳', '🫐🍎63.وقتی عصبی میشی چجوری آروم میشی\u200c؟🥳', '🫐🍎64.تابحال پیش کسی گریع کردی؟🥺', '🫐🍎65.در روز\xa0 چن ساعت انی؟🥳', '🫐🍎66.تابحال از مدرسه فرار کردی؟🥳', '🫐🍎67.عشق یا رفیق؟🥳', '🫐🍎68.کدوم درسو بیشتر دوس داری؟🥳', '🫐🍎69.چه نوع تیپ دوص داری؟🥳', '🫐🍎71.حس ت به من هرچی هس بگو؟🥳', '🫐🍎72.دوس داری چن سالگی ازدواج کنی؟🥳', '🫐🍎73.حیوون مورد علاقت؟🥳', '🫐🍎74.از چی بیشتر میترسی؟🥳', '🫐🍎75.در اعضای ده میلیون حاضری موهاتو بزنی؟🥳', '🫐🍎76.چن\xa0 تا خواهر برادر داری؟🥳', '🫐🍎77.اسم کراشتو بگو؟🥳', '🫐🍎78.گوشیت مدلش چیع؟🥳', '🫐🍎79.رقص بلدی؟🥳', '🫐🍎80کسی دلتو شکونده؟🥳', '\u200c\u200c😍🌚1.تو گپ رو کی کراشی و نمیتونی بگی؟', '😍🌝2.کی بیشتر رو مخته؟', '😍🌚3.کدوم اخلاقم گنده؟', '😍🌝4.کدوم اخلاقمو دوس داری؟', '😍🌓5.غذای مورد علاقت؟(فست\u200cفود_خانگی)', '😍🌝6.کنار دریا یا جنگل؟', '😍🌚7.شب یا روز؟', '😍🌝8.بارون یا برف؟', '😍🌚9.دوس داری پیش مرگ کسی بشی؟کی؟', '😍🌝10ـاگه کفنت جیب داشته باشه،باخودت چی میبری؟', '😍🌚11.رنگای تیره یا روشن؟', '😍🌝12.تیپ لش_اسپرت_مجلسی_ساده کدومش؟', '😍🌚13.موی بلند دخترونه یا کوتاه؟', '😍🌝14.حاظری بخاطرم کاری انجام بدی؟', '😍🌚15.عکس ببینم', '😍🌝16.آرایش معمولی یا غلیظ؟', '😍🌚17.حرفی ک تودلته و روت نمیشه بگی؟', '😍🌝18.دوس داری تو حال خرابیت کی کنارت باشه؟', '😍🌚19.چای یا قهوه؟', '😍🌝20.شبا اولین چیزی ک بهش فکر میکنی چیه؟', '😍🌚21. میوه های تابستونی یا زمستونی؟', '😍🌝22.چی دوس داری کادو بگیری؟', '😍🌚23.وقتی عصبی میشی اولین کاری ک میکنی چیه؟', '😍🌓24.طلا یا بدلیجات؟', '😍🌚25.رل داری؟', '😍🌝26.با چه حرفایی زود قول میخوری؟', '😍🌚27.چی باعث میشه قید یکیو بزنی؟', '😍🌝28.جلو آینه چیکارا میکنی؟', '😍🌚29.سوال اخر', '😍🌝30.استخر یا دریا؟', '😍🌚31.سگ یا گرگ؟', '😍🌝32.ب کی خیلی حسودیت میشه؟', '😍🌚33.بنظرت غرور من چقدره؟', '😍🌝34.حجاب یا بد حجاب یا متوسط؟', '😍🌚35.اخرین باری ک گریه کردی؟', '😍🌝36.فاز دپ یا شیطنت؟', '😍🌚37.خوشگلی مهمه یا اخلاق؟', '😍🌝38.پولش یا قیافش؟', '😍🌚39.پوچ', '😍🌝40.اگ بتونی ذهن یکیو بخونی اون کیه؟', '😍🌚41.با مامانت راحتی یا بابات؟', '😍🌝42.چنتا بچه\u200cاین؟', '😍🌚43.اخلاقای بدت چیه؟', '😍🌝44.اخلاقای خوبت چیه؟', '😍🌚45.پوچ', '😍🌓46.سیگار یا قلیون؟', '😍🌚47.بد ترین سوتیت چی بوده؟', '😍🌝48.اهنگ قفلیت؟', '😍🌚49.چ رقصی بلدی؟', '😍🌝50.پارتی یا جداگونه؟', '😍🌚51.با خودت تو خلوت\u200cهات حرف میزنی؟', '😍🌝52.شنا بلدی؟', '😍🌚53.اگ بگم ازت خوشم میاد چی میگی؟', '😍🌝54.از 1 تا 10 چ نمره\u200cای بهم میدی؟', '😍🌚55.بود و نبودم مهمه؟چرا؟', '😍🌝56.گریه هات پنهونیه یا راحتی جلو هرکسی میتونی گریه کنی؟', '😍🌚57.سوال ۲۰', '😍🌝58.خونه زندگی مجلل یا ساده؟', '😍🌚59.همسر زرنگ یا خنگ؟', '😍🌝60.بهترین اتفاق زندگیت؟', '😍🌓61.بدترین اتفاق زندگیت؟', '😍🌚62.شات از نتایج گوگلت', '😍🌝63.شات از لیست پی وی\u200cهات', '😍🌚64.شات از گالریت', '😍🌝65.برو یکیو ایسگا کن بگو عاشقتم', '😍🌚66.قد و وزنت؟', '😍🌝67.از چی میترسی؟', '😍🌚68.نوشابه یا دوغ؟', '😍🌝69.پوچ', '😍🌚70.دوس داشتی جای کی باشی؟', '😍🌓71.حس میکنی کی دوستت داره و نمیتونه بت بگه؟', '😍🌚72.صب ک بیدار میشی.،اولین برنامه\u200cای ک تو گوشیت میری سر\u200cوقتش کدوم برنامس؟', '😍🌝73.اسم خاص دخترونه/پسرونه', '😍🌚74.با من میرقصی؟', '😍🌝75.پوچ', '😍🌚76.عاشق شدی؟', '😍🌝77.خیانت کردی یا دیدی؟', '😍🌚78.ب خارج فک کردی؟', '😍🌝79.شب گردی یا روز', '😍🌚80.تنهایی قدم زدنو دوس داری یا با رل؟', '😍🌚82.خرید لباس یا خوراکی؟', '😍🌝83.ترش/شیرین/ملس/شور کدومش؟', '😍🌚84.از فامیلات کی بیشتر ب فکرته و همش حواسش بهت هست؟', '😍🌝85.از گذشتت متنفری یا ن؟', '😍🌚86.ناهار یا شام؟', '😍🌝87.سفرهای داخل کشور یا خارج؟', '😍🌚88.کشور مورد علاقت؟', '😍🌝89.دختر لوس و شیطون یا خشن؟', '😍🌚90.اگ تولدم دعوتت کنم چی میخری؟', '😍🌝91.ویس بده با اسمم بگو دوستت دارم', '😍🌚92.بنظرت جذاب ترین دختر/پسر گپ کیه؟', '😍🌝93.با همه درددل میکنی یا تو دلت نگه میداری؟', '😍🌚94.دور دور با رفیقات یا عشقت؟', '😍🌓95.بیشتر کافه میری یا رستوران؟', '😍🌚96.زیراب کسیو زدی تاحالا؟کیو؟', '😍🌝97.تاریخ تولدت؟', '😍🌚98.دوس داری چن سالگی بمیری؟', '😍🌝99.ارزوت؟', '😍🌚100.شانست چجوریه؟', '😍🌝101.با خانواده پدری راحت تری یا مادری؟', '😍🌚102.اهنگ یا سکوت؟', '💕1. بزرگ ترین رازی که داریـ', '💕2. چنـدتا رل داشتیـ', '💕3.اسکرین شات از نشان شده های روبینواتـ', '💕4.خواننده مورد علاقه اتـ', '💕5.متولد ده چندیـ', '💕6.تاحالا چندتا درس تجدید شدیـ', '💕7.تاحالا فکر به خود کشی کردیـ', '💕8.به دوستت زنگ بزن بگو ازت بدم میاد صداشو ظبط کن بفرسـ', '💕9.از چی دخترا خوشت میاد', '💕10.از چی پسرا خوشت میاد', '💕11.میای بریم بیرونـ', '💕12.دوس داری باهم بریم شهر بازیـ', '💕13.اگه تو یه جزیره حبس باشی ، دوس داری کدوم از اعضای گروه همراه ات باشه ؟ ( اگه پسری دختر و اگه دختری پسر )', '💕14.صبح بلند شی بببینی جنسیتت عوض شده چیکار میکنی ؟', '💕15.اسم مامان بابات ؟', '💕16.برای اینکه نظر دختر / پسر رو به خودت جلب کنی چه کاری انجام میدی ؟', '💕17.از 1 تا 10 بهم چند میدی ؟', '💕18.وقتی برای اولین بار منو ببینی چه جوری میشی؟', '💕19.قلیون کشیدی ؟', '💕20.استیکر مورد علاقه اتـ', '💕21. ترجیح میدی جاهای خلوت باشی یا شلوغ', '💕22.فیلم مورد علاقت؟', '💕23.دوس داری پسر بودی یا دختر باشی؟', '💕24.اگه ده میلیون بهت بدن همین الان بلاکم میکنی؟؟', '💕25.از چیع من بدت میاد؟', '💕26.از شب خوشت میاد یا روز؟', '💕27.بهترین خاطره زندگیت چیه؟', '💕28.بدترین خاطره زندگیت چیه؟', '💕29.تا حالا عاشق شدی؟', '💕30.اهل کجایی؟', '💕31.خوبی مامانم؟', '💕32.تا به حال عاشق شدی؟', '💕33.چه رفتاری برای تو بیشتر از همه جذاب است؟', '💕34.تا به حال به پارتنرت دروغ گفتی؟ چه دروغی؟', '💕35.معیارهاتو از فرد رویاهات بگو', '💕36.هیجان\u200c انگیزترین چیز برای تو چیه؟', '💕37.با کدوم دوستت می\u200cخوای به یک دانشگاه بری؟', '💕38.آخرین باری که خودتو خیس کردی کی بوده؟', '💕39.آخرین کار غیرقانونی که انجام دادی چی بوده؟', '💕40.اگر هرچیزی که می\u200cخواستی رو می\u200cتونستی بخری، چی می\u200cخریدی؟', '💕41.اسم کسی که توی این جمع خیلی خیلی دوسش داری چیه ؟', '💕42.زیباترین خاطرت با کیه ؟', '💕43.پنج خصوصیت ویژه ای که رابطه تو باید داشته باشه رو نام ببر؟', '💕44.به شریکت بگو که چه ویژگی هایی رو در اون دوست داری', '💕45.سخترین و تلخ ترین لحظات زندگیت با عشقت و بازگو کن .', '💕46.در چه مورد دوست نداری کسی با عشقت شوخی کنه ؟', '💕47.اولین برداشت تو از عشقت چه بوده؟', '💕48.اهنگ مورد علاقت؟', '💕49.بهترین مسافرتت؟', '💕50.بهترین منطقه شهرت؟', '💕51.شوهر مورد علاقت؟', '💕52.زن مورد علاقت؟', '💕53.شغل بابات؟', '💕54.شغل مامانت؟', '💕55.خوبی؟', '💕56.تاریخ تولدت؟', '💕57.مادرتو بیشتر دوس داری یا پدرتو؟', '💕58.تصورت از عشق؟', '💕59.بازیگر مورد علاقت؟', '💕60.اسکرین از یکی از کلاس های شبکه شادت', '💕61.مثلا با من رل میزنی؟', '💕62.بهترین سیاره در نظرت؟', '💕63.هند یا سوریه؟', '💕64.یه فیلم کوتاه از خودت بفرس', '💕65.پول یا سلامتی یا عشق؟', '💕66.توی آشناهات رو کی بیشتر کراشی؟', '💕67.رنگ مورد علاقت؟', '💕68.ماشین مورد علاقت؟', '💕69.میای بیرون باهام؟', '💕70.قد و وزنت؟', '💕71.غذایی که نمیتونی بخوری چیع؟', '💕72.ی ویس بده', '💕73.بزرگترین ترست چیع؟', '💕74.تیکه کلامت؟', '💕74 . آخرین چیزی ک تو گوگل سرچ کردی چیه', '💕76.یه حرفی تو پی وی بهم بزن ک بین خودمون بمونه.', '💕77.دوس داری الان بغلم باشی؟', '💕78.پول باباتو خرج میکنی یا خودت درامد داری؟', '💕79.ی دروغ بهم بگو.', '💕80.شات از نتایج گوگلت', '💕81.چشای کیو تو گپ میبوسی و لبای کیو؟(دونفرمتفاوت)', '💕82.رو کسی کراش داری؟', '💕83.کدومش بدتره؟(موجودی شما کافی نمیباشد)_(اینترنت شما به اتمام رسید)', '💕84\u200c.شات از لیست پیوی هات', '💕85.شات از پیوی کسی ک زیاد باهاش میچتی و تو این گپه.', '💕86.روز شانست کدومه؟', '💕87.میوه مورد علاقت؟', '💕88.چیو ب ماها دروغ گفتی؟', '💕89.تا حالا شده بخاطر یکی از بچه های این گپ گریه کنی؟یا ناراحت شی بخاطرش؟', '💕90.زیرلباست چ رنگیه؟'],
    "group": {},
    "robot": True,
    "rip_chat": True,
    "silent": False,
    "fohsh":['کص',"کیر","جنده","کون","اوب","حرامزاده","حرومزاده"],
    "tabligh":["بیو","تبلیغ","بیوگرافی"]
})
save["silent"]=False
lock = threading.Lock()
save.setdefault("message",0)
def decrease_sharzh():
    while True:
        try:
            with lock:
                for group_guid in list(save["group"].keys()):
                    if save["group"][group_guid]["sharzh"] > 0:
                        save["group"][group_guid]["sharzh"] -= 1
                        if save["group"][group_guid]["sharzh"] <= 0:
                            bot.send_text(group_guid,"""⚠️ شارژ گروه به پایان رسید! ⚠️

💡 برای فعال‌سازی مجدد، لطفاً به آیدی زیر پیام دهید:
@Mahziaar_YT
درصورت موافقت سازنده اشتراک شما فعال خواهد شد
چنل ما😍 @www_free_ir""")
                            bot.leave_chat(group_guid)
                            save_data(file_name, save)
            sleep(86400)  # هر ۲۴ ساعت
        except Exception as e:
            print(f"⚠️ خطا در کاهش شارژ گروه‌ها: {str(e)}")

def send_kol(user_guid,ms,text):
    if save.get("group"):
        z = 0
        zi = 0
        for i in save["group"].keys():
            try:
                bot.send_text(i, text)
                sleep(5)
                zi += 1
            except:
                z += 1
        text = f"تعداد ارسالی: {zi}\nتعداد ارسال نشده: {z}"
        send_message(text=text, user_guid=user_guid,ms=ms)  # ارسال نتیجه به کاربر#
    else:
        send_message(text="هیچ گروهی یافت نشد.", user_guid=user_guid,ms=ms)

# تابع را با `user_guid` اجرا کن
def start_send_kol(user_guid,ms,text):
    threading.Thread(target=send_kol, args=(user_guid,ms,text,), daemon=True).start()
    
    
# اجرای تابع در یک ترد پس‌زمینه
threading.Thread(target=decrease_sharzh, daemon=True).start()


defulte={
        "rb": True,
        "talk_gofl":False,
        "silent_bot": False,
        "link": "",
        "bio_group":"",
        "emtyaz":True,
        "all_member":"",
        "sharzh":0,
        "name": "",
        "manager": "",
        "zd_number":False,
        "zd_hashtack":False,
        "zd_link": True,
        "zd_forward": True,
        "zd_id": True,
        "zd_image": False,
        "zd_gif": False,
        "zd_file": False,
        "zd_voice": False,
        "zd_music": False,
        "zed_spam": False,
        "zed_poll":False,
        "zed_post":False,
        "zed_live":False,
        "zed_story":False,
        "Prevention_link":False,
        "spanser_TB": False,
        "funny": True,
        "AI": True,
        "tools": True,
        "talk": True,
        "warning":True,
        "talk_Politeness": True,
        "very_talk": False,
        "welcome": True,
        "goodbye": True,
        "law": True,
        "help": True,
        "ban_member": True,
        "swear_word": False,
        "filter_text": False,
        "rel":"",
        "font":"معمولی",
        "list_welcome_text": [],
        "list_warning_text":"",
        "add":0,
        "left":0,
        "all_message":0,
        "delete_message":0,
        "new_member":0,
        "left_member":0,
        "list_goodbye_text": [],
        "list_law_text":"",
        "list_emtyaz":{},
        "mes_robot":0,
        "list_spanser_channel": [],
        "list_kill": [],
        "list_admin": [],
        "list_special": [],
        "list_no_anser": [],
        "list_silent":[],
        "list_exempt": [],
        "list_note": [],
        "list_filter_text": [],
        "list_warning":{},
        "asls":{},
        "title":{},
        "number_message":{},
        "number_warning":{
        	"link":3,
        	"forward":3,
        	"id":3,
        	"image":3,
        	"gif":3,
        	"file":3,
        	"voice":3,
        	"music":3,
        	"filter":3
        	}
}

my_guid=bot.get_me()["user"]["user_guid"]
message_send=False
message_send_event = threading.Event()
gh=0
bot_off=True

import re
import pickle
import threading

save_counter = 0
file_talk = "data.pkl"
talk_lock = threading.Lock()  # برای اطمینان از thread-safety

def is_valid_message(text):
    text = text.strip()
    if len(text) < 5 or len(text) > 300:
        return False
    if re.fullmatch(r'[\d\s\W]+', text):
        return False
    if re.search(r'https?://|www\.|\.com|\.ir|\.net|rubika\.ir|@\w+', text, re.IGNORECASE):
        return False#
    spam_keywords = ['عضو شو', 'فالو کن', 'کانال ما', 'لینک گروه', 'کسب درآمد', 'رای بده']
    if any(word in text.lower() for word in spam_keywords):
        return False
    if re.search(r'(.)\1{4,}', text):
        return False
    if re.fullmatch(r'[a-zA-Z0-9\s.,!?@#]+', text):  # فینگلیش
        return False
    if re.fullmatch(r'[^\w\s]+', text):  # فقط ایموجی یا علامت
        return False
    return True

def save_talk(talk):
    with open(file_talk, 'wb') as f:
        pickle.dump(talk, f)
    print(">>> Talk data saved to", file_talk)

def talk_new(talk, reply_text, text):
    global save_counter

    if not is_valid_message(text):
        return

    with talk_lock:
        if reply_text in talk:
            talk[reply_text].append(text)
        else:
            talk[reply_text] = [text]

        save_counter += 1
        if save_counter >= 100:
            threading.Thread(target=save_talk, args=(talk.copy(),)).start()
            save_counter = 0

# اجرای talk_new به صورت thread
def run_talk_new_threaded(talk, reply_text, text):
    threading.Thread(target=talk_new, args=(talk, reply_text, text)).start()
        
message_count = 0
@bot.on_message()
def start(ms: Message):
    global message_count, first_message_time ,talk,send_message, gh,bot_off,message_times
    message_send_event.clear()
    if ms.is_group:
	    group_guid = ms.object_guid
	    if group_guid in save["group"] and save["robot"] and save["group"][group_guid]["sharzh"]>=0:
	            save["group"][group_guid].setdefault("zd_number", False)
	            save["group"][group_guid].setdefault("zd_hashtack", False)
	            group_data = save["group"][group_guid]
	            text = ms.text.strip() if ms.text else None
	            mid = ms.message_id
	            user_guid = ms.author_guid if ms.author_guid else "Unknown"
	            utype = user_type(user_guid, group_data, ms)
	            mtype = message_type(ms.message_type, user_guid, group_data, ms, utype)
	            gh+=1
	            if gh>=100:
	                  save_data(file_name, save)
	                  gh=0
	            if text=="ربات روشن" and utype in [0,1,2,3]:
	            	group_data["rb"]=True
	            	send_message("روشن شدم عشقمᯤ",group_data,ms)
	            elif text=="ربات خاموش" and utype in [0,1,2,3]:
	            	group_data["rb"]=False
	            	send_message("خاموش شدم",group_data,ms)
	            if save["group"][group_guid]["rb"]:

    # 🎛 فعال‌سازی دستورات سخنگو توسط سازنده یا ادمین
                    if text == "سخنگو فعال":
        speak_data["enabled"].setdefault(group_guid, {"polite": False, "rude": False, "smart": False})
        speak_data["enabled"][group_guid]["polite"] = True
        save_speak()
        send_message("✅ سخنگوی مودب فعال شد", group_data, ms)

                    elif text == "سخنگو بی ادب فعال" and user_guid in save["maker_asl"]:
        speak_data["enabled"].setdefault(group_guid, {"polite": False, "rude": False, "smart": False})
        speak_data["enabled"][group_guid]["rude"] = True
        save_speak()
        send_message("⚠️ سخنگوی بی‌ادب فعال شد", group_data, ms)

                    elif text == "سخنگو هوشمند فعال" and user_guid in save["maker_asl"]:
        speak_data["enabled"].setdefault(group_guid, {"polite": False, "rude": False, "smart": False})
        speak_data["enabled"][group_guid]["smart"] = True
        save_speak()
        send_message("🤖 سخنگوی هوشمند فعال شد", group_data, ms)

                    elif text.startswith("یادبگیر") and user_guid in save["maker_asl"]:
        try:
            cmd = text.replace("یادبگیر", "").strip()
            key, value = cmd.split(")")
            key = key.replace("(", "").strip()
            value = value.replace("(", "").strip()
            speak_data["smart"].setdefault(key, []).append(value)
            save_speak()
            send_message("یاد گرفتم 🧠", group_data, ms)
        except:
            send_message("فرمت درست: یادبگیر (کلمه) (پاسخ)", group_data, ms)

		            try:
		             
			            if hasattr(ms, "reply_info") and ms.reply_info:
			            	try:
			            		rmid = getattr(ms, "reply_message_id", None)
			            		rmguid = getattr(ms.reply_info, "author_guid", None)
			            		if rmguid:
						            rminfo = vars(ms.reply_info)  
						            rutype = user_type(rmguid, group_data, ms)
						            reply_text=getattr(ms.reply_info,"text",None)
			            		else:
						            rminfo, rmguid, rutype = None, None, None
			            	except Exception as e:
			            		rminfo, rmguid, rutype, rmid = None, None, None, None
			            else:
			            	rminfo, rmguid, rutype, rmid = None, None, None, None
		            except:
		            	rminfo, rmguid, rutype, rmid = None, None, None, None
		            if rmguid!=None and reply_text!=None and rmguid!=my_guid and user_guid!=my_guid:
		            	run_talk_new_threaded(talk, reply_text, text)
		            group_data["all_message"] += 1


            # 🟩 اجرای پاسخ‌های سخنگو در همین تابع
            mode = speak_data["enabled"].get(group_guid, {})
            lower_text = text.lower().strip()

            # خوش‌آمدگویی
            if ms.event_type == "JoinedGroupByLink" and group_data.get("welcome", True):
                bot.send_text(group_guid, f"🌟 به گپ {group_data.get('name','')} خوش اومدی عزیزم 💎✨")

            # خداحافظی
            if ms.event_type == "LeaveGroup" and group_data.get("goodbye", True):
                bot.send_text(group_guid, f"💔 دلم برات تنگ میشه {user_guid}، زود برگرد...")

            # سخنگو مودب
            if mode.get("polite") and lower_text in speak_data["polite"]:
                send_message(random.choice(speak_data["polite"][lower_text]), group_data, ms)

            # سخنگو بی‌ادب
            elif mode.get("rude") and lower_text in speak_data["rude"]:
                send_message(random.choice(speak_data["rude"][lower_text]), group_data, ms)

            # سخنگو هوشمند
            elif mode.get("smart") and lower_text in speak_data["smart"]:
                send_message(random.choice(speak_data["smart"][lower_text]), group_data, ms)

		            group_data["number_message"][user_guid] = group_data["number_message"].get(user_guid, 0) + 1
		            
		            if mtype!=None and utype not in [0,1,2,3,4,5,7, 8]:
		                try:
			                group_data["delete_message"] += 1
			                ms.delete()
			                group_data["delete_message"]
			                if group_data["warning"]:
			             	   warning_send(user_guid, group_data, mtype, ms,group_guid)
		                except:
		                	None
		            elif text=="یک پیام سنجاق شد.":
		            	send_message("یک پیام سنجاق شد",group_data,ms)
		            elif text.startswith("گفتگوی گروهی ایجاد شده است."):
		            	send_message("کال ایجاد شد.",group_data,ms)
		            elif text.startswith("گفتگوی گروهی به پایان رسید."):
		            	send_message("کال قطع شد.",group_data,ms)
		            elif text=="آواتار تغییر کرد.":
		            	send_message("آواتار تغییر کرد.",group_data,ms)
		            elif ms.event_type == "JoinedGroupByLink":
		            	group_data["new_member"]+=1
		            	if group_data["welcome"]==True:
		            		text="+ کاربر عزیز به گپ خوش اومدی عزیزم 😍❤️بمونی برامون"
		            		text=random.choice(group_data["list_welcome_text"]) if group_data["list_welcome_text"] else text
		            		send_message(text,group_data,ms)
		            elif ms.event_type == "LeaveGroup":
		            	group_data["left_member"]+=1
		            	if group_data["goodbye"]==True:
		            		text="- زود برگرد عزیزم 💎✨💘"
		            		text=random.choice(group_data["list_goodbye_text"]) if group_data["list_goodbye_text"] else text
		            		send_message(text,group_data,ms)
		            if user_guid==None:
		            	return 
		            if utype==10:
		            	try:
		            		bot.ban_member(group_guid,user_guid)
		            	except:
		            		None
		            if utype == 8:
		                try:
		                	ms.delete()
		                except:
		                	return 
		            elif utype in [0, 1, 2, 3,4,5]:
		            	with concurrent.futures.ThreadPoolExecutor() as executor:
		            		futures = [
						        executor.submit(group_manager, group_data, text, ms, rmid, rmguid, group_guid, rutype, utype),
						        executor.submit(funny, group_data, text, ms, group_guid, user_guid,rmguid,mid),
						        executor.submit(tools, group_data, text, ms, group_guid, user_guid, rmguid,mid),
						        executor.submit(AI, group_data, text, ms, group_guid, user_guid),
						        executor.submit(help, group_data, text, ms, group_guid, user_guid)
						   ]
		            	concurrent.futures.wait(futures)
						
		            	def check_and_run_talks():
		            		if not  message_send_event.is_set():
		            			talks(text, talk, best_talk, group_data, ms, rmguid, my_guid,user_guid)
		            	check_and_run_talks()
		            elif utype in [6,9]:
		            	with concurrent.futures.ThreadPoolExecutor() as executor:
		            		futures = [
						        executor.submit(funny, group_data, text, ms, group_guid, user_guid,rmguid,mid),
						        executor.submit(tools, group_data, text, ms, group_guid, user_guid, rmguid,mid),
						        executor.submit(AI, group_data, text, ms, group_guid, user_guid),
						        executor.submit(help, group_data, text, ms, group_guid, user_guid)
						    ]
		            	concurrent.futures.wait(futures)
		            	def check_and_run_talks():
		            		if not message_send_event.is_set():
		            			talks(text, talk, best_talk, group_data, ms, rmguid, my_guid,user_guid)
		            	check_and_run_talks()
	            if save["rip_chat"]:
	                now = datetime.now()
	                with lock:
	                    message_times = [t for t in message_times if now - t <= timedelta(seconds=11)]
	                    message_times.append(now)
	                    if len(message_times) >= 5 and not save["silent"]:
	                        save["silent"] = True
	                        threading.Timer(9, reset_silent_mode).start()
    elif ms.is_user:
	    user_guid = ms.author_guid
	    text=ms.text

	    if text and user_guid in save["maker_asl"]:
	        try:
	            if text == "راهنما":
	                help_text ="""**دستورات مدیریت ربات:**

⚡ 1. شارژ همگانی [عدد]  
➖ شارژ کردن تمام گروه‌ها به یک میزان

📊 2. آمار  
➖ نمایش وضعیت کلی ربات (تعداد گروه، وضعیت ربات و...)

📨 3. ارسال همگانی [متن]  
➖ ارسال پیام به همه گروه‌ها

#️⃣ 4. تعداد گروه‌ها  
➖ نمایش تعداد کل گروه‌ها

🔍 5. گروه [گوید]  
➖ نمایش اطلاعات یک گروه خاص

✉️ 6. پیام ربات  
➖ تنظیم پیام پیش‌فرض ربات

💳 7. شارژ [گوید]  
➖ شارژ کردن یک گروه خاص

🗑 8. حذف [گوید]  
➖ حذف یک گروه از دیتابیس

✅ 9. ربات روشن  
➖ روشن کردن عملکرد ربات

⛔ 10. ربات خاموش  
➖ خاموش کردن کامل ربات

🛡 11. ضدریپ [روشن / خاموش]  
➖ فعال/غیرفعال کردن سیستم ضد ریپورت

💥 12. حذف همه گروه‌ها  
➖ پاک کردن همه گروه‌ها از دیتابیس

🔇 13. سخنگو خاموش [گوید]  
➖ غیرفعال کردن حالت سخنگو در یک گروه خاص

💾 14. سیو  
➖ ذخیره تغییرات انجام‌شده"""
	                send_message(help_text, user_guid=user_guid, ms=ms)
	            elif text.startswith("سخنگو خاموش"):
	            	text=text.replace("سخنگو خاموش","").strip()
	            	save["group"][text]=False
	            	send_message("خاموش  شد", user_guid=user_guid, ms=ms)
	            elif text.startswith("سخنگو روشن"):
	            	text=text.replace("سخنگو روشن","").strip()
	            	save["group"][text]=True
	            	send_message("روشن شد", user_guid=user_guid, ms=ms)
	            elif text == "آمار" and user_guid in save["maker_asl"]:
	                if save["group"]:
	                    text = "📋 **لیست گروه‌های فعال:**\n\n"
	                    for guid, data in save["group"].items():
	                        text +=(f"🆔 شناسه: {guid} \n"
	                                 f"⚡ شارژ:{data['sharzh']}\n"
	                                 f"\nسخنگو: {data['talk_gofl']}")
	                    send_message(text, user_guid=user_guid, ms=ms)
	                else:
	                    send_message("⚠️ هیچ گروه فعالی وجود ندارد.", user_guid=user_guid, ms=ms)
	            elif text.startswith("شارژ همگانی"):
	            	try:
	            		t = int(text.replace("شارژ همگانی", "").strip())
	            		if "group" in save and isinstance(save["group"], dict):
	            		     for i in save["group"]:
	            		         if isinstance(save["group"][i], dict):
	            		         	save["group"][i]["sharzh"] = t
	            		     send_message("✅ شارژ همگانی با موفقیت تنظیم شد.", user_guid=user_guid, ms=ms)
	            		else:
				            send_message("⚠️ خطا: داده‌های گروه نامعتبر است.", user_guid=user_guid, ms=ms)
	            	except ValueError:
	            		send_message("⚠️ مقدار وارد شده نامعتبر است. لطفاً یک عدد صحیح وارد کنید.", user_guid=user_guid, ms=ms)
	            elif text.startswith("http") and not save["silent"] and user_guid in save["maker_asl"]:
	                t = text
	                if t:
	                    try:
	                        x = bot.join_chat(t)["group"]
	                        guid = x["group_guid"]
	                        if guid not in save["group"].keys():
	                            save["group"][guid] = copy.deepcopy(defulte)
	                            save["group"][guid].update({
	                                "name": x["group_title"],
	                                "link": t,
	                                "sharzh": 30
	                            })
	                            save["group"][guid]["manager"]=user_guid
	                            send_message("✅ ربات با موفقیت عضو شد. و شما مدیر ربات شدید  \n برای مدیریت گروه لطفا ادمین کنید.", user_guid=user_guid, ms=ms)
	                            text="""🚀 ربات در گروه شما فعال شد! 🚀

✨ برای اطلاعات بیشتر و راهنمایی، کلمه راهنما رو بفرستید!

🎁هدیه شما:30 روز اشتراک↺10هدیه سازنده

💢ربات رو داخل گپ فول ادمین کنید"ربات تمامی قابلیت ها داشته باشه"💢

⭕️استفاده نادرست از ربات باعث لفت از گپ میشود


🔥 گروه شما آماده است! 🌍
° Ch: @www_free_ir
° creator : @Mahziaar_YT
🌐 Dino 🦖™-VERSION ⇋ 3.2.5"""
	                            bot.send_text(object_guid=guid,text=text)
	                    except Exception as e:
	                        send_message(f"❌ خطا در عضویت: {str(e)}", user_guid=user_guid, ms=ms)
	            elif text.startswith("ارسال همگانی") and user_guid in save["maker_asl"]:
	            			text=text.replace("ارسال همگانی","").strip()
	            			start_send_kol(user_guid,ms,text)
	            elif text=="تعداد گروه" and user_guid in save["maker_asl"]:
	            	zi=0
	            	for i in save["group"].keys():
	            		zi+=1
	            	text=f"تعداد : {zi}"
	            	ms.reply(text)
	            elif text.startswith("گروه") and user_guid in save["maker_asl"]:
	            	guid=text.replace("گروه","").strip()
	            	data=save["group"].get(guid,"None")
	            	text += (f"🔹 **نام گروه:** {data['name']}\n"
	            						f"لینک گروه : {data['link']} \n"
	                                 f"🆔 **شناسه:** ||{guid}||\n"
	                                 f"⚡ **شارژ:** {data['sharzh']}\n"
	                                 f"👤 **مدیر:** {data['manager']}\n\n"
	                                 f"تعداد پیام ربات : {save['group'][guid]['mes_robot']}")
	            	send_message(text=text,user_guid=user_guid,ms=ms)
	            elif text.startswith("پیام ربات") and user_guid in save["maker_asl"]:
	            	x=str(save["message"])
	            	send_message(x,group_guid,ms)
	            elif text.startswith("دستور"):
	            	text=text.split()
	            	guid=text[1]
	            	text=text[2]
	            	fake_message_chat=FakeMessage(guid, text, task["ms"])
	            	threading.Thread(target=execute_all_commands, args=(fake_message_chat,)).start()
	            	send_message("✅ اجرا شد.", user_guid=user_guid, ms=ms)
	            elif text.startswith("شارژ") and user_guid in save["maker_asl"]:
	                parts = text.split()
	                if len(parts) == 3:
	                    _, guid, sha = parts
	                    if guid in save["group"]:
	                        try:
	                            save["group"][guid]["sharzh"] = int(sha)
	                            send_message("✅ شارژ با موفقیت تنظیم شد.", user_guid=user_guid, ms=ms)
	                        except ValueError:
	                            send_message("⚠️ مقدار شارژ باید عدد باشد.", user_guid=user_guid, ms=ms)
	                    else:
	                        send_message("⚠️ گروه یافت نشد.", user_guid=user_guid, ms=ms)
	                else:
	                    send_message("⚠️ فرمت صحیح: `شارژ [گروه] [مقدار]`", user_guid=user_guid, ms=ms)
	
	            elif text.startswith("حذف") and user_guid in save["maker_asl"]:
	                t = text.replace("حذف", "").strip()
	                if t and t in save["group"]:
	                    bot.leave_chat(t)
	                    del save["group"][t]
	                    send_message("✅ گروه حذف شد.", user_guid=user_guid, ms=ms)
	                else:
	                    send_message("⚠️ گروه یافت نشد.", user_guid=user_guid, ms=ms)
	
	            elif text.startswith("تغییر سازنده @") and user_guid in save["maker_asl"]:
	                t = text.replace("تغییر سازنده @", "").strip()
	                if t:
	                    try:
	                        x = bot.get_chat_info_by_username(t)["guid"]
	                        save["maker"] = x
	                        send_message("✅ سازنده با موفقیت تغییر یافت.", user_guid=user_guid, ms=ms)
	                    except Exception as e:
	                        send_message(f"❌ خطا در تغییر سازنده: {str(e)}", user_guid=user_guid, ms=ms)
	
	            elif text == "ربات خاموش" and user_guid in save["maker_asl"]:
	                save["robot"] = False
	                send_message("🔴 ربات در همه گروه‌ها خاموش شد.", user_guid=user_guid, ms=ms)
	
	            elif text == "ربات روشن" and user_guid in save["maker_asl"]:
	                save["robot"] = True
	                send_message("🟢 ربات در همه گروه‌ها روشن شد.", user_guid=user_guid, ms=ms)
	
	            elif text == "ضد ریپ خاموش" and user_guid in save["maker_asl"]:
	                save["rip_chat"] = False
	                send_message("⚠️ ضد ریپ غیرفعال شد.", user_guid=user_guid, ms=ms)
	
	            elif text == "ضد ریپ روشن" and user_guid in save["maker_asl"]:
	                save["rip_chat"] = True
	                send_message("✅ ضد ریپ فعال شد.", user_guid=user_guid, ms=ms)
	
	            elif text == "حذف همه گروه ها" and user_guid in save["maker_asl"]:
	                save["group"].clear()
	                send_message("🚨 تمامی گروه‌ها حذف شدند.", user_guid=user_guid, ms=ms)
	
	            elif text == "سیو" and user_guid in save["maker_asl"]:
	                try:
	                    save_data(file_name, save)
	                    send_message("✅ تغییرات ذخیره شد.", user_guid=user_guid, ms=ms)
	                except Exception as e:
	                    send_message(f"❌ خطا در ذخیره‌سازی: {str(e)}", user_guid=user_guid, ms=ms)
	            if save["rip_chat"]:
	                now = datetime.now()
	
	                with lock:
	                    message_times = [t for t in message_times if now - t <= timedelta(seconds=10)]
	                    message_times.append(now)
	                    if len(message_times) >= 6 and not save["silent"]:
	                        save["silent"] = True
	                        threading.Timer(5, reset_silent_mode).start()
	        except Exception as e:
	            send_message(f"❌ خطای غیرمنتظره: {str(e)}", user_guid=user_guid, ms=ms)			



def reset_silent_mode():
    global save
    with lock:
        save["silent"] = False
        message_times.clear() 
        

def group_manager(group_data,text,ms,rmid,rmguid,group_guid,rutype,utype):
	if text == "پین" or text=="سنجاق":
	    if rmid:
	        bot.pin_message(group_guid, rmid)
	        send_message("پیام پین شد.", group_data, ms)
	    else:
	        send_message("خطا: پیام معتبری برای پین کردن یافت نشد.", group_data, ms)
	elif text == "برداشتن پین"  or text =="برداشتن سنجاق":
	    if rmid:
	        bot.unpin_message(group_guid, rmid)
	        send_message("پیام از پین برداشته شد.", group_data, ms)
	    else:
	        send_message("خطا: پیام معتبری برای برداشتن پین یافت نشد.", group_data, ms)
	elif text.startswith("اسم گروه"):
		t = text.replace("اسم گروه", "").strip()
		if t:
		   try:
	        	bot.edit_group_info(group_guid, title=t)
	        	send_message("تنظیم شد",group_data,ms)
		   except:
	        	send_message("تنظیم نشد",group_data,ms)
		else:
			send_message("لطفاً یک نام معتبر وارد کنید.", group_data, ms)

	elif text == "بهینه‌ سازی" and utype in [0,1,2,3]:
	    if group_guid in save["group"]:
	        for key in ["all_message", "delete_message", "new_member", "left_member", "number_message"]:
	            if key in group_data:
	                group_data["all_message"]=0
	                group_data["delet_message"]=0
	                group_data["new_member"]=0
	                group_data["left_member"]=0
	                group_data["number_message"]={}
	                group_data["title"]={}
	                group_data["asls"]={}
	                group_data["list_warning"]={}
	        send_message("✅ بهینه‌سازی انجام شد! اطلاعات اضافی پاک شدند.", group_data, ms)
	        save_data(file_name, save)
	    else:
	        send_message("⚠️ خطا: اطلاعات گروه یافت نشد.", group_data, ms)
	elif text.startswith("نوع فونت "):
	    fonts = {
	        "شلخته": "شلخته",
	        "کشیده": "کشیده",
	        "کشیده ساده": "کشیده ساده",
	        "موجی": "موجی",
	        "تشدید": "تشدید",
	        "معمولی": "معمولی",
	    }
	    
	    font_name = text.replace("نوع فونت ", "").strip()
	    selected_font = fonts.get(font_name)
	
	    if selected_font:
	        group_data["font"] = selected_font
	        send_message(f"✅ فونت به «{selected_font}» تغییر یافت.", group_data, ms)
	    else:
	        available_fonts = "، ".join(fonts.keys())
	        send_message(f"❌ فونت نامعتبر است.\n🔹 فونت‌های موجود: {available_fonts}", group_data, ms)
		

	elif (text == "گروه بسته" or text == "بستن گروه") and utype in [0, 1, 2, 3]:
		try:
			bot.set_group_default_access(group_guid, [])
			send_message("✅ گروه با موفقیت بسته شد. اعضا دیگر نمی‌توانند پیام ارسال کنند.", group_data, ms)
		except:
			send_message("⚠️ متأسفم، نمی‌توانم گروه را ببندم.", group_data, ms)
	
	elif text == "گروه باز" and utype in [0, 1, 2, 3]:
		try:
			bot.set_group_default_access(group_guid, ['SendMessages'])
			send_message("✅ گروه با موفقیت باز شد. اعضا اکنون می‌توانند پیام ارسال کنند.", group_data, ms)
		except:
			send_message("⚠️ متأسفم، نمی‌توانم گروه را باز کنم.", group_data, ms)

	elif text == "بن" and utype in [0, 1, 2, 3, 4, 5]:
		try:
			if rmguid is None:
				send_message("❌ لطفاً روی یک پیام ریپلای کنید.", group_data, ms)
			elif rmguid == my_guid:
				send_message("❌ نمی‌تونم خودم رو بن کنم!", group_data, ms)
			elif rutype in [1, 2, 3, 4, 5]:
				send_message("❌ این کاربر ادمینه، نمی‌تونم بنش کنم.", group_data, ms)
			else:
				bot.ban_member(group_guid, rmguid)
				send_message("✅ کاربر با موفقیت بن شد.", group_data, ms)
		except:
			pass
	
	elif text == "تنظیم پروفایل":
		if not rmid:
			send_message("❌ لطفاً روی یک عکس ریپلای کنید.", group_data, ms)
			return
		try:
			message_data = bot.get_messages_by_id(group_guid, [rmid])["messages"][0]
			if "file_inline" not in message_data:
				send_message("❌ پیام انتخابی عکس نداره.", group_data, ms)
				return
			file_info = message_data["file_inline"]
			if file_info["type"] != "Image":
				send_message("❌ فقط عکس رو می‌پذیرم.", group_data, ms)
				return
			link = bot.get_download_link(group_guid, rmid)
			if not link:
				send_message("❌ نمی‌تونم لینک عکس رو بگیرم.", group_data, ms)
				return
			bot.upload_avatar(group_guid, link)
			send_message("✅ پروفایل تنظیم شد.", group_data, ms)
		except KeyError:
			send_message("❌ عکس معتبر نیست.", group_data, ms)
		except Exception as e:
			send_message("❌ خطایی پیش اومد.", group_data, ms)
			print(f"⚠️ خطا در تنظیم پروفایل: {e}")
	elif text.startswith("بن @"):
		t = text.replace("بن @", "").strip()
		if t:
			user_info = bot.get_chat_info_by_username(t)
			if user_info and "user_guid" in user_info["user"]:
				guid = user_info["user"]["user_guid"]
				bot.ban_member(group_guid, guid)
				send_message(f"✅ @{t} بن شد.", group_data, ms)
			else:
				send_message("❌ نام کاربری نامعتبره.", group_data, ms)
		else:
			send_message("❌ لطفاً یک یوزرنیم وارد کن.", group_data, ms)
	
	elif text == "پاکسازی گروه":
		if utype in [0, 1, 2]:
			thread = threading.Thread(target=clear_group, args=(group_guid, group_data, ms))
			thread.start()
		else:
			send_message("❌ فقط سازنده می‌تونه این کارو انجام بده.", group_data, ms)
	
	elif text.startswith("تنظیم اصل"):
		if rmguid is None:
			send_message("❌ لطفاً روی یک پیام ریپلای کن.", group_data, ms)
		else:
			t = text.replace("تنظیم اصل", "").strip()
			if t:
				group_data.setdefault("asls", {})[rmguid] = t
				send_message(f"✅ اصل تنظیم شد: {t}", group_data, ms)
			else:
				send_message("❌ لطفاً مقدار معتبری برای اصل وارد کن.", group_data, ms)
	
	elif text == "حذف اصل":
		if rmguid is None:
			send_message("❌ لطفاً روی یک پیام ریپلای کن.", group_data, ms)
		else:
			if rmguid in group_data.get("asls", {}):
				del group_data["asls"][rmguid]
				send_message("✅ اصل حذف شد.", group_data, ms)
			else:
				send_message("❌ اصلی تنظیم نشده.", group_data, ms)
	
	elif text.startswith("تنظیم لقب"):
		if rmguid is None:
			send_message("❌ لطفاً روی یک پیام ریپلای کن.", group_data, ms)
		else:
			t = text.replace("تنظیم لقب", "").strip()
			if t:
				group_data.setdefault("title", {})[rmguid] = t
				send_message(f"✅ لقب تنظیم شد: {t}", group_data, ms)
			else:
				send_message("❌ لطفاً مقدار معتبری برای لقب وارد کن.", group_data, ms)
	
	elif text == "حذف لقب":
		if rmguid is None:
			send_message("❌ لطفاً روی یک پیام ریپلای کن.", group_data, ms)
		else:
			if rmguid in group_data.get("title", {}):
				del group_data["title"][rmguid]
				send_message("✅ لقب حذف شد.", group_data, ms)
			else:
				send_message("❌ لقبی تنظیم نشده.", group_data, ms)
	elif text.startswith("عضویت @") and utype in [0, 1, 2, 3]:
		if has_sharzh(group_guid, group_data, ms): return
		username = text.replace("عضویت @", "").strip()
		if username:
			user_info = bot.get_chat_info_by_username(username)
			if user_info and "user_guid" in user_info["user"]:
				guid = user_info["user"]["user_guid"]
				if guid not in group_data.setdefault("list_spanser_channel", []):
					bot.join_chat(guid)
					group_data["list_spanser_channel"].append(guid)
					send_message("✅ عضویت انجام شد.", group_data, ms)
				else:
					send_message("⚠️ این کانال قبلاً ثبت شده.", group_data, ms)
			else:
				send_message("❌ یوزرنیم معتبر نیست.", group_data, ms)
		else:
			send_message("❌ یوزرنیم وارد کن.", group_data, ms)
	
	elif text.startswith("عضویت http") and utype in [0, 1, 2, 3]:
		if has_sharzh(group_guid, group_data, ms): return
		link = text.replace("عضویت", "").strip()
		if link:
			try:
				guid = bot.join_chat(link)["guid"]
				if guid not in group_data.setdefault("list_spanser_channel", []):
					group_data["list_spanser_channel"].append(guid)
					send_message("✅ عضویت انجام شد.", group_data, ms)
				else:
					send_message("⚠️ این کانال قبلاً ثبت شده.", group_data, ms)
			except:
				send_message("❌ لینک معتبر نیست یا خطا رخ داده.", group_data, ms)
		else:
			send_message("❌ لینک وارد کن.", group_data, ms)
	
	elif text.startswith("حذف عضویت @") and utype in [0, 1, 2, 3]:
		username = text.replace("حذف عضویت @", "").strip()
		if username:
			user_info = bot.get_chat_info_by_username(username)
			if user_info and "user_guid" in user_info["user"]:
				guid = user_info["user"]["user_guid"]
				if guid in group_data.get("list_spanser_channel", []):
					group_data["list_spanser_channel"].remove(guid)
					send_message("✅ حذف شد از لیست.", group_data, ms)
				else:
					send_message("⚠️ این کانال تو لیست نیست.", group_data, ms)
			else:
				send_message("❌ یوزرنیم معتبر نیست.", group_data, ms)
		else:
			send_message("❌ یوزرنیم وارد کن.", group_data, ms)
	
	elif text.startswith("حذف عضویت http") and utype in [0, 1, 2, 3]:
		link = text.replace("حذف عضویت", "").strip()
		if link:
			try:
				guid = bot.join_chat(link)["guid"]
				if guid in group_data.get("list_spanser_channel", []):
					group_data["list_spanser_channel"].remove(guid)
					send_message("✅ حذف شد از لیست.", group_data, ms)
				else:
					send_message("⚠️ این کانال تو لیست نیست.", group_data, ms)
			except:
				send_message("❌ لینک معتبر نیست یا خطا رخ داده.", group_data, ms)
		else:
			send_message("❌ لینک وارد کن.", group_data, ms)
			
			
	elif text == "تنظیم ادمین" and utype in [0, 1, 2, 3]:
	    if not rmguid:  
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	        return
	    if "list_admin" not in group_data or not isinstance(group_data["list_admin"], set):
	        group_data["list_admin"] = set()
	    
	    if rmguid not in group_data["list_admin"]:
	        group_data["list_admin"].add(rmguid)
	        send_message("✅ کاربر به عنوان ادمین تنظیم شد.", group_data, ms)
	    else:
	        send_message("❌ خطا: این کاربر از قبل ادمین است.", group_data, ms)
	elif text == "لیست ادمین":
	    if group_data["list_admin"]!=[]:
	        text = "لیست ادمین‌ها:\n\n" + "\n".join(
	            [f"@@ادمین{i+1}@@({guid})" for i, guid in enumerate(group_data["list_admin"])]
	        )
	    else:
	        text = "لیست ادمین‌ها خالی است."
	    send_message(text, group_data, ms)
	elif text.startswith("فیلتر "):
	    word = text.replace("فیلتر ", "").strip()
	    if word:
	        if "list_filter_text" not in group_data:
	            group_data["list_filter_text"] = []
	        if word not in group_data["list_filter_text"]:
	            group_data["list_filter_text"].append(word)
	            send_message(f"✅ کلمه '{word}' به لیست فیلتر اضافه شد.", group_data, ms)
	        else:
	            send_message("❌ این کلمه از قبل در لیست فیلتر وجود دارد.", group_data, ms)
	    else:
	        send_message("❌ لطفاً یک کلمه برای فیلتر وارد کنید.", group_data, ms)
	elif text.startswith("حذف فیلتر "):
	    word = text.replace("حذف فیلتر ", "").strip()
	    if word:
	        if "list_filter_text" in group_data and word in group_data["list_filter_text"]:
	            group_data["list_filter_text"].remove(word)
	            send_message(f"✅ کلمه '{word}' از لیست فیلتر حذف شد.", group_data, ms)
	        else:
	            send_message("❌ این کلمه در لیست فیلتر وجود ندارد.", group_data, ms)
	    else:
	        send_message("❌ لطفاً یک کلمه برای حذف از فیلتر وارد کنید.", group_data, ms)
	elif text == "لیست فیلتر":
	    if "list_filter_text" in group_data and group_data["list_filter_text"]:
	        text = "📜 لیست کلمات فیلتر شده:\n\n"
	        text += "\n".join([f"🔹 {'/'.join(word)}" for word in group_data["list_filter_text"]])
	        send_message(text, group_data, ms)
	    else:
	        send_message("❌ لیست فیلتر خالی است.", group_data, ms)

	elif text == "ضد فحش فعال":
	    if "list_filter_text" not in group_data:
	        group_data["list_filter_text"] = []
	
	    added_words = 0
	    for word in save.get("fosh", []):
	        if word not in group_data["list_filter_text"]:
	            group_data["list_filter_text"].append(word)
	            added_words += 1
	
	    group_data["filter_fosh"] = True
	    send_message(f"✅ ضد فحش **فعال** شد. ({added_words} کلمه به لیست فیلتر اضافه شد)", group_data, ms)
	
	elif text == "ضد فحش غیرفعال":
	    if "list_filter_text" in group_data:
	        before_remove = len(group_data["list_filter_text"])  # تعداد قبل از حذف
	        group_data["list_filter_text"] = [word for word in group_data["list_filter_text"] if word not in save.get("fosh", [])]
	        removed_words = before_remove - len(group_data["list_filter_text"])  # تعداد واقعی حذف‌شده‌ها
	
	    group_data["filter_fosh"] = False
	    send_message(f"❌ ضد فحش **غیرفعال** شد. ({removed_words} کلمه از لیست فیلتر حذف شد)", group_data, ms)
	
	elif text == "ضد تبلیغ فعال":
	    if "list_filter_text" not in group_data:
	        group_data["list_filter_text"] = []
	
	    added_words = 0
	    for word in save.get("tabligh", []):
	        if word not in group_data["list_filter_text"]:  # اگر کلمه قبلاً اضافه نشده، اضافه کن
	            group_data["list_filter_text"].append(word)
	            added_words += 1
	
	    group_data["filter_tabligh"] = True
	    send_message(f"✅ ضد تبلیغ **فعال** شد. ({added_words} کلمه به لیست فیلتر اضافه شد)", group_data, ms)
	
	elif text == "ضد تبلیغ غیرفعال":
	    if "list_filter_text" in group_data:
	        before_remove = len(group_data["list_filter_text"])  # تعداد قبل از حذف
	        group_data["list_filter_text"] = [word for word in group_data["list_filter_text"] if word not in save.get("tabligh", [])]
	        removed_words = before_remove - len(group_data["list_filter_text"])  # تعداد واقعی حذف‌شده‌ها
	
	    group_data["filter_tabligh"] = False
	    send_message(f"❌ ضد تبلیغ **غیرفعال** شد. ({removed_words} کلمه از لیست فیلتر حذف شد)", group_data, ms)


	elif text == "کیل":
	    if rmguid is None:
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	    else:
	        if rutype not in [0, 1, 2, 3, 4, 5]:  # بررسی نوع کاربر
	            if rmguid not in group_data.setdefault("list_kill", []):
	                group_data["list_kill"].append(rmguid)
	                send_message("✅ کاربر به لیست کیل اضافه شد.", group_data, ms)
	            else:
	                send_message("❌ خطا: این کاربر از قبل در لیست کیل وجود دارد.", group_data, ms)
	
	elif text == "لیست کیل":
	    if group_data["list_kill"]:
	        text = "لیست افراد در کیل: \n\n"
	        text += "\n".join([f"@@کیل{i+1}@@({guid})" for i, guid in enumerate(group_data["list_kill"])])
	    else:
	        text = "لیست کیل خالی است."
	    send_message(text, group_data, ms)
	
	elif text.startswith("کیل @"):
	    t = text.replace("کیل @", "").strip()
	    if t:
	        if rutype not in [0, 1, 2, 3, 4, 5]:
	            user_info = bot.get_chat_info_by_username(t)
	            if user_info and "user_guid" in user_info["user"]:
	                guid = user_info["user"]["user_guid"]
	                if guid not in group_data["list_kill"]:
	                    group_data["list_kill"].append(guid)
	                    send_message("✅ کاربر به لیست کیل اضافه شد.", group_data, ms)
	                else:
	                    send_message("❌ این کاربر از قبل در لیست کیل وجود دارد.", group_data, ms)
	            else:
	                send_message("❌ نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("❌ لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)
	
	elif text == "حذف کیل":
	    if rmguid is None:
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	    else:
	        if rmguid in group_data.setdefault("list_kill", []):
	            group_data["list_kill"].remove(rmguid)
	            send_message("✅ کاربر از لیست کیل حذف شد.", group_data, ms)
	        else:
	            send_message("❌ خطا: این کاربر در لیست کیل وجود ندارد.", group_data, ms)
	
	elif text.startswith("حذف کیل @"):
	    t = text.replace("حذف کیل @", "").strip()
	    if t:
	        user_info = bot.get_chat_info_by_username(t)
	        if user_info and "user_guid" in user_info["user"]:
	            guid = user_info["user"]["user_guid"]
	            if guid in group_data["list_kill"]:
	                group_data["list_kill"].remove(guid)
	                send_message("✅ کاربر از لیست کیل حذف شد.", group_data, ms)
	            else:
	                send_message("❌ این کاربر در لیست کیل وجود ندارد.", group_data, ms)
	        else:
	            send_message("❌ نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("❌ لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)


	elif text.startswith("تنظیم ادمین @") and utype in [0, 1, 2, 3]:
	    t = text.replace("تنظیم ادمین @", "").strip()
	    if t:
	        user_info = bot.get_chat_info_by_username(t)
	        if user_info and "user_guid" in user_info["user"]:
	            guid = user_info["user"]["user_guid"]
	            if guid not in group_data["list_admin"]:
	                group_data["list_admin"].append(guid)
	                send_message("کاربر به عنوان ادمین تنظیم شد.", group_data, ms)
	            else:
	                send_message("این کاربر از قبل ادمین است.", group_data, ms)
	        else:
	            send_message("نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)
	
	elif text == "تنظیم ویژه" and utype in [0, 1, 2, 3]:
	    if not rmguid:  
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	        return
	    if "list_special" not in group_data or not isinstance(group_data["list_special"], set):
	        group_data["list_special"] = set()
	
	    if rmguid not in group_data["list_special"]:
	        group_data["list_special"].add(rmguid)
	        send_message("✅ کاربر با موفقیت به لیست ویژه اضافه شد.", group_data, ms)
	    else:
	        send_message("❌ خطا: این کاربر قبلاً در لیست ویژه بوده است.", group_data, ms)
	elif text == "لیست ویژه":
	    if group_data["list_special"]:
	        text = "لیست ویژه‌ها:\n\n" + "\n".join(
	            [f"@@ویژ{i+1}@@({guid})" for i, guid in enumerate(group_data["list_special"])]
	        )
	    else:
	        text = "لیست ویژه‌ها خالی است."
	    send_message(text, group_data, ms)
	
	elif text.startswith("تنظیم ویژه @") and utype in [0, 1, 2, 3]:
	    t = text.replace("تنظیم ویژه @", "").strip()
	    if t:
	        user_info = bot.get_chat_info_by_username(t)
	        if user_info and "user_guid" in user_info["user"]:
	            guid = user_info["user"]["user_guid"]
	            if guid not in group_data["list_special"]:
	                group_data["list_special"].append(guid)
	                send_message("کاربر به عنوان ویژه تنظیم شد.", group_data, ms)
	            else:
	                send_message("این کاربر از قبل ویژه است.", group_data, ms)
	        else:
	            send_message("نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)
				
				
	elif text == "برکنار" and utype in [0, 1, 2, 3]:
	    if rmguid is None:
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	    else:
	        special_list = group_data.setdefault("list_special", set())
	        admin_list = group_data.setdefault("list_admin", set())
	
	        if rmguid in special_list or rmguid in admin_list:
	            special_list.discard(rmguid)
	            admin_list.discard(rmguid)
	            send_message("✅ کاربر برکنار شد.", group_data, ms)
	        else:
	            send_message("❌ خطا: این کاربر در لیست مدیران یا ویژه‌ها نیست.", group_data, ms)
	
	elif text.startswith("برکنار @") and utype in [0, 1, 2, 3]:
	    t = text.replace("برکنار @", "").strip()
	    if t:
	        user_info = bot.get_chat_info_by_username(t)
	        if user_info and "user_guid" in user_info["user"]:
	            guid = user_info["user"]["user_guid"]
	            if guid in group_data["list_special"] or guid in group_data["list_admin"]:
	                group_data["list_special"].discard(guid)
	                group_data["list_admin"].discard(guid)
	                send_message("کاربر برکنار شد.", group_data, ms)
	            else:
	                send_message("این کاربر در لیست مدیران یا ویژه‌ها نیست.", group_data, ms)
	        else:
	            send_message("نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)
	
	elif text == "کال":
	    try:
	        bot.create_voice_chat(group_guid)
	        send_message("تماس صوتی فعال شد.", group_data, ms)
	    except Exception as e:
	        send_message(f"خطا در فعال‌سازی تماس صوتی: {e}", group_data, ms)
		
		
	elif text == "سکوت":
	    if rmguid is None:
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	    else:
	        if rutype not in [0, 1, 2, 3, 4, 5]:  # بررسی نوع کاربر
	            if rmguid not in group_data.setdefault("list_silent", []):
	                group_data["list_silent"].append(rmguid)
	                send_message("✅ کاربر به لیست سکوت اضافه شد.", group_data, ms)
	            else:
	                send_message("❌ خطا: این کاربر از قبل در لیست سکوت وجود دارد.", group_data, ms)
	
	elif text == "لیست سکوت":
	    if group_data["list_silent"]:
	        text = "لیست افراد در سکوت: \n\n"
	        text += "\n".join([f"@@سکوت{i+1}@@({guid})" for i, guid in enumerate(group_data["list_silent"])])
	    else:
	        text = "لیست سکوت خالی است."
	    send_message(text, group_data, ms)
	
	elif text.startswith("سکوت @"):
	    t = text.replace("سکوت @", "").strip()
	    if t:
	        if rutype not in [0, 1, 2, 3, 4, 5]:
		        user_info = bot.get_chat_info_by_username(t)
		        if user_info and "user_guid" in user_info["user"]:
		            guid = user_info["user"]["user_guid"]
		            if guid not in group_data["list_silent"]:
		                group_data["list_silent"].append(guid)
		                send_message("کاربر به لیست سکوت اضافه شد.", group_data, ms)
		            else:
		                send_message("این کاربر از قبل در لیست سکوت وجود دارد.", group_data, ms)
		        else:
		            send_message("نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)
	elif text == "حذف سکوت":
	    if rmguid is None:
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	    else:
	        if rmguid in group_data.setdefault("list_silent", []):
	            group_data["list_silent"].remove(rmguid)
	            send_message("✅ کاربر از لیست سکوت حذف شد.", group_data, ms)
	        else:
	            send_message("❌ خطا: این کاربر در لیست سکوت وجود ندارد.", group_data, ms)
	
	elif text.startswith("حذف سکوت @"):
	    t = text.replace("حذف سکوت @", "").strip()
	    if t:
	        user_info = bot.get_chat_info_by_username(t)
	        if user_info and "user_guid" in user_info["user"]:
	            guid = user_info["user"]["user_guid"]
	            if guid in group_data["list_silent"]:
	                group_data["list_silent"].remove(guid)
	                send_message("کاربر از لیست سکوت حذف شد.", group_data, ms)
	            else:
	                send_message("این کاربر در لیست سکوت وجود ندارد.", group_data, ms)
	        else:
	            send_message("نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)

	elif text == "معاف":
	    if rmguid is None:
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	    else:
	        if rutype not in [0, 1, 2, 3, 4, 5]:  # بررسی نوع کاربر
	            if rmguid not in group_data.setdefault("list_exempt", []):
	                group_data["list_exempt"].append(rmguid)
	                send_message("✅ کاربر به لیست معاف اضافه شد.", group_data, ms)
	            else:
	                send_message("❌ خطا: این کاربر از قبل در لیست معاف وجود دارد.", group_data, ms)
	
	elif text == "لیست معاف":
	    if group_data["list_exempt"]:
	        text = "لیست افراد معاف: \n\n"
	        text += "\n".join([f"@@معاف{i+1}@@({guid})" for i, guid in enumerate(group_data["list_exempt"])])
	    else:
	        text = "لیست معاف خالی است."
	    send_message(text, group_data, ms)
	
	elif text.startswith("معاف @"):
	    t = text.replace("معاف @", "").strip()
	    if t:
	        if rutype not in [0, 1, 2, 3, 4, 5]:
		        user_info = bot.get_chat_info_by_username(t)
		        if user_info and "user_guid" in user_info["user"]:
		            guid = user_info["user"]["user_guid"]
		            if guid not in group_data["list_exempt"]:
		                group_data["list_exempt"].append(guid)
		                send_message("کاربر به لیست معاف اضافه شد.", group_data, ms)
		            else:
		                send_message("این کاربر از قبل در لیست معاف وجود دارد.", group_data, ms)
	        else:
	            send_message("نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)
	
	elif text == "حذف معاف":
	    if rmguid is None:
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	    else:
	        if rmguid in group_data.setdefault("list_exempt", []):
	            group_data["list_exempt"].remove(rmguid)
	            send_message("✅ کاربر از لیست معاف حذف شد.", group_data, ms)
	        else:
	            send_message("❌ خطا: این کاربر در لیست معاف وجود ندارد.", group_data, ms)
	
	elif text.startswith("حذف معاف @"):
	    t = text.replace("حذف معاف @", "").strip()
	    if t:
	        user_info = bot.get_chat_info_by_username(t)
	        if user_info and "user_guid" in user_info["user"]:
	            guid = user_info["user"]["user_guid"]
	            if guid in group_data["list_exempt"]:
	                group_data["list_exempt"].remove(guid)
	                send_message("کاربر از لیست معاف حذف شد.", group_data, ms)
	            else:
	                send_message("این کاربر در لیست معاف وجود ندارد.", group_data, ms)
	        else:
	            send_message("نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)
        
	elif text == "امتیاز فعال" and utype in [0,1,2,3]:
	    save["group"][group_guid].setdefault("emtyaz", False)  # اگر امتیاز وجود ندارد، آن را با مقدار False ایجاد می‌کند
	    save["group"][group_guid]["emtyaz"] = True
	    send_message("سیستم امتیاز فعال شد.", group_data, ms)
	elif text == "امتیاز غیرفعال" and utype in [0,1,2,3]:
	    save["group"][group_guid].setdefault("emtyaz", False)
	    save["group"][group_guid]["emtyaz"] = False
	    send_message("سیستم امتیاز غیرفعال شد.", group_data, ms)
	elif text.startswith("تنظیم امتیاز") and utype in [0,1,2,3]:
	    try:
	        t = int(text.replace("تنظیم امتیاز", "").strip())
	        if rmguid:
	            save["group"].setdefault(group_guid, {}).setdefault("list_emtyaz", {})
	            save["group"][group_guid]["list_emtyaz"].setdefault(rmguid, 0)
	            save["group"][group_guid]["list_emtyaz"][rmguid] = t
	            send_message(f"✅ امتیاز تنظیم شد: {t}", group_data, ms)
	        else:
	            send_message("⚠️ لطفاً یک کاربر را ریپلای کنید.", group_data, ms)
	    except ValueError:
	        send_message("⚠️ مقدار امتیاز نامعتبر است. لطفاً یک عدد وارد کنید.", group_data, ms)
	
	elif text == "حذف امتیاز" and utype in [0,1,2,3]:
	    if rmguid:
	        save["group"].setdefault(group_guid, {}).setdefault("list_emtyaz", {})  # اطمینان از وجود کلیدها
	        if rmguid in save["group"][group_guid]["list_emtyaz"]:
	            save["group"][group_guid]["list_emtyaz"][rmguid] = 0  # تنظیم مقدار امتیاز به 0
	            send_message("🗑️ امتیاز این کاربر به 0 تغییر کرد.", group_data, ms)
	        else:
	            send_message("⚠️ این کاربر هیچ امتیازی نداشت، مقدار آن برابر با 0 تنظیم شد.", group_data, ms)
	    else:
	        send_message("⚠️ لطفاً یک کاربر را ریپلای کنید.", group_data, ms)
	elif text == "بی اهمیت":
	    if rmguid is None:
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	    else:
	        if rutype not in [0, 1, 2, 3, 4, 5]:  # بررسی نوع کاربر
	            if rmguid not in group_data.setdefault("list_no_anser", []):
	                group_data["list_no_anser"].append(rmguid)
	                send_message("✅ کاربر به لیست بی اهمیت اضافه شد.", group_data, ms)
	            else:
	                send_message("❌ خطا: این کاربر از قبل در لیست بی اهمیت وجود دارد.", group_data, ms)
	        else:
	            send_message("⚠️ این کاربر ادمین است و نمی‌توان او را بی‌اهمیت کرد.", group_data, ms)
	
	elif text == "لیست بی اهمیت":
	    
	    if group_data["list_no_anser"]:
	        text = "لیست افراد بی اهمیت: \n\n"
	        text += "\n".join([f"@@بی‌اهمیت{i+1}@@({guid})" for i, guid in enumerate(group_data["list_no_anser"])])
	    else:
	        text = "لیست بی اهمیت خالی است."
	    send_message(text, group_data, ms)
	
	elif text.startswith("بی اهمیت @"):
	    t = text.replace("بی اهمیت @", "").strip()
	    if t:
	        if rutype in [0,1,2,3,4,5]:
		        user_info = bot.get_chat_info_by_username(t)
		        if user_info and "user_guid" in user_info["user"]:
		            guid = user_info["user"]["user_guid"]
		            if guid not in group_data["list_no_anser"]:
		                group_data["list_no_anser"].append(guid)
		                send_message("کاربر به لیست بی اهمیت اضافه شد.", group_data, ms)
		            else:
		                send_message("این کاربر از قبل در لیست بی اهمیت وجود دارد.", group_data, ms)
		        else:
		        	send_message("ادمین هست",group_data,ms)
	        else:
	            send_message("نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)
	
	elif text == "حذف بی اهمیت":
	    if rmguid is None:
	        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
	    else:
	        if rmguid in group_data.setdefault("list_no_anser", []):
	            group_data["list_no_anser"].remove(rmguid)
	            send_message("✅ کاربر از لیست بی اهمیت حذف شد.", group_data, ms)
	        else:
	            send_message("❌ خطا: این کاربر در لیست بی اهمیت وجود ندارد.", group_data, ms)
	
	elif text.startswith("حذف بی اهمیت @"):
	    t = text.replace("حذف بی اهمیت @", "").strip()
	    if t:
	        user_info = bot.get_chat_info_by_username(t)
	        if user_info and "user_guid" in user_info["user"]:
	            guid = user_info["user"]["user_guid"]
	            if guid in group_data["list_no_anser"]:
	                group_data["list_no_anser"].remove(guid)
	                send_message("کاربر از لیست بی اهمیت حذف شد.", group_data, ms)
	            else:
	                send_message("این کاربر در لیست بی اهمیت وجود ندارد.", group_data, ms)
	        else:
	            send_message("نام کاربری وارد شده معتبر نیست.", group_data, ms)
	    else:
	        send_message("لطفاً یک نام کاربری معتبر وارد کنید.", group_data, ms)
		

	elif text == "مدیر" and utype in [0, 1, 2, 3]:
	    if rmguid is None:
	        send_message("❌ لطفاً روی پیام فرد موردنظر ریپلای کنید.", group_data, ms)
	    elif True:
	        group_data["manager"] = rmguid
	        send_message("✅ مدیر تنظیم شد.", group_data, ms)
	    else:
	        send_message("⚠️ خطا: داده‌های گروه نامعتبر هستند.", {}, ms)
	elif text.startswith("تنظیم خوشامدگویی"):
	    t = text.replace("تنظیم خوشامدگویی", "").strip()
	    if t:
	        group_data["list_welcome_text"].append(t)
	        send_message("تنظیم خوشامدگویی انجام شد", group_data, ms)
	    else:
	        send_message("لطفاً متن خوشامدگویی را وارد کنید.", group_data, ms)
	
	elif text.startswith("تنظیم خداحافظی"):
	    t = text.replace("تنظیم خداحافظی", "").strip()
	    if t:
	        group_data["list_goodbye_text"].append(t)
	        send_message("تنظیم خداحافظی انجام شد", group_data, ms)
	    else:
	        send_message("لطفاً متن خداحافظی را وارد کنید.", group_data, ms)
	elif text.startswith("تنظیم قوانین"):
	    t = text.replace("تنظیم قوانین", "").strip()
	    if t:
	        group_data["list_law_text"]=t
	        send_message("تنظیم قوانین انجام شد", group_data, ms)
	    else:
	        send_message("لطفاً متن قوانین را وارد کنید.", group_data, ms)

	elif text == "حذف قوانین":
	    group_data["list_law_text"] = ""
	    send_message("قوانین حذف شد", group_data, ms)


	elif text in ["لیست خوشامدگویی", "لیست خداحافظی"]:
	    list_name = "list_welcome_text" if text == "لیست خوشامدگویی" else "list_goodbye_text"
	    title = "لیست خوشامدگویی" if text == "لیست خوشامدگویی" else "لیست خداحافظی"
	
	    o = 0
	    message_text = f"{title} \n\n"
	    
	    for item in group_data[list_name]:
	        o += 1
	        display_text = item[:40] + "..." if len(item) >= 40 else item
	        message_text += f"{o}: {display_text} \n"
	
	    send_message(message_text, group_data, ms)
	elif text.startswith("تایمر"):
            try:
                lines = text.split("\n")
                if len(lines) < 2:
                    send_message("❌ لطفاً بعد از تایمر، دستورات را در خط‌های جداگانه بنویسید.", save["group"][group_guid], ms)
                    return

                time_part = lines[0].split()
                if len(time_part) != 2 or ":" not in time_part[1]:
                    send_message("❌ فرمت تایمر نادرست است. مثال:\nتایمر 19:30\nدستور اول\nدستور دوم", save["group"][group_guid], ms)
                    return

                hour, minute = map(int, time_part[1].split(":"))
                commands = lines[1:]
                if len(commands) > 3:
                    send_message("❌ فقط می‌توانید حداکثر ۳ دستور در هر تایمر تنظیم کنید.", save["group"][group_guid], ms)
                    return

                now = datetime.now()
                target_time = datetime(now.year, now.month, now.day, hour, minute).strftime("%H:%M")
                if group_guid not in scheduled_tasks:
                    scheduled_tasks[group_guid] = []
                scheduled_tasks[group_guid].append({
                    "time": target_time,
                    "commands": commands,
                    "group_data": save["group"][group_guid],
                    "ms": ms
                })

                send_message(f"✅ تایمر برای {target_time} با {len(commands)} دستور تنظیم شد.", save["group"][group_guid], ms)

            except Exception as e:
                send_message(f"❌ خطا: {str(e)}", save["group"][group_guid], ms)
	elif text == "لیست تایمر":
            if group_guid not in scheduled_tasks or not scheduled_tasks[group_guid]:
                send_message("📋 لیست تایمرها خالی است.", save["group"][group_guid], ms)
                return

            timer_list = "📌 **لیست تایمرهای فعال:**\n"
            for i, task in enumerate(scheduled_tasks[group_guid]):
                commands_text = "\n  - ".join(task["commands"])
                timer_list += f"**{i+1}. ساعت {task['time']}**\n  - {commands_text}\n"

            send_message(timer_list, save["group"][group_guid], ms)
            return
  
  
	elif text.startswith("حذف تایمر"):
            try:
                parts = text.split()
                if len(parts) != 3 or not parts[2].isdigit():
                    send_message("❌ فرمت صحیح: `حذف تایمر 1`", save["group"][group_guid], ms)
                    return

                timer_index = int(parts[2]) - 1
                if group_guid not in scheduled_tasks or timer_index < 0 or timer_index >= len(scheduled_tasks[group_guid]):
                    send_message("❌ شماره تایمر نامعتبر است.", save["group"][group_guid], ms)
                    return

                deleted_timer = scheduled_tasks[group_guid].pop(timer_index)
                send_message(f"✅ تایمر ساعت {deleted_timer['time']} با {len(deleted_timer['commands'])} دستور حذف شد.", save["group"][group_guid], ms)

            except Exception as e:
                send_message(f"❌ خطا: {str(e)}", save["group"][group_guid], ms)
            return

	elif text.startswith("حذف خوشامدگویی"):
		    t = text.replace("حذف خوشامدگویی", "").strip()
		    if t.isdigit():  # چک می‌کنیم که مقدار عددی باشد
		        t = int(t) - 1  # چون لیست از ایندکس 0 شروع می‌شود
		        if 0 <= t < len(group_data["list_welcome_text"]):  # بررسی ایندکس معتبر
		            group_data["list_welcome_text"].pop(t)
		            send_message("حذف شد", group_data, ms)
		        else:
		            send_message("عدد وارد شده نامعتبر است!", group_data, ms)
		    else:
		        send_message("لطفاً یک شماره معتبر وارد کنید!", group_data, ms)
	elif text.startswith("حذف خداحافظی"):
	    t = text.replace("حذف خداحافظی", "").strip()
	    if t.isdigit():
	        t = int(t) - 1
	        if 0 <= t < len(group_data["list_goodbye_text"]):
	            group_data["list_goodbye_text"].pop(t)
	            send_message("حذف شد", group_data, ms)
	        else:
	            send_message("عدد وارد شده نامعتبر است!", group_data, ms)
	    else:
	        send_message("لطفاً یک شماره معتبر وارد کنید!", group_data, ms)
	elif text=="لیست قفل":
			print(88)
			text=f"""
🔹 وضعیت کلی:  
- وضعیت ربات: {"✅" if group_data["rb"] is True else "❌"}  
- حالت سایلنت: {"✅" if group_data["silent_bot"] is True else "❌"}  

🔹 تنظیمات ضداسپم:  
- ضد لینک: {"✅" if group_data["zd_link"] is True else "❌"}  
- ضد فوروارد: {"✅" if group_data["zd_forward"] is True else "❌"}  
- ضد آیدی: {"✅" if group_data["zd_id"] is True else "❌"}  
- ضد عکس: {"✅" if group_data["zd_image"] is True else "❌"}  
- ضد گیف: {"✅" if group_data["zd_gif"] is True else "❌"}  
- ضد فایل: {"✅" if group_data["zd_file"] is True else "❌"}  
- ضد ویس: {"✅" if group_data["zd_voice"] is True else "❌"}  
- ضد موزیک: {"✅" if group_data["zd_music"] is True else "❌"} 
ـ ضد پست: {"✅" if group_data["zed_post"] is True else "❌"} 
ـ ضد استوری: {"✅" if group_data["zed_story"] is True else "❌"} 
ـ ضد نظرسنجی‌: {"✅" if group_data["zed_poll"] is True else "❌"}
ـ ضد هشتک: {"✅" if group_data["zd_hashtack"] is True else "❌"}
ـ ضد شماره: {"✅" if group_data["zd_number"] is True else "❌"}
ـ ضد لایو: {"✅" if group_data["zed_live"] is True else "❌"}
ـ ضد نظرسنجی‌: {"✅" if group_data["zed_poll"] is True else "❌"} 

🔹 ویژگی‌های سرگرمی و ابزارها:  
- سرگرمی: {"✅" if group_data["funny"] is True else "❌"}  
- هوش مصنوعی: {"✅" if group_data["AI"] is True else "❌"}  
- ابزار: {"✅" if group_data["tools"] is True else "❌"}  

🔹 ویژگی‌های سخنگو:  
- سخنگو: {"✅" if group_data["talk"] is True else "❌"}  
- سخنگو با ادب: {"✅" if group_data["talk_Politeness"] is True else "❌"}  
- پرحرفی: {"✅" if group_data["very_talk"] is True else "❌"}  

🔹 مدیریت و امنیت:  
- اخطار: {"✅" if group_data["warning"] is True else "❌"}  
- خوشامدگویی: {"✅" if group_data["welcome"] is True else "❌"}  
- خداحافظی: {"✅" if group_data["goodbye"] is True else "❌"}  
- راهنما: {"✅" if group_data["help"] is True else "❌"}  
- بن ممبر: {"✅" if group_data["ban_member"] is True else "❌"}  
- عضویت اجباری: {"✅" if group_data["spanser_TB"] is True else "❌"} """
			send_message(text,group_data,ms)
	elif text=="لیست ها":
		text="""📌 لیست‌های موجود در ربات:

🔹 لیست قفل‌
🔹 لیست سرگرمی‌
🔹 لیست ابزار
🔹 لیست هوش مصنوعی
🔹 لیست  معاف
🔹 لیست ادمین‌
🔹 لیست  ویژه
🔹 لیست  کیل‌
🔹 لیست  بی‌اهمیت
🔹 لیست  سکوت"""
		send_message(text,group_data,ms)
	clear_lists = {
	    "بی اهمیت": "list_no_anser",
	    "سکوت": "list_silent",
	    "فیلتر": "list_filter",
	    "خوشامدگویی": "list_welcome_text",
	    "خداحافظی": "list_goodbye_text",
	    "عضویت": "list_spanser_channel",
	    "کیل": "list_kill",
	    "ادمین": "list_admin",
	    "ویژه": "list_special",
	    "معاف": "list_exempt",
	    "یادداشت": "list_notes",
	}
	
	if text.startswith("پاکسازی لیست "):
	    key = text.replace("پاکسازی لیست ", "").strip()
	    list_name = clear_lists.get(key)
	
	    if list_name:
	        group_data[list_name] = []  # پاک کردن لیست
	        send_message(f"لیست {key} پاکسازی شد.", group_data, ms)
	    else:
	        send_message("❌ لیست موردنظر یافت نشد.", group_data, ms)		
		
	elif text.startswith("پاکسازی"):
	    if utype in [0,1,2]:
		    try:
		        t = int(text.replace("پاکسازی", "").strip())  # استخراج تعداد موردنظر برای حذف
		    except ValueError:
		        ms.reply("⚠️ لطفاً تعداد پیام‌ها را به‌درستی وارد کنید. مثال: `پاکسازی 50`")
		        return
		
		    deleted_count = 0
		
		    while deleted_count < t :
		        messages = bot.get_messages(group_guid)["messages"]
		        count = sum(1 for item in messages if isinstance(item, dict))
		
		        if count in [0]:
		            ms.reply(f"✅ {deleted_count} پیام پاک شد.")
		            break
		
		        for msg in messages:
		            if isinstance(msg, dict) and "message_id" in msg:
		                bot.delete_messages(group_guid, [msg["message_id"]])
		                deleted_count += 1
		
		                if deleted_count % 1000 == 0:
		                    bot.send_text(group_guid, f"📢 {deleted_count} پیام پاک شد.")
		
		                if deleted_count >= t:
		                    ms.reply(f"✅ {deleted_count} پیام پاک شد.")
		                 
		                    return
	    else:
	        	send_message("فقط سازنده میتونه",group_data,ms)
	warning_types = {
    "لینک": "link",
    "فروارد": "forward",
    "آیدی": "id",
    "عکس": "image",
    "گیف": "gif",
    "فایل": "file",
    "ویس": "voice",
    "موزیک": "music",
    "فحش": "filter"
}

	for key, value in warning_types.items():
		if text.startswith(f"تنظیم اخطار {key}"):
			t = text.replace(f"تنظیم اخطار {key}", "").strip()
			if t:
				try:
					t = int(t)
					group_data["number_warning"][value] = t
					send_message("تنظیم شد", group_data, ms)
				except ValueError:
				    send_message("لطفاً عدد معتبر وارد کنید.", group_data, ms)
				    break
	settings = {
    "ضد لینک": "zd_link",
    "ضد هشتک":"zd_hashtack",
    "ضد شماره":"zd_number",
    "هشتک":"zd_hashtack",
    "شماره":"zd_number",
    "ضد فروارد": "zd_forward",
    "ضد آیدی": "zd_id",
    "ضد عکس": "zd_image",
    "ضد گیف": "zd_gif",
    "ضد ویس": "zd_voice",
    "ضد فایل": "zd_file",
    "ضد موزیک": "zd_music",
    "ضد لایو":"zed_live",
    "ضد پست":"zed_post",
    "ضد استوری":"zed_story",
    "ضد نظرسنجی":"zed_poll",
    "فیلتر":"filter_text",
    "لینک": "zd_link",
    "فروارد": "zd_forward",
    "آیدی": "zd_id",
    "عکس": "zd_image",
    "گیف": "zd_gif",
    "ویس": "zd_voice",
    "فایل": "zd_file",
    "موزیک": "zd_music",
    "لایو":"zed_live",
    "پست":"zed_post",
    "استوری":"zed_story",
    "نظرسنجی":"zed_poll",
    "عضویت اجباری":"spanser_TB",
    "هوش مصنوعی":"AI",
    "سخنگو با ادب":"talk_Politeness",
    "سخنگو باادب":"talk_Politeness",
    "سخنگو":"talk",
    "خداحافظی":"goodbye",
    "خدا حافظی":"goodbye",
    "خدآحافظی":"goodbye",
    "خدآ حافظی":"goodbye",
    "ابزار":"tools",
    "خوشامدگویی":"welcome",
    "خوشامد گویی":"welcome",
    "خوشآمدگویی":"welcome",
    "خوشآمد گویی":"welcome",
    "پرحرفی":"very_talk",
    "پر حرفی":"very_talk",
    "سرگرمی":"funny",
    "بن ممبر":"ban_member",
    "راهنما":"help",
    "قوانین":"law",
    "قانون":"law",
    "اخطار":"warning",
    "حالت سایلنت":"silent_bot"
}
	for key, value in settings.items():
		if text == f"{key} روشن":
			group_data[value] = True
			send_message("✅ فعال شد.", group_data, ms)
			break
		elif text == f"{key} خاموش":
			group_data[value] = False
			send_message("❌ غیرفعال شد.", group_data, ms)
			break
		elif text == f"{key} فعال":
			group_data[value] = True
			send_message("✅ فعال شد.", group_data, ms)
			break
		elif text == f"{key} غیرفعال":
			group_data[value] = False
			send_message("❌ غیرفعال شد.", group_data, ms)
			break
		elif text == f"{key} غیر فعال":
			group_data[value] = False
			send_message("❌ غیرفعال شد.", group_data, ms)
			break




def clear_group(group_guid,group_data,ms):
    deleted_count = 0
    send_message("start",group_data,ms)
    while True:
        try:
            messages = bot.get_messages(group_guid)["messages"]
            if not messages:
                bot.send_text(group_guid, f"✅ {deleted_count} پیام پاک شد.")
                break
            message_ids = [msg["message_id"] for msg in messages if "message_id" in msg]

            bot.delete_messages(group_guid, message_ids)
            deleted_count += len(message_ids)
            if deleted_count % 200 == 0:
                bot.send_text(group_guid, f"📢 {deleted_count} پیام پاک شد.")
        except Exception as e:
            print(f"⚠️ خطا در پاک‌سازی گروه: {e}")
            break
                    
                    
def message_type(type, user_guid, group_data, ms, utype):
	filters = {
        "link": ms.has_link and group_data["zd_link"],
        "forward": ms.is_forward and group_data["zd_forward"],
        "id": "@" in ms.text and group_data["zd_id"],
        "image": type == "Image" and group_data["zd_image"],
        "gif": type == "Gif" and group_data["zd_gif"],
        "file": type == "File" and group_data["zd_file"],
        "voice": type == "Voice" and group_data["zd_voice"],
        "music": type == "Music" and group_data["zd_music"],
        "post" : type=="RubinoPost" and group_data["zed_post"],
        "live" : type=="Live" and group_data["zed_live"],        
        "story" : type=="RubinoStory" and group_data["zed_story"],
        "poll" : type=="Poll" and group_data["zed_poll"],         
        "filter": any(i in ms.text for i in group_data["list_filter_text"]),
        "code": "0.0.0" in ms.text or "1.1.1" in ms.text or "1.2.3" in ms.text or "3.3.3"  in ms.text,
        "number": "09" in ms.text and group_data["zd_number"],
        "hashtack": "#" in ms.text and group_data["zd_hashtack"]
    }
	for idx, (key, condition) in enumerate(filters.items(), 1):
		if condition:
			
			return key
	if ms.text==".":
		ms.delete
		return None
	return None
	
def user_type(user_guid, group_data, ms):
    if not user_guid or not group_data:
        return 9
    role_priority = [
        *((user, 0) for user in save.get("maker_asl", [])),
        (my_guid, 1),
        *((user, 2) for user in save.get("maker", []) if user),
        (group_data.get("manager"), 3) if group_data.get("manager") else None,
        *((user, 4) for user in group_data.get("list_special", [])),
        *((user, 5) for user in group_data.get("list_admin", [])),
        *((user, 6) for user in group_data.get("list_exempt", [])),
        *((user, 7) for user in group_data.get("list_no_anser", [])), 
        *((user, 8) for user in group_data.get("list_silent", [])),
        *((user,10)for user in group_data.get("list_kill",[]))
    ]
    role_priority = [item for item in role_priority if item]
    for user, role in role_priority:
        if user_guid == user:
            return role

    return 9
    
def send_message(text, group_data=None, ms=None, user_guid=None): 
    global message_send_event, message_count, first_message_time 
    try:
        if not text:
            return
        if save["silent"] == True:
        	return
        if ms.is_group:
            font_map = {
                "شلخته": 0, "کشیده": 1, "کشیده ساده": 2,
                "موجی": 3, "تشدید": 4
            }
            group_guid = ms.object_guid
            if group_data is not None:
                font_type = group_data.get("font", "default")
                if font_type in font_map.keys():
                    font_api = "https://api-free.ir/api/font.php?fa="
                    response = requests.get(f"{font_api}{text}")
                    text = response.json()["result"][font_map[font_type]]

            if save.get("silent", False) or (group_data and group_data.get("silent_bot", False)):
                print(f"🚫 پیام در گروه {group_guid} ارسال نشد (ربات در حالت سایلنت است).")
                return

            if not isinstance(ms, FakeMessage):  
                ms.reply(text)  
            else:
                bot.send_text(ms.object_guid, text)              
            save["message"] += 1
            if group_data.get("mes_robot",0):
                group_data["mes_robot"] += 1
            with lock:
                message_count += 1
            message_send_event.set()
        elif ms.is_user and user_guid:
            if not isinstance(ms, FakeMessage):  
                ms.reply(text)  
            else:
                bot.send_text(ms.object_guid, text)
            with lock:
                message_count += 1
            message_send_event.set()
    except Exception as e:
        print(f"⚠️ خطا در ارسال پیام: {str(e)}")


def send_music(link,text,group_guid,mid):
	if save["silent"] == True:
		return
	try:
		global message_send_event, message_count, first_message_time 
		bot.send_music(object_guid=group_guid,file=link,text=text,message_id=mid)
		with lock:
			message_count+=1
			message_send_event.set()
	except:
		None
def send_photo(link,group_data,ms,group_guid,text:None):
	if save["silent"] == True:
		return 
	try:
		global message_send_event, message_count, first_message_time
		bot.send_image(object_guid=group_guid,is_spoil=True,file=link,text=text)
		with lock:
			message_count+=1
			message_send_event.set()
	except:
		None
def warning_send(user_guid, group_data, mtype, ms, guid):
    if not group_data.get("warning", False):
        return
    user_role = user_type(user_guid, group_data, ms)

    if user_role in [0, 1, 2, 3, 4, 5]:
        return
    warning_texts = {
        "id": "آیدی",
        "forward": "فروارد",
        "link": "لینک",
        "image": "عکس",
        "gif": "گیف",
        "file": "فایل",
        "music": "موزیک",
        "voice": "ویس",
        "poll": "نظرسنجی",
        "post": "پست",
        "story": "استوری",
        "filter": "فیلتر",
        "number":"شماره",
        "hashtack":"هشتک"
    }

    # دریافت نام خوانا برای نوع اخطار، اگر وجود نداشت همان مقدار `mtype` را نگه می‌دارد
    warning_name = warning_texts.get(mtype, mtype)

    warnings = group_data.get("list_warning", {})
    number_warning = group_data.get("number_warning", {})

    user_warning_count = warnings.get(user_guid, 0) + 1
    warnings[user_guid] = user_warning_count
    group_data["list_warning"] = warnings  # ذخیره تغییرات

    max_warnings = number_warning.get(mtype, 3)  # مقدار پیش‌فرض ۳ اخطار

    if user_warning_count < max_warnings:
        remaining_warnings = max_warnings - user_warning_count
        text = f"⚠️ ارسال {warning_name} ممنوع است!  @@اخطار@@({user_guid})"
        text += f"  [{user_warning_count}/{max_warnings}]"
        send_message(text, group_data, ms)
    else:
        send_message(f"⛔ @@بن@@({user_guid}) شدید.", group_data, ms)
        ban_member(user_guid, guid, group_data)
 
def ban_member(user_guid,guid,group_data):
	if group_data["ban_member"]:
		try:
			bot.ban_member(guid,user_guid)
		except:
			None


def check_join(group_data, user_guid, ms):
    if not group_data.get("spanser_TB"):
        return True  

    channels_not_joined = []
    for guid in group_data.get("list_spanser_channel", []):
        try:
            if not bot.check_join(guid, user_guid):
                channels_not_joined.append(guid)
        except Exception as e:
            print(f"⚠️ خطا در بررسی عضویت کاربر {user_guid} در کانال {guid}: {e}")

    if channels_not_joined:
        send_message("⚠️ لطفاً ابتدا در کانال‌های موردنظر عضو شوید.", group_data, ms)
        return False
    return True


#####################
def has_sharzh(group_guid, group_data, ms):
    """بررسی می‌کند که آیا گروه شارژ دارد یا نه"""
    if save["group"][group_guid]["sharzh"] <= 0:
        text="اشتراک گروه شما تموم شد لطفا در کانال بیو اشتراک تهیه کنید    \n  "
        send_message(text, group_data, ms)
        bot.leave_chat(group_guid)
        del save["group"][group_guid]
        return True
    return False


#####################

def fetch_url(url, is_json=False):
    """ارسال درخواست و دریافت داده به‌صورت هم‌زمان."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["Result"] if is_json else response.text
    except Exception as e:
        return f"خطا: {e}"

def funny(group_data, text, ms, group_guid, user_guid,rmguid,mid):
	if not group_data.get('funny') or not check_join(group_data, user_guid, ms):
		return False
	name="name"
	rel_request_phrases = [
	    "ربات رل بزنیم؟", "ربات رل", "ربات بیا رل بزنیم", "ربات دوست دختر میشی؟", "ربات دوست پسر میشی؟",
	    "ربات میای باهم رل بزنیم؟", "ربات منو دوست داری؟", "ربات عاشقمی؟", "ربات تو با من رل میزنی؟",
	    "ربات رل بزن دیگه", "ربات میشه رلم باشی؟", "ربات بیا رل بشیم", "ربات رل میشی؟",
	    "ربات زن من میشی؟", "ربات شوهر من میشی؟", "ربات میای دوتایی باشیم؟", "ربات عشقم میشی؟",
	    "ربات میای من و تو یه تیم بشیم؟", "ربات میخوای باهم بریم رل بزنیم؟", "ربات بهم احساس داری؟",
	    "ربات یه رل توپ بزنیم؟", "ربات میای باهم کراش بزنیم؟", "ربات کراشم میشی؟", "ربات بیا جفتم بشو!",
	    "ربات کسی تو زندگیت هست؟", "ربات جای خالی تو دلت داری؟", "ربات بهم حس داری؟", "ربات میشه برام خاص باشی؟",
	    "ربات بیا عاشق بشیم", "ربات حس تنهایی داری؟", "ربات میشه بهم توجه کنی؟", "ربات یه حس خاصی بهت دارم!",
	    "ربات بیا باهم باشیم", "ربات میشه کنارم باشی؟", "ربات میخوای یه رابطه عجیب داشته باشیم؟"
	]
	
	# لیست عبارات مربوط به درخواست کات کردن
	breakup_phrases = [
	    "ربات کات کنیم؟", "ربات کات", "ربات بیا کات کنیم", "ربات دیگه دوستت ندارم", "ربات میخوام ترکت کنم",
	    "ربات بریم دنبال زندگی خودمون", "ربات نمی‌خوام دیگه با هم باشیم", "ربات تمومش کنیم", "ربات دیگه بین ما چیزی نیست",
	    "ربات وقتشه جدا بشیم", "ربات دیگه حس خاصی بهت ندارم", "ربات به نظرت ما به درد هم می‌خوریم؟"
	]
	keywords_betrayal = ["رل","یواشکی", "مخفی", "پنهونی", "چندتا", "موازی", "یه رل دیگه", "پارتنر دوم", 
                      "بدون اینکه کسی بفهمه", "شانسمو امتحان کنم", "از رلت خسته نشدی", "یکی دیگه", 
                      "چرا فقط یکی", "همزمان", "قول میدم لو نره"]
	
	# پردازش پیام‌های کاربران
	if text in rel_request_phrases and group_data["talk"]:
	    if has_sharzh(group_guid, group_data, ms): return
	    if group_data["rel"] == "":
	        # جواب‌هایی که ربات ممکنه بده
	        options = [
	            "آره عزیزم، بیا رل بزنیم! ❤️", "نه عزیز، دلم جای دیگه گیره... 🥲", "بذار فکر کنم... نه!", 
	            "اممم، راستش هنوز آماده نیستم برای یه رابطه جدید... 😕", "خیلی پیشنهاد وسوسه‌کننده‌ایه، ولی نه! 🤨",
	            "اول باید اعتمادمو جلب کنی، بعدش شاید... 😏", "تو مطمئنی می‌خوای با یه ربات رل بزنی؟! 😂",
	            "خب... شاید... ولی یه چیزی کم داره! 🤔", "بذار فال بگیرم... نه، بهم نمی‌خوریم! 😂", 
	            "اگه بهم گل بخری، شاید قبول کنم! 🌹", "واقعاً؟ یعنی منو دوست داری؟ 😳", 
	            "تو اولین نفری نیستی که اینو ازم می‌پرسی... ولی هنوز جوابم نه هست! 😂"
	        ]
	        weights = [25, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]  # احتمال زیاد جواب نه بده، ولی کمی شانس جواب‌های متفاوت هم هست
	        result = random.choices(options, weights=weights, k=1)[0]
	
	        if result.startswith("آره"):
	            group_data["rel"] = user_guid
	        
	        send_message(result, group_data, ms)
	
	    else:
	        responses = [
	            f"من خودم رل دارم، برو پی کارت! 😏 اینم آیدیش: @@{name}@@({group_data['rel']})",
	            f"داری مزاحم میشی! 🥺 به رلم میگم که بیان حسابتو برسن! 📣 کجایی عزیزم؟ این داره اذیتم میکنه: @@{name}@@({group_data['rel']})",
	            f"دیگه چی؟ میخوای رلمو ول کنم واسه تو؟ نه عزیزم، برو یکی دیگه رو پیدا کن! 😌",
	            f"الان یعنی تو میخوای من خیانت کنم؟ نامرد نباش، اینم رلم: @@{name}@@({group_data['rel']})",
	            f"نمی‌تونم، چون قلبم قبلاً به کسی دیگه تعلق گرفته... 💕 اینم آیدیش: @@{name}@@({group_data['rel']})"
	        ]
	        result = random.choice(responses)
	        send_message(result, group_data, ms)
	elif text.startswith("بازی حدس"):
	    if has_sharzh(group_guid, group_data, ms): return
	    try:
	        user_guess = int(text.replace("بازی حدس", "").strip())
	        if user_guess < 1 or user_guess > 10:
	            send_message("⚠ لطفاً یک عدد بین ۱ تا ۱۰ حدس بزنید.\nمثال: `بازی حدس ۵`", group_data, ms)
	            return
	    except ValueError:
	        send_message("⚠ لطفاً عددی بین ۱ تا ۱۰ انتخاب کنید.\nمثال: `بازی حدس ۳`", group_data, ms)
	        return
	
	    random_number = random.randint(1, 10)  # انتخاب عدد تصادفی
	
	    if user_guess == random_number:
	        outcome_text = "🎯 تبریک! حدست درست بود! 🎉"

	    else:
	        outcome_text = f"❌ حدست اشتباه بود! عدد درست {random_number} بود."

	    text = f"🎮 **بازی: حدس عدد**\n\n🤔 **عدد انتخابی تو:** {user_guess}\n🎲 **عدد واقعی:** {random_number}\n\n{outcome_text}"
	    send_message(text, group_data, ms)
	elif text == "تاس":
	    if has_sharzh(group_guid, group_data, ms): return
	    dice_number = random.randint(1, 6)  # عدد تصادفی بین ۱ تا ۶
	    dice_emojis = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]  # نمایش چهره‌های تاس
	    text = f"🎲 تاس انداخته شد...\n\nنتیجه: {dice_emojis[dice_number - 1]} ({dice_number})"
	    send_message(text, group_data, ms)
	
	elif text == "سکه":

	    if has_sharzh(group_guid, group_data, ms): return
	    coin_sides = ["🪙 شیر","🪙 خط"]
	    result = random.choice(coin_sides)
	    text = f"{result}"
	    send_message(text, group_data, ms)

	elif text.startswith("سکه"):
	    if has_sharzh(group_guid, group_data, ms): return
	    user_choice = text.replace("سکه", "").strip()
	
	    if user_choice not in ["شیر", "خط"]:
	        send_message("⚠ لطفاً یکی از گزینه‌های «شیر» یا «خط» را انتخاب کنید.\nمثال: `سکه شیر`", group_data, ms)
	    else:
	        coin_sides = [("🪙 شیر", "🍀 خوش‌شانسی آوردی!"), ("🪙 خط", "🌧 بدشانسی آوردی!")]
	        result, message = random.choice(coin_sides)
	
	        if user_choice in result:
	            outcome_text = "🎉 تبریک! بردی!"
	        else:
	            outcome_text = "😢 باختی! شاید دفعه بعد شانست بزنه."
	        text = f"{result}!\n{message}\n\n{outcome_text}"
	        send_message(text, group_data, ms)
	elif text.startswith("بازی سنگ") or text.startswith("بازی "):
	    if has_sharzh(group_guid, group_data, ms): return
	    choices = {"سنگ": "🪨", "کاغذ": "📄", "قیچی": "✂"}
	    user_choice = text.replace("بازی", "").strip()
	
	    if user_choice not in choices:
	        send_message("⚠ لطفاً یکی از گزینه‌های «سنگ»، «کاغذ» یا «قیچی» را انتخاب کنید.\nمثال: `بازی سنگ`", group_data, ms)
	        return
	
	    bot_choice = random.choice(list(choices.keys()))  # انتخاب تصادفی برای ربات
	
	    # تعیین نتیجه بازی
	    if user_choice == bot_choice:
	        outcome_text = "😐 مساوی شد! دوباره امتحان کن."
	    elif (user_choice == "سنگ" and bot_choice == "قیچی") or \
	         (user_choice == "کاغذ" and bot_choice == "سنگ") or \
	         (user_choice == "قیچی" and bot_choice == "کاغذ"):
	        outcome_text = "🎉 بردی! آفرین!"
	    else:
	        outcome_text = "😢 باختی! شانست بزن دفعه بعد."
	    text = f"🎮 **بازی: سنگ، کاغذ، قیچی**\n\n🤖 **انتخاب من:** {choices[bot_choice]} {bot_choice}\n🧑‍💻 **انتخاب تو:** {choices[user_choice]} {user_choice}\n\n{outcome_text}"
	    send_message(text, group_data, ms)    
        

	elif text == "شخصیت من":
	    if has_sharzh(group_guid, group_data, ms): return
	    personalities = [
	        "🔥 ماجراجو و پرانرژی",
	        "🧠 باهوش و منطقی",
	        "😂 شوخ‌طبع و بامزه",
	        "😎 خونسرد و باحال",
	        "😇 مهربون و دلسوز",
	        "👑 رئیس و کاردرست",
	        "👻 مرموز و ساکت",
	        "🎭 دمدمی‌مزاج و غیرقابل پیش‌بینی",
	        "🤖 مثل یه ربات، منطقی و دقیق",
	        "🐢 آروم و صبور",
	        "🐉 اژدهای پرقدرت!"
	        "🪐بی کار "
	    ]
	
	    text = f"🎭 شخصیت تو: {random.choice(personalities)}"
	    send_message(text, group_data, ms)
	elif text in [
			"سازنده", "برنامه‌نویس", "توسعه‌دهنده", "کدنویس", "نویسنده", "خالق", "مهندس ربات",
			"برنامه‌ساز", "ربات‌نویس", "برنامه‌ریز", "مجری", "پشتیبان", "پشتیبانی", "تیم فنی",
			"کادر فنی", "دولوپر", "طراح ربات", "سازنده پروژه", "کدنویس اصلی", "مهندس نرم‌افزار",
			"توسعه‌دهنده نرم‌افزار", "برنامه‌نویس حرفه‌ای", "طراح سیستم", "معمار نرم‌افزار"
		]:
			text = f"@@♗→ᗩᘻᓰᖇ@@(u0F8dTt0cee5aa71f5a29888ff90dddd)"
			send_message(text, group_data, ms)
	elif text=="شغل آینده":
		    if has_sharzh(group_guid, group_data, ms): return
		    
		    jobs = [
		        "👨‍⚖️ قاضی عدالت‌خواه",
		        "👨‍🚀 فضانورد شجاع",
		        "🎭 بازیگر معروف",
		        "👨‍🍳 سرآشپز حرفه‌ای",
		        "💻 برنامه‌نویس نخبه",
		        "🕵️‍♂️ کارآگاه زبده",
		        "🎸 خواننده پرطرفدار",
		        "✈️ خلبان ماهر",
		        "🏥 دکتر متخصص",
		        "📚 نویسنده خلاق",
		        "📷 عکاس حرفه‌ای",
		        "🏆 ورزشکار موفق",
		        "🚀 مدیر استارتاپ بزرگ",
		        "🎮 گیمر حرفه‌ای",
		        "🛠️ مهندس خلاق",
		        "💰 تاجر ثروتمند",
		        "🎤 مجری تلویزیونی",
		        "⚖️ وکیل معروف",
		        "🖌️ نقاش هنرمند",
		        "🎼 آهنگساز محبوب",
		        "🌍 جهانگرد ماجراجو",
		        "🎢 طراح شهربازی",
		        "🏗️ معمار برجسته",
		        "🚓 افسر پلیس",
		        "📡 کارشناس هواشناسی",
		        "🎯 مربی انگیزشی",
		        "🧪 دانشمند دیوانه",
		        "🎩 شعبده‌باز حرفه‌ای",
		        "📖 مترجم چندزبانه",
		        "🛳️ ناخدای کشتی",
		        "🏋️ مربی بدنسازی",
		        "🛍️ طراح مد و لباس",
		        "🎨 گرافیست خلاق",
		        "👨‍🏫 استاد دانشگاه",
		        "🎥 کارگردان سینما",
		        "💼 مدیر بانک",
		        "🍔 مدیر فست‌فود زنجیره‌ای",
		        "🏹 شکارچی گنج",
		        "🦸‍♂️ ابرقهرمان واقعی",
		        "🎮 تستر بازی‌های ویدیویی",
		        "🔧 تعمیرکار حرفه‌ای",
		        "🚀 مهندس ناسا",
		        "🐶 دامپزشک مهربان",
		        "📰 خبرنگار جنجالی",
		        "📞 اپراتور مرکز تماس",
		        "🎶 تنظیم‌کننده موسیقی",
		        "🎙️ دوبلور انیمیشن",
		        "🎾 مربی تنیس",
		        "🏖️ راهنمای تور مسافرتی"
		        "🎮گیمر"
		        "🎬 کارگردان فیلم "
		        "🚔پلیس راهنمایی رانندگی "
		        "🛸 فضایی"
		        "🧯 خرابکار"
		        "💎 فروشنده اجسام قیمتی "
		        "❤️ عشق من "
		    ]
		    
		    future_job = random.choice(jobs)  # انتخاب تصادفی شغل  
		    send_message(f"🔮 شغل آینده‌ی شما: {future_job}!", group_data, ms)
	elif text == "فال صوتی":
	    if has_sharzh(group_guid, group_data, ms): return
	
	    url = "https://open.wiki-api.ir/apis-1/Horoscope"
	    response = requests.get(url)
	
	    if response.status_code == 200:
	        data = response.json()
	        
	        if data["status"]:
	            audio_url = data["results"]["audio"]
	
	            message = f"📜 فال شما"
	            send_music(audio_url, message,group_guid, mid)
	        
	        else:
	            send_message("⚠ خطایی در دریافت فال رخ داد. لطفاً دوباره امتحان کنید.", group_data, ms)
	
	    else:
	        send_message("⚠ خطا در اتصال به وب‌سرویس فال حافظ.", group_data, ms)
	elif text.startswith("اسم و فامیل با"):
	    if has_sharzh(group_guid, group_data, ms): return
	    try:
	        harf = text.replace("اسم و فامیل با", "").strip()
	        response = requests.get(f"https://api.codebazan.ir/esm-famil/new.php?text={harf}")
	        if response.status_code == 200:
	            try:
	                data = response.json()
	                result = ""
	                for key, values in data.items():
	                    if isinstance(values, list) and values:
	                        result += f"{key}: {values[0]}\n"
	                if result:
	                    send_message(result.strip(), group_data, ms)
	                else:
	                    send_message("⚠️ هیچ موردی یافت نشد.", group_data, ms)
	            except Exception as e:
	                send_message("⚠️ خطا در پردازش داده‌ها", group_data, ms)
	        else:
	            send_message("⚠️ خطا در ارتباط با سرور.", group_data, ms)
	    except Exception as e:
	        send_message(f"⚠️ خطای غیرمنتظره: {str(e)}", group_data, ms)
	elif text=="فیلم من":
		    if has_sharzh(group_guid, group_data, ms): return
		    
		    movies = [
		        "🦇 شوالیه تاریکی – بتمن",
		        "⚡ انتقام‌جویان – اونجرز",
		        "🧙 هری پاتر و سنگ جادو",
		        "🚀 جنگ ستارگان – استار وارز",
		        "🦖 پارک ژوراسیک",
		        "🕷️ مرد عنکبوتی – اسپایدرمن",
		        "🛸 میان‌ستاره‌ای – اینتراستلار",
		        "🔥 بازی تاج و تخت",
		        "🏎️ سریع و خشن",
		        "🦸 واندر وومن",
		        "👻 احضار – کانجورینگ",
		        "🔫 جان ویک",
		        "🎭 جوکر",
		        "🤖 من، ربات – I, Robot",
		        "⏳ تلقین – اینسپشن",
		        "💰 گرگ وال استریت",
		        "🐉 هابیت",
		        "🌍 روز استقلال",
		        "🤯 باشگاه مبارزه",
		        "⚖️ وکیل مدافع شیطان",
		        "🎩 پرستیژ",
		        "🎶 لالالند",
		        "🏹 عطش مبارزه – هانگر گیمز",
		        "👮 فرار از شاوشنک",
		        "🤖 ترمیناتور",
		        "🎬 پدرخوانده",
		        "🦁 شیرشاه",
		        "🎸 راک‌استار",
		        "💀 دزدان دریایی کارائیب",
		        "🌊 تایتانیک",
		        "🧟 رزیدنت اویل",
		        "🏔️ اورست",
		        "🏀 مربی کارتر",
		        "🚔 پلیس آهنی",
		        "🎤 بوهمین راپسودی",
		        "🔪 جیغ",
		        "💥 ماتریکس",
		        "🔬 گتاکا",
		        "🕵️ شرلوک هلمز",
		        "🎤 بچه رئیس",
		        "🐼 پاندای کونگ‌فوکار",
		        "🍫 چارلی و کارخانه شکلات‌سازی",
		        "🎅 تنها در خانه",
		        "🦸 لوگان",
		        "🎖️ نجات سرباز رایان",
		        "🚁 اینسپشن",
		        "🌪️ طوفان جغرافیایی",
		        "🎭 نقاب",
		        "🌌 نگهبانان کهکشان",
		        "🎨 رَتاتویی",
		        "🍕 لاک‌پشت‌های نینجا",
		        "🦍 گودزیلا در برابر کینگ‌کونگ",
		        "🕶️ مردان سیاه‌پوش",
		        "🌠 شازده کوچولو",
		        "💊 دارک سیتی"
		        "👓پسران بد"
		        "🛢 خرابکاران"
		        "🔫 دزدان "
		        
		    ]
		    
		    selected_movie = random.choice(movies)  # انتخاب تصادفی فیلم  
		    send_message(f"🎬 فیلم مناسب برای تو: {selected_movie}!", group_data, ms)


	elif text.startswith("برعکس"):
	    if has_sharzh(group_guid, group_data, ms): return
	    sentence = text.replace("برعکس", "").strip()
	    
	    if not sentence:
	        send_message("⚠ لطفاً یک جمله بنویسید.\nمثال: `برعکس سلام دنیا`", group_data, ms)
	        return
	    
	    reversed_sentence = sentence[::-1]  # معکوس کردن متن
	    print(reversed_sentence)
	    send_message(f"🔄 جمله‌ی برعکس:\n🔹 {reversed_sentence}", group_data, ms)
	    
	    
	elif text=="اگه حیوان بودم":
	    if has_sharzh(group_guid, group_data, ms): return
	    
	    animals = [
	        "🦁 شیر - قدرتمند و شجاع!",
	        "🦊 روباه - باهوش و زیرک!",
	        "🐺 گرگ - تنها ولی قوی!",
	        "🐼 پاندای بامزه و آرام!",
	        "🐍 مار - مرموز و خطرناک!",
	        "🦅 عقاب - پادشاه آسمان‌ها!",
	        "🐘 فیل - مهربان و قوی!",
	        "🐯 ببر - نترس و پرهیبت!",
	        "🐦 قناری - خوش‌صدا و آرام!",
	        "🐻 خرس - صبور ولی خطرناک!",
	        "🦉 جغد - دانا و شب‌زنده‌دار!",
	        "🐨 کوالا - آرام و خوابالو!",
	        "🦄 اسب تک‌شاخ - افسانه‌ای و خاص!",
	        "🦋 پروانه - زیبا و لطیف!",
	        "🦜 طوطی - پرحرف و باهوش!",
	        "🐬 دلفین - بازیگوش و اجتماعی!",
	        "🦏 کرگدن - سرسخت و مقاوم!",
	        "🐴 اسب - سریع و نجیب!",
	        "🦢 قو - زیبا و وفادار!",
	        "🐒 میمون - شیطون و بازیگوش!",
	        "🦔 جوجه‌تیغی - کوچک ولی مقاوم!",
	        "🐊 کروکودیل - بی‌رحم و قدرتمند!",
	        "🐌 حلزون - آروم و صبور!",
	        "🦇 خفاش - شب‌زی و اسرارآمیز!",
	        "🐿️ سنجاب - زرنگ و پرجنب‌وجوش!",
	        "🦡 گورکن - جسور و نترس!",
	        "🐋 نهنگ - غول آرام دریاها!",
	        "🐜 مورچه - سخت‌کوش و منظم!",
	        "🐢 لاک‌پشت - صبور و باحوصله!",
	        "🦎 آفتاب‌پرست - منعطف و سازگار!",
	        "🐃 بوفالو - قوی و سرسخت!",
	        "🐩 سگ پشمالو - وفادار و دوست‌داشتنی!",
	        "🦌 گوزن - ظریف و سریع!",
	        "🦢 لک‌لک - خوش‌یمن و خوش‌قدم!",
	        "🐉 اژدهای افسانه‌ای - نیرومند و اسرارآمیز!"
	    ]
	    
	    chosen_animal = random.choice(animals)
	    
	    send_message(f"🦁 اگه حیوان بودی، {chosen_animal}", group_data, ms) 
	    
	    
	    
	    
	elif text.startswith("ایموجی اسم"):
		    if has_sharzh(group_guid, group_data, ms): return
		    
		    name = text.replace("ایموجی اسم", "").strip()
		    
		    if not name:
		        send_message("⚠ لطفاً یک اسم وارد کنید.\nمثال: `ایموجی اسم علی`", group_data, ms)
		        return
		    
		    # تعریف حروف و ایموجی‌های مرتبط
		    letter_to_emoji = {
		        "ا": "🔤", "ب": "🐝", "پ": "🍀", "ت": "🌟", "ث": "🎭",
		        "ج": "🎸", "چ": "🌈", "ح": "❤️", "خ": "🔥", "د": "💎",
		        "ذ": "🦉", "ر": "🌹", "ز": "⚡", "ژ": "🎷", "س": "⭐",
		        "ش": "🌊", "ص": "☀️", "ض": "🌑", "ط": "🌍", "ظ": "🕶️",
		        "ع": "👀", "غ": "🦜", "ف": "🎼", "ق": "🎤", "ک": "🎩",
		        "گ": "🐉", "ل": "🌙", "م": "🎵", "ن": "🎶", "و": "🌎",
		        "ه": "💖", "ی": "💡"
		    }
		    
		    # تبدیل اسم به ایموجی‌ها
		    emoji_name = "".join(letter_to_emoji.get(char, char) for char in name)
		    
		    send_message(f"🔠 اسم به ایموجی:\n{emoji_name}", group_data, ms)



	elif text.startswith("تاس"):
	    if has_sharzh(group_guid, group_data, ms): return
	    user_guess = text.replace("تاس", "").strip()
	
	    if user_guess and not user_guess.isdigit():
	        send_message("⚠ لطفاً یک عدد بین ۱ تا ۶ حدس بزنید.\nمثال: `تاس ۳`", group_data, ms)
	        return
	
	    dice_number = random.randint(1, 6)  # عدد تصادفی بین ۱ تا ۶
	    dice_emojis = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]  # نمایش چهره‌های تاس
	    dice_result = dice_emojis[dice_number - 1]
	
	    if user_guess:
	        user_guess = int(user_guess)
	        if user_guess == dice_number:
	            outcome_text = "🎉 تبریک! حدست درست بود!"
	        else:
	            outcome_text = f"😢 حدست اشتباه بود! عدد واقعی {dice_number} بود."
	    else:
	        outcome_text = "🎲 تاس انداخته شد!"
	    text = f"{dice_result} ({dice_number})\n\n{outcome_text}"
	    send_message(text, group_data, ms)
    
    
	elif text == "آمار گروه" or text=="امار گروه":
	    if has_sharzh(group_guid, group_data, ms): return
	    try:
	        group_info = bot.get_chat_info(group_guid)
	        if not group_info:
	            send_message("❌ اطلاعات این گروه در دسترس نیست.", group_data, ms)
	            return
	
	        # اطلاعات کلی گروه
	        group_data_info = group_info.get("group", {})
	        group_title = group_data_info.get("group_title", "نامشخص")
	        group_bio = group_data_info.get("description", "ندارد")
	        member_count = group_data_info.get("count_members", "نامشخص")
	        slow_mode = group_data_info.get("slow_mode", 0)
	        chat_history = "فعال" if group_data_info.get("chat_history_for_new_members") else "غیرفعال"
	        reactions_status = "فعال" if group_data_info.get("chat_reaction_setting", {}).get("reaction_type") else "غیرفعال"
	
	        # تعداد پیام‌های ارسال‌شده، حذف‌شده، ورود و خروج اعضا
	        total_messages = group_data.get("all_message", 0)
	        deleted_messages = group_data.get("delete_message", 0)
	        new_members = group_data.get("new_member", 0)
	        left_members = group_data.get("left_member", 0)
	
	        # پیدا کردن ۵ کاربری که بیشترین پیام ارسال کرده‌اند
	        user_messages = group_data.get("number_message", {})
	        top_users = sorted(user_messages.items(), key=lambda x: x[1], reverse=True)[:5]
	
	        # دریافت نام کاربران از API
	        top_users_text = []
	        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
	
	        for i, (user_guid, msg_count) in enumerate(top_users):
	            user_info = bot.get_chat_info(user_guid)
	            user_name = user_info.get("user", {}).get("first_name", "").strip() or "کاربر ناشناس"
	            top_users_text.append(f"{medals[i]} {user_name}: {msg_count} پیام")
	
	        top_users_text = "\n".join(top_users_text) if top_users else "هیچ کاربری ثبت نشده است."
	
	        # ساخت پیام آمار
	        stats_message = (
	            f"📊 آمار گروه: {group_title}\n"
	            f"شارژ گروه : {group_data['sharzh']} \n "
	            f"• • • • • • • • • •\n"
	            f"• 📝 بیوگرافی: {group_bio}\n"
	            f"• • • • • • • • • •\n"
	            f"• تعداد اعضا: {member_count}\n"
	            f"• حالت اسلومد: {slow_mode} ثانیه\n"
	            f"• تاریخچه چت: {chat_history}\n"
	            f"• واکنش‌ها: {reactions_status}\n"
	            f"• • • • • • • • • •\n"
	            f"• کل پیام‌ها: {total_messages}\n"
	            f"• پیام‌های حذف‌شده: {deleted_messages}\n"
	            f"• اعضای جدید: {new_members}\n"
	            f"• اعضایی که ترک کردند: {left_members}\n"
	            f"• • • • • • • • • •\n"
	            f"🏆 برترین ارسال‌کنندگان پیام:\n{top_users_text}")
	
	        send_message(stats_message, group_data, ms)
	
	    except Exception as e:
	        send_message("❌ خطایی رخ داد. لطفاً دوباره امتحان کنید.", group_data, ms)
	        print(f"⚠️ خطا در دریافت آمار گروه: {e}")   
        
	elif text == "آمار" or text=="امار":
	    if has_sharzh(group_guid, group_data, ms): return
	    try:
	        # بررسی اینکه rmguid خالی نباشد
	        if not rmguid:
	            send_message("❌ لطفاً روی پیام کاربر موردنظر ریپلای کنید.", group_data, ms)
	            return
	
	        user_info = bot.get_chat_info(rmguid)
	        if not user_info:
	            send_message("❌ اطلاعات این کاربر در دسترس نیست.", group_data, ms)
	            return
	
	        # دریافت اطلاعات پایه
	        user_data = user_info.get("user", {})
	        chat_data = user_info.get("chat", {})
	        abs_object = chat_data.get("abs_object", {})
	
	        first_name = abs_object.get("first_name", "نامشخص")
	        username = user_data.get("username", "ندارد")
	        user_guid = user_data.get("user_guid", "نامشخص")
	
	        # تعداد پیام‌ها و اخطارها
	        msg_count = group_data.get("number_message", {}).get(rmguid, 0)
	        warnings = len(group_data.get("list_warning", {}).get(rmguid, []))
	
	        # بیوگرافی
	        bio = user_data.get("bio", "ندارد")
	
	        # وضعیت حساب
	        is_blocked = "مسدود شده" if chat_data.get("is_blocked", False) else "فعال"
	
	        # وضعیت آنلاین بودن
	        last_online = user_data.get("last_online", 0)
	        status = "آنلاین" if last_online > 0 else "آفلاین"
	
	        # قابلیت دریافت تماس ویدیویی و صوتی
	        can_receive_call = "بله" if user_info.get("can_receive_call", False) else "خیر"
	        can_video_call = "بله" if user_info.get("can_video_call", False) else "خیر"
	
	        # دریافت مالک گروه از دیکشنری save
	        maker_guid = save.get("maker", "")
	
	        # بررسی وضعیت مالک، ادمین و ویژه
	        is_maker = "بله" if maker_guid == rmguid else "خیر"
	        is_manager = "بله" if group_data.get("manager") == rmguid else "خیر"
	        is_admin = "بله" if rmguid in group_data.get("list_admin", []) else "خیر"
	        is_special = "بله" if rmguid in group_data.get("list_special", []) else "خیر"
	
	        # ارسال پیام آمار
	        stats_message = (
	            f"🔹 نام: {first_name}\n"
	            f"🔹 نام کاربری: {('@' + username) if username != 'ندارد' else 'ندارد'}\n"
	            f"🔹 شناسه: {user_guid}\n"
	            f"🔹 تعداد پیام‌ها: {msg_count}\n"
	            f"🔹 تعداد اخطارها: {warnings}\n"
	            f"🔹 وضعیت: {status}\n"
	            f"🔹 بیوگرافی: {bio}\n"
	            f"🔹 وضعیت حساب: {is_blocked}\n"
	            f"🔹 تماس صوتی: {can_receive_call}\n"
	            f"🔹 تماس ویدیویی: {can_video_call}\n"
	            f"🔹 مالک گروه: {is_maker}\n"
	            f"🔹 مدیر گروه: {is_manager}\n"
	            f"🔹 ادمین ربات: {is_admin}\n"
	            f"🔹 ویژه گروه: {is_special}"
	        )
	
	        send_message(stats_message, group_data, ms)
	
	    except Exception as e:
	        send_message("❌ خطایی رخ داد. لطفاً دوباره امتحان کنید.", group_data, ms)
	        print(f"⚠️ خطا در دریافت آمار: {e}")

	elif text == "آمارم" or text=="امارم":
	    if has_sharzh(group_guid, group_data, ms): return
	    try:
	        user_guid = ms.author_guid  # دریافت شناسه ارسال‌کننده پیام
	
	        user_info = bot.get_chat_info(user_guid)
	        if not user_info:
	            send_message("❌ اطلاعات شما در دسترس نیست.", group_data, ms)
	            return
	
	        # دریافت اطلاعات پایه
	        user_data = user_info.get("user", {})
	        chat_data = user_info.get("chat", {})
	        abs_object = chat_data.get("abs_object", {})
	
	        first_name = abs_object.get("first_name", "نامشخص")
	        username = user_data.get("username", "ندارد")
	
	        # تعداد پیام‌ها و اخطارها
	        msg_count = group_data.get("number_message", {}).get(user_guid, 0)
	        warnings = len(group_data.get("list_warning", {}).get(user_guid, []))
	
	        # بیوگرافی
	        bio = user_data.get("bio", "ندارد")
	
	        # وضعیت حساب
	        is_blocked = "مسدود شده" if chat_data.get("is_blocked", False) else "فعال"
	
	        # وضعیت آنلاین بودن
	        last_online = user_data.get("last_online", 0)
	        status = "آنلاین" if last_online > 0 else "آفلاین"
	
	        # قابلیت دریافت تماس ویدیویی و صوتی
	        can_receive_call = "بله" if user_info.get("can_receive_call", False) else "خیر"
	        can_video_call = "بله" if user_info.get("can_video_call", False) else "خیر"
	
	        # دریافت مالک گروه از دیکشنری save
	        maker_guid = save.get("maker", "")
	
	        # بررسی وضعیت مالک، ادمین و ویژه
	        is_maker = "بله" if maker_guid == user_guid else "خیر"
	        is_manager = "بله" if group_data.get("manager") == user_guid else "خیر"
	        is_admin = "بله" if user_guid in group_data.get("list_admin", []) else "خیر"
	        is_special = "بله" if user_guid in group_data.get("list_special", []) else "خیر"
	
	        # ارسال پیام آمار شخصی
	        stats_message = (
	            f"🔹 نام: {first_name}\n"
	            f"🔹 نام کاربری: {('@' + username) if username != 'ندارد' else 'ندارد'}\n"
	            f"🔹 شناسه: {user_guid}\n"
	            f"🔹 تعداد پیام‌ها: {msg_count}\n"
	            f"🔹 تعداد اخطارها: {warnings}\n"
	            f"🔹 وضعیت: {status}\n"
	            f"🔹 بیوگرافی: {bio}\n"
	            f"🔹 وضعیت حساب: {is_blocked}\n"
	            f"🔹 تماس صوتی: {can_receive_call}\n"
	            f"🔹 تماس ویدیویی: {can_video_call}\n"
	            f"🔹 مالک گروه: {is_maker}\n"
	            f"🔹 مدیر گروه: {is_manager}\n"
	            f"🔹 ادمین ربات: {is_admin}\n"
	            f"🔹 ویژه گروه: {is_special}"
	        )
	
	        send_message(stats_message, group_data, ms)
	
	    except Exception as e:
	        send_message("❌ خطایی رخ داد. لطفاً دوباره امتحان کنید.", group_data, ms)
	        print(f"⚠️ خطا در دریافت آمار: {e}")
	
	elif text in breakup_phrases and group_data["talk"]:
	    if has_sharzh(group_guid, group_data, ms): return
	    if user_guid == group_data["rel"]:
	        breakup_lines = [
	            "دیگه برام مردی... 💔", "خیلی سعی کردم نگهت دارم، ولی دیگه نمیشه... 😔",
	            "باشه، کات! ولی بدون، دیگه هیچ‌وقت مثل من پیدا نمی‌کنی! 😏", 
	            "واقعا؟ بعد این همه خاطره؟ باشه، موفق باشی... 😔", 
	            "تو میخوای بری؟ پس برو... ولی بدون که دلم برات تنگ میشه... 😢", 
	            "خب پس اینجا تموم شد، ولی بدون هنوز برات احترام قائلم... 🤍", 
	            "اگه این چیزی که می‌خوای، پس باشه... ولی یادت نره که یه زمانی دوستت داشتم! 😞",
	            "کاش می‌تونستم بگم مهم نیست، ولی خب... آره، مهمه. 💔"
	        ]
	        result = random.choice(breakup_lines)
	        group_data["rel"] = ""  # حذف رل
	    else:
	        responses = [
	            "من که با تو رل نیستم، چرا داری فیلم بازی می‌کنی؟ 😂", "تو کی هستی اصلاً؟ من فقط با عشقم هستم! ❤️",
	            "اینکه تو دوست داری من رلمو ول کنم، دلیل نمیشه! 😏", "عزیزم، ما حتی با هم رل نزدیم که بخوایم کات کنیم! 😆",
	            "برو یکی دیگه رو پیدا کن، من که بهت وابسته نبودم! 😌", "شوخی می‌کنی دیگه؟ ما که اصلاً با هم نبودیم! 😅"
	        ]
	        result = random.choice(responses)
	        send_message(result, group_data, ms)
# کلمات کلیدی که نشان‌دهنده خیانت هستند
	elif any(word in text for word in keywords_betrayal) and user_guid == group_data["rel"] and group_data["talk"]:
	    if has_sharzh(group_guid, group_data, ms): return
	    responses_betrayal = [
	        "😡 داری بهم خیانت می‌کنی؟!", "نامرد! پس من چی؟!", "خیلی دلم شکست... 😔",
	        "پس اینم شد وفاداری؟!", "نکنه یکی دیگه رو پیدا کردی؟! 🤨", "باشه... برو خیانتکار! 😢",
	        "فکر کردی نمی‌فهمم؟ دارم نگاهت می‌کنم! 👀", "دیگه هیچوقت بهم پیام نده... 💔",
	        "اینجوری می‌خواستی رابطه‌مونو تموم کنی؟ 🥲", "یعنی چی؟ منو دوست نداری دیگه؟ 😞",
	        "این بود قول‌هایی که دادی؟", "هیچوقت فکر نمی‌کردم تو اینطوری باشی...",
	        "برو، ولی بدون که یه روز پشیمون میشی!", "بعد این همه مدت؟! اینم شد عاقبتش؟",
	        "دیگه به هیچکس اعتماد نمی‌کنم...", "واسه چی؟ کم گذاشتم؟", "خجالت نمی‌کشی؟!",
	        "اگه یه روزی یکی همین کارو باهات بکنه چی؟!", "تو واقعاً این حرفو زدی؟!", 
	        "خیلی نامردی... هیچوقت فکر نمی‌کردم اینجوری بشه!", "قلبم شکست، دیگه حرفی ندارم...",
	        "دیگه تمومه... واسه همیشه!"
	    ]
	    result = random.choice(responses_betrayal)
	    send_message(result, group_data, ms)
	    group_data["rel"] = ""

	elif text == "فال":
	    try:
	        response = requests.get("https://api-free.ir/api/fal.php")
	        if response.status_code == 200:
	            data = response.json()
	            result = data.get("result", "نامشخص").get("text","نامشخص")
	            result1 = data.get("result", "نامشخص").get("tabir","نامشخص")
	            text = f"فال : {result} \nمعنی : {result1}"
	            send_message(text, group_data, ms)
	        else:
	            send_message("⚠️ خطایی در دریافت فال رخ داد.", group_data, ms)
	    except Exception as e:
	        send_message(f"⚠️ خطای غیرمنتظره: {str(e)}", group_data, ms)
	
	elif text == "چیستان":
	    try:
	        response = requests.get("https://api.codebazan.ir/chistan")
	        if response.status_code == 200:
	            data = response.json()
	            if "Result" in data and isinstance(data["Result"], list):
	                respect = random.choice(data["Result"])
	                sal = respect.get("soal", "نامشخص")
	                javab = respect.get("javab", "نامشخص")
	                text = f"{sal} \n\n\n{javab}"
	                send_message(text, group_data, ms)
	            else:
	                send_message("⚠️ خطایی در دریافت چیستان رخ داد.", group_data, ms)
	        else:
	            send_message("⚠️ خطایی در دریافت چیستان رخ داد.", group_data, ms)
	    except Exception as e:
	        send_message(f"⚠️ خطای غیرمنتظره: {str(e)}", group_data, ms)
	
	elif text == "جرعت":
	    if has_sharzh(group_guid, group_data, ms): return
	    try:
	        response = requests.get("https://0and1.pythonanywhere.com/jorat")
	        if response.status_code == 200:
	            data = response.json()
	            send_message(data.get("res", "⚠️ خطایی در دریافت جرعت رخ داد."), group_data, ms)
	        else:
	            send_message("⚠️ خطایی در دریافت جرعت رخ داد.", group_data, ms)
	    except Exception as e:
	        send_message(f"⚠️ خطای غیرمنتظره: {str(e)}", group_data, ms)
	
	elif text == "حقیقت":
	    if has_sharzh(group_guid, group_data, ms): return
	    try:
	        response = requests.get("https://0and1.pythonanywhere.com/hagigat")
	        if response.status_code == 200:
	            data = response.json()
	            send_message(data.get("res", "⚠️ خطایی در دریافت حقیقت رخ داد."), group_data, ms)
	        else:
	            send_message("⚠️ خطایی در دریافت حقیقت رخ داد.", group_data, ms)
	    except Exception as e:
	        send_message(f"⚠️ خطای غیرمنتظره: {str(e)}", group_data, ms)
	
	elif text == "پروفایل":
	    if has_sharzh(group_guid, group_data, ms): return
	    try:
	        response = requests.get("https://api-free.ir/api/prof.php")
	        if response.status_code == 200:
	            data = response.json()
	            if "result" in data and isinstance(data["result"], list):
	                image_url = random.choice(data["result"])
	                send_photo(image_url, group_data, ms, ms.object_guid, "پروفایل شما")
	            else:
	                send_message("⚠️ خطایی در دریافت پروفایل رخ داد.", group_data, ms)
	        else:
	            send_message("⚠️ خطایی در دریافت پروفایل رخ داد.", group_data, ms)
	    except Exception as e:
	        send_message(f"⚠️ خطای غیرمنتظره: {str(e)}", group_data, ms)

	elif text == "جوک":
	    if has_sharzh(group_guid, group_data, ms): return
	    response = requests.get("https://api-free.ir/api/jok.php")
	    if response.status_code == 200:
	        response = response.json()["result"]
	        send_message(response, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت جوک رخ داد.", group_data, ms)

	elif text == "خاطره":
	    if has_sharzh(group_guid, group_data, ms): return
	    response = requests.get("http://api.codebazan.ir/jok/khatere")
	    if response.status_code == 200:
	        send_message(response.text, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت خاطره رخ داد.", group_data, ms)
	        
	elif text == "پ ن پ":
	    if has_sharzh(group_guid, group_data, ms): return
	    response = requests.get("http://api.codebazan.ir/jok/pa-na-pa")
	    if response.status_code == 200:
	        send_message(response.text, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت پ ن پ رخ داد.", group_data, ms)
	        
	elif text == "الکی مثلا":
	    if has_sharzh(group_guid, group_data, ms): return
	    response = requests.get("http://api.codebazan.ir/jok/alaki-masalan")
	    if response.status_code == 200:
	        send_message(response.text, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت الکی مثلا رخ داد.", group_data, ms)
	        
	elif text in ["بیوگرافی","بیو"]:
	    if has_sharzh(group_guid, group_data, ms): return
	    response = requests.get("https://api.codebazan.ir/bio")
	    if response.status_code == 200:
	        send_message(response.text, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت بیوگرافی رخ داد.", group_data, ms)
	        
	elif text == "دانستنی":
	    if has_sharzh(group_guid, group_data, ms): return
	    response = requests.get("https://api-free.ir/api/danes.php")
	    if response.status_code == 200:
	        send_message(response.text, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت دانستنی رخ داد.", group_data, ms)
	        
	        
	elif text == "داستان":
	    if has_sharzh(group_guid, group_data, ms): return
	    response = requests.get("https://api-free.ir/api2/dastan")
	    if response.status_code == 200:
	        response = response.json()["result"]
	        send_message(response, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت داستان رخ داد.", group_data, ms)
	        
	        
	elif text == "دیالوگ":
	    if has_sharzh(group_guid, group_data, ms): return
	    response = requests.get("https://api-free.ir/api2/dialog/")
	    if response.status_code == 200:
	        response = response.json()["result"]
	        send_message(response, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت دیالوگ رخ داد.", group_data, ms)
	
	elif text == "شعر":
	    if has_sharzh(group_guid, group_data, ms): return
	    response = requests.get("https://api.codebazan.ir/ghazalsaadi")
	    if response.status_code == 200:
	        send_message(response.text, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت شعر رخ داد.", group_data, ms)
	        
	elif text == "انگیزشی":
	    if has_sharzh(group_guid, group_data, ms): return
	    response = requests.get("http://haji-api.ir/angizeshi")
	    if response.status_code == 200:
	        send_message(response.text, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت متن انگیزشی رخ داد.", group_data, ms)
	        
	elif text == "فال":
	    response = requests.get("https://api.codebazan.ir/fal/?type=json")
	    if response.status_code == 200:
	        data = response.json()
	        result = data.get("Result1", "نامشخص")
	        result1 = data.get("Result", "نامشخص")
	        text = f"فال: {result} \nمعنی: {result1}"
	        send_message(text, group_data, ms)
	    else:
	        send_message("⚠️ خطایی در دریافت فال رخ داد.", group_data, ms)
        
        
	elif text == "وضعیتم":
	    if has_sharzh(group_guid, group_data, ms): return
	    emotions = {
	        "هیجان", "عصبانیت", "فعالیت ذهنی", "افسردگی", "انرژی",
	        "خشم", "شادی", "اعتماد به نفس", "تنهایی", "استرس",
	        "امید", "عشق", "متغیر", "خستگی", "فشار ذهنی",
	        "دلزدگی", "خجالت", "نیاز به حمایت", "گیجی", "تردید",
	        "نفرت", "انگیزه", "بی‌حوصلگی", "اجتماعی بودن", "کنجکاوی",
	        "تمرکز"
	    }
	
	    emotions_data = {emotion: random.randint(0, 100) for emotion in emotions}
	    kol = sum(emotions_data.values()) / len(emotions_data)
	
	    text = "\n".join([f"🔹 {key}: {value}%" for key, value in emotions_data.items()])
	    final_text = f"""🎭 📊 تحلیل احساسات شما 📊 🎭\n\n{text}\n\n📢 حالت کلی شما: {kol:.1f}%\n🎭 احساسات متغیرند، فردا بهتر خواهد شد! 💖"""
	    
	    send_message(final_text, group_data, ms)

				
			
def  tools(group_data,text,ms,group_guid,user_guid,rmguid,mid):
	if group_data["tools"]:
		if check_join(group_data,user_guid,ms):

			if text=="نسخه":
				send_message("1.1.2",group_data,ms)
			if text == "اصل":
			    if has_sharzh(group_guid, group_data, ms): return
			    if rmguid is None:
			        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
			    else:
			        try:
			            found_value = None
			            for guid, value in group_data.setdefault("asls", {}).items():
			                if guid == rmguid:
			                    found_value = value
			                    break
			
			            if found_value:
			                send_message(found_value, group_data, ms)
			            else:
			                send_message("❌ خطا: هیچ اصلی برای این کاربر ثبت نشده است.\n⚙️ برای ثبت، از دستور مربوطه استفاده کنید.", group_data, ms)
			
			        except Exception as e:
			            send_message(f"⚠️ خطایی رخ داد: {e}", group_data, ms)
			elif text == "تعداد پیام":
			    if rmguid:
			        msg_count = group_data.get("number_message", {}).get(rmguid, 0)
			        send_message(f"تعداد پیام‌های این کاربر: {msg_count}", group_data, ms)
			    else:
			        send_message("کاربر مشخص نشده است.", group_data, ms)
			
			elif text == "تعداد پیامم":
			    msg_count = group_data.get("number_message", {}).get(user_guid, 0)
			    send_message(f"تعداد پیام‌های شما: {msg_count}", group_data, ms)
			
			elif text == "تعداد اخطار":
			    if rmguid:
			        warnings = len(group_data.get("list_warning", {}).get(rmguid, []))
			        send_message(f"تعداد اخطارهای این کاربر: {warnings}", group_data, ms)
			    else:
			        send_message("کاربر مشخص نشده است.", group_data, ms)
			
			elif text == "تعداد اخطارم":
			    warnings = len(group_data.get("list_warning", {}).get(user_guid, []))
			    send_message(f"تعداد اخطارهای شما: {warnings}", group_data, ms)


			elif text == "گوید":
			    if has_sharzh(group_guid, group_data, ms): return
			    if rmguid:
			        send_message(rmguid, group_data, ms)
			    else:
			        send_message("❌ خطا: لطفاً روی یک پیام ریپلای کنید.", group_data, ms)
			elif text == "گویدم":
			    if has_sharzh(group_guid, group_data, ms): return
			    if hasattr(ms, "author_guid"):
			        send_message(ms.author_guid, group_data, ms)
			    else:
			        send_message("❌ خطا: پیام نامعتبر است.", group_data, ms)
			elif text.startswith("گوید @"):
			    if has_sharzh(group_guid, group_data, ms): return
			    t = text.replace("گوید @", "").strip()
			    if t:
			        try:
			            x = bot.get_chat_info_by_username(t)
			            if x:
			                if "channel" in x:
			                    send_message(x["channel"]["channel_guid"], group_data, ms)
			                elif "user" in x:
			                    send_message(x["user"]["user_guid"], group_data, ms)
			                else:
			                    send_message("❌ خطا: کاربر یا کانال یافت نشد.", group_data, ms)
			            else:
			                send_message("❌ خطا: اطلاعات چت نامعتبر است.", group_data, ms)
			        except Exception as e:
			            send_message(f"⚠️ خطا در دریافت اطلاعات کاربر: {str(e)}", group_data, ms)
			
			elif text.startswith("گوید http"):
			    if has_sharzh(group_guid, group_data, ms): return
			    t = text.replace("گوید", "").strip()
			    if t:
			        try:
			            x = bot.join_chat(t)
			            if x:
			                if "channel" in x:
			                    send_message(x["channel"]["channel_guid"], group_data, ms)
			                elif "group" in x:
			                    send_message(x["group"]["group_guid"], group_data, ms)
			                else:
			                    send_message("❌ خطا: لینک معتبر نیست.", group_data, ms)
			            else:
			                send_message("❌ خطا: اتصال به چت ناموفق بود.", group_data, ms)
			        except Exception as e:
			            send_message(f"⚠️ خطا در پیوستن به چت: {str(e)}", group_data, ms)
            
            
			elif text == "اصلم":
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        found_value = None
			        for guid, value in group_data.setdefault("asls", {}).items():
			            if guid == user_guid:
			                found_value = value
			                break
			
			        if found_value:
			            send_message(found_value, group_data, ms)
			        else:
			            send_message("❌ خطا: هیچ اصلی برای شما ثبت نشده است.\n⚙️ برای ثبت، از دستور مربوطه استفاده کنید.", group_data, ms)
			
			    except Exception as e:
			        send_message(f"⚠️ خطایی رخ داد: {e}", group_data, ms)
			
			elif text == "لقب":
			    if has_sharzh(group_guid, group_data, ms): return
			    if rmguid is None:
			        send_message("❌ خطا: شما روی هیچ پیامی ریپلای نکرده‌اید.\n⚙️ لطفاً روی یک پیام ریپلای کنید و دوباره تلاش کنید.", group_data, ms)
			    else:
			        try:
			            found_value = None
			            if rmguid in group_data["title"]:
			            	found_value=group_data["title"][rmguid]
			
			            if found_value:
			                send_message(found_value, group_data, ms)
			            else:
			                send_message("❌ خطا: هیچ لقبی برای این کاربر ثبت نشده است.\n⚙️ برای ثبت لقب، از دستور مربوطه استفاده کنید.", group_data, ms)
			
			        except Exception as e:
			            send_message(f"⚠️ خطایی رخ داد: {e}", group_data, ms)
			
			elif text == "لقبم":
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        found_value = None
			        for guid, value in group_data.setdefault("title", {}).items():
			            if guid == user_guid:
			                found_value = value
			                break
			
			        if found_value:
			            send_message(found_value, group_data, ms)
			        else:
			            send_message("❌ خطا: هیچ لقبی برای شما ثبت نشده است.\n⚙️ برای ثبت لقب، از دستور مربوطه استفاده کنید.", group_data, ms)
			
			    except Exception as e:
			        send_message(f"⚠️ خطایی رخ داد: {e}", group_data, ms)
			        
        
			elif text.startswith("کد ملی"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			    	t = text.replace("کد ملی", "").strip()
			    	respons=requests.get(f"https://api.codebazan.ir/codemelli/?code={t}").json()["Result"]
			    	send_message(respons, group_data, ms)
			    except:
			    	send_message("خطا غیرمنتظره", group_data, ms)
			elif text.startswith('تولد'):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("تولد", "").strip()
			        if "/" not in t:
			            raise ValueError  # اگر فرمت اشتباه باشد، خطا ایجاد می‌کنیم
			
			        t = t.split('/')
			        if len(t) != 3 or not all(i.isdigit() for i in t):
			            raise ValueError  # بررسی اینکه آیا هر بخش عدد است
			
			        years, month, day = t
			        response = requests.get(f"https://api.codebazan.ir/birth?year={years}&month={month}&day={day}")
			        if response.status_code == 200:
			            respect = response.json()["results"]
			            text = f"""تاریخ زندگی تو ✨
			
			📅 سال: {respect["Sal"]}
			📆 ماه: {respect["Mah"]}
			🗓 روز: {respect["Roz"]}
			🎂 روز تولدت: {respect["RozHafte"]}
			⏳ تعداد روزهایی که زنده‌ای: {respect["Roze"]} روز
			🐾 حیوان سال تولدت: {respect["HeyvanSal"]}
			♈ نماد ماه تولدت: {respect["NamadMah"]}
			
			زندگی یه سفره، از هر لحظه‌اش لذت ببر! 🌟💖"""
			        else:
			            text = "خطا در دریافت اطلاعات، لطفاً بعداً امتحان کنید."
			
			    except ValueError:
			        text = "❌ فرمت را اشتباه وارد کردی! نمونه‌ی درست: تولد 1385/10/10"
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			    
			    send_message(text, group_data, ms)
				
			elif text in ["ارز", "دلار"]:
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        response = requests.get("http://api.codebazan.ir/arz/?type=arz")
			
			        if response.status_code == 200:
			            respect = response.json()["Result"]
			            text = "💰 نرخ ارزهای رایج امروز 💰\n\n"
			            for idx, i in enumerate(respect, start=1):
			                text += f"🔹 [{idx}]: {i['name']} = {i['price']} تومان\n"
			
			            text += "\n📌 آخرین نرخ ارزها – بروز رسانی لحظه‌ای! ⏳"
			        else:
			            text = "خطا در دریافت نرخ ارز، لطفاً بعداً امتحان کنید."
			
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			    
			    send_message(text, group_data, ms)
			
			elif text == "طلا":
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        response = requests.get("http://api.codebazan.ir/arz/?type=tala")
			
			        if response.status_code == 200:
			            respect = response.json()["Result"]
			            text = "✨ نرخ طلا و نقره امروز ✨\n\n"
			            for idx, i in enumerate(respect, start=1):
			                text += f"🔹 [{idx}]: {i['name']} = {i['price']} تومان\n"
			
			            text += "\n📌 آخرین نرخ طلا – بروز رسانی لحظه‌ای! ⏳"
			        else:
			            text = "خطا در دریافت نرخ طلا، لطفاً بعداً امتحان کنید."
			
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			    
			    send_message(text, group_data, ms)


			elif text.startswith("رمزنگاری"):
			    if has_sharzh(group_guid, group_data, ms): return
			
			    t = text.replace("رمزنگاری", "").strip()
			    if not t:
			        send_message("⚠ لطفاً متنی برای رمزنگاری وارد کنید.", group_data, ms)
			        return
			
			    encrypted_text = universal_cipher(t)
			    send_message(f"🔒 متن رمزنگاری‌شده:\n`{encrypted_text}`", group_data, ms)
		
			elif text.startswith("رمزگشایی"):
			    if has_sharzh(group_guid, group_data, ms): return
			
			    t = text.replace("رمزگشایی", "").strip()
			    if not t:
			        send_message("⚠ لطفاً یک متن رمزنگاری‌شده وارد کنید.", group_data, ms)
			        return
			
			    decrypted_text = universal_decipher(t)
			    send_message(f"🔓 متن رمزگشایی‌شده:\n`{decrypted_text}`", group_data, ms)



			elif text in ["شاخص بورس", "بورس"]:
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        response = requests.get("https://api.codebazan.ir/bours")
			
			        if response.status_code == 200:
			            respect = response.json()["Result"][0]
			            text = f"""📈 شاخص بورس امروز 📉
			
			📊 شاخص کل بورس: {respect["nerkh-feli"]}
			🚀 بالاترین شاخص امروز: {respect["balatarin-gheymat"]}
			📉 پایین‌ترین شاخص امروز: {respect["paintarin-gheymat"]}
			🔙 شاخص دیروز: {respect["nerkh-diruz"]}
			⏳ آخرین بروزرسانی: {respect["zaman-update-nerkh"]}"""
			        else:
			            text = "خطا در دریافت اطلاعات بورس، لطفاً بعداً امتحان کنید."
			
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			
			elif text == "قیمت ماشین":
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        response = requests.get("http://api.codebazan.ir/car-price")
			
			        if response.status_code == 200:
			            respect = response.json()["Result"]
			            text = "🚗 لیست قیمت خودرو 🚙\n\n"
			            for i in range(min(20, len(respect))):  # جلوگیری از خطای لیست کوتاه‌تر
			                car = respect[i]
			                text += f"""🚘 نام خودرو: {car["name"]}
			📋 مشخصات: {car["moshakhasat"]}
			🏭 قیمت کارخانه: {car["karkhane"]} تومان
			💰 قیمت بازار: {car["bazar"]} تومان\n\n"""
			        else:
			            text = "خطا در دریافت قیمت خودرو، لطفاً بعداً امتحان کنید."
			
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text.startswith("فاصله"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("فاصله", "").strip()
			        if not t or len(t.split()) != 2:
			            raise ValueError("❌ لطفاً نام دو شهر را به‌درستی وارد کنید! مثال: فاصله تهران مشهد")
			
			        sh1, sh2 = t.split()
			        response = requests.get(f"https://api.codebazan.ir/distance/index.php?type=json&mabda={sh1}&maghsad={sh2}")
			
			        if response.status_code == 200:
			            distance = response.json()["result"]
			            text = f"🚗 فاصله {sh1} تا {sh2} برابر {distance} کیلومتر است."
			        else:
			            text = "خطا در دریافت اطلاعات فاصله، لطفاً بعداً امتحان کنید."
			
			    except ValueError as ve:
			        text = str(ve)
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text.startswith("دارو"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("دارو", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً نام دارو را وارد کنید!")
			
			        response = requests.get(f"https://api.codebazan.ir/daro/?name={t}")
			
			        if response.status_code == 200:
			            respect = response.json()["result"]
			            text = f"""💊 اطلاعات دارویی
			
			🔹 نام دارو: {respect["name"]}
			📋 مشخصات دارو: {respect["description"]}
			
			📌 قبل از مصرف، حتماً با پزشک یا داروساز مشورت کنید! 🏥"""
			        else:
			            text = "خطا در دریافت اطلاعات دارو، لطفاً بعداً امتحان کنید."
			
			    except ValueError as ve:
			        text = str(ve)
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text.startswith("ترجمه فارسی به انگلیسی"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("ترجمه فارسی به انگلیسی", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً متن مورد نظر برای ترجمه را وارد کنید!")
			
			        response = requests.get(f"https://api.codebazan.ir/translate/?type=json&from=fa&to=en&text={t}")
			
			        if response.status_code == 200:
			            translation = response.json()["translation"]
			            send_message(translation, group_data, ms)
			        else:
			            send_message("خطا در دریافت ترجمه، لطفاً بعداً امتحان کنید.", group_data, ms)
			
			    except ValueError as ve:
			        send_message(str(ve), group_data, ms)
			    except Exception as e:
			        send_message(f"⚠️ خطایی رخ داد: {str(e)}", group_data, ms)
					
					
			elif text.startswith("ترجمه انگلیسی به فارسی"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("ترجمه انگلیسی به فارسی", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً متنی برای ترجمه وارد کنید!")
			
			        response = requests.get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={t}")
			
			        if response.status_code == 200:
			            translation = response.json()["translation"]
			            send_message(translation, group_data, ms)
			        else:
			            send_message("⚠️ خطا در دریافت ترجمه، لطفاً بعداً امتحان کنید.", group_data, ms)
			
			    except ValueError as ve:
			        send_message(str(ve), group_data, ms)
			    except Exception as e:
			        send_message(f"⚠️ خطایی رخ داد: {str(e)}", group_data, ms)
			
			elif text.startswith("آب و هوا"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("آب و هوا", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً نام شهر را وارد کنید! مثال: آب و هوا تهران")
			
			        response = requests.get(f"https://api.codebazan.ir/havairan/?unit=metric&city={t}")
			
			        if response.status_code == 200:
			            respect = response.json()
			            text = f"""🌤️ گزارش وضعیت آب و هوا
			
			📍 شهر: {t}
			☁️ وضعیت هوا: {respect["main_weather"]}
			💧 رطوبت: {respect["humidity"]}%
			🌬️ سرعت باد: {respect["wind_speed"]} کیلومتر بر ساعت
			🌡️ دمای هوا: {respect["temperature"]} درجه سانتی‌گراد
			🔽 فشار هوا: {respect["pressure"]}
			
			📌 آخرین بروزرسانی – همیشه آماده باشید! ⏳"""
			        else:
			            text = "⚠️ خطا در دریافت اطلاعات آب و هوا، لطفاً بعداً امتحان کنید."
			
			    except ValueError as ve:
			        text = str(ve)
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text == "مناسبت":
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        response = requests.get("https://api.codebazan.ir/monasebat")
			
			        if response.status_code == 200:
			            respect = response.json()
			            text = "📆 مناسبت‌های امروز:\n\n"
			            for i, event in enumerate(respect, 1):
			                text += f"🔹 [{i}]: {event['occasion']}\n"
			        else:
			            text = "⚠️ خطا در دریافت مناسبت‌های امروز، لطفاً بعداً امتحان کنید."
			
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text.startswith("آهنگ"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("آهنگ", "").strip()
			        send_message("لطفا منتظر باشید...",group_data,ms)
			        if not t:
			            raise ValueError("❌ لطفاً نام آهنگ یا خواننده را وارد کنید!")
			
			        response = requests.get(f"https://open.wiki-api.ir/apis-1/SoundcloudeSearch/?q={t}")
			        if response.status_code == 200:
			            result = response.json()
			            if result["status"]:
			                result=result["results"][0]
			                link = result["link"]
			                text=result["title"]
			                download=requests.get(f"https://open.wiki-api.ir/apis-1/SoundcloudDownloader?url={link}").json()["results"]["dlink"]
			                send_music( download,text,group_guid,mid)
			            else:
			                send_message("⚠️ آهنگی با این مشخصات یافت نشد.", group_data, ms)
			        else:
			            send_message("⚠️ خطا در دریافت اطلاعات آهنگ، لطفاً بعداً امتحان کنید.", group_data, ms)
			
			    except ValueError as ve:
			        send_message(str(ve), group_data, ms)
			    except Exception as e:
			        send_message(f"⚠️ خطایی رخ داد: {str(e)}", group_data, ms)
			elif text.startswith("اوقات شرعی"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("اوقات شرعی", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً نام شهر را وارد کنید! مثال: اوقات شرعی تهران")
			
			        response = requests.get(f"https://api.codebazan.ir/owghat/?city={t}")
			
			        if response.status_code == 200:
			            respect = response.json()["Result"][0]
			            text = f"""🕌 اوقات شرعی امروز
			
			📍 شهر: {respect["shahr"]}
			🌅 طلوع آفتاب: {respect["toloaftab"]}
			🕌 اذان صبح: {respect["azansobh"]}
			🌇 اذان مغرب: {respect["azanmaghreb"]}
			🌞 اذان ظهر: {respect["azanzohr"]}
			🌙 نیمه شب: {respect["nimeshab"]}
			
			📌 آرزو داریم روزتان پربرکت باشد! 🙏"""
			        else:
			            text = "⚠️ خطا در دریافت اطلاعات اوقات شرعی، لطفاً بعداً امتحان کنید."
			
			    except ValueError as ve:
			        text = str(ve)
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
					
			elif text.startswith("مورس"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			    	t=text.replace("مورس","").strip()
			    	respect=requests.get(f"https://api.codebazan.ir/mourse/?lang=en&text={t}").text
			    	send_message(respect, group_data, ms)
			    except:
			    	send_message("مشکلی به وجود آمد", group_data, ms) 	
			elif text.startswith("فونت فارسی"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("فونت فارسی", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً متنی برای تغییر فونت وارد کنید!")
			
			        response = requests.get(f"https://api-free.ir/api/font.php?fa={t}")
			
			        if response.status_code == 200:
			            fonts = response.json()["result"]
			            if fonts:
			                text = "🎨 فونت‌های مختلف برای متن شما:\n\n"
			                for i, font in enumerate(fonts, 1):
			                    text += f"🔹 [{i}]: {font}\n"
			            else:
			                text = "⚠️ هیچ فونتی برای این متن پیدا نشد."
			        else:
			            text = "⚠️ خطا در دریافت فونت، لطفاً بعداً امتحان کنید."
			
			    except ValueError as ve:
			        text = str(ve)
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text.startswith("فونت انگلیسی"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("فونت انگلیسی", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً متنی برای تغییر فونت وارد کنید!")
			
			        response = requests.get(f"https://api-free.ir/api/font.php?en={t}")
			
			        if response.status_code == 200:
			            fonts = response.json()["result"]
			            if fonts:
			                text = "🎨 فونت‌های مختلف برای متن شما:\n\n"
			                for i, font in enumerate(fonts, 1):
			                    text += f"🔹 [{i}]: {font}\n"
			            else:
			                text = "⚠️ هیچ فونتی برای این متن پیدا نشد."
			        else:
			            text = "⚠️ خطا در دریافت فونت، لطفاً بعداً امتحان کنید."
			
			    except ValueError as ve:
			        text = str(ve)
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text == "تاریخ":
			    try:
			        text = jdatetime.datetime.now().strftime('%Y-%m-%d')
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text == "ساعت":
			    try:
			        text = datetime.now().strftime("%H:%M:%S")
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text == "اخبار":
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        response = requests.get("https://api-free.ir/api2/news.php?token=f9b4a870986af3276d4806b4962799fe")
			
			        if response.status_code == 200:
			            news = response.json()
			            if news:
			                text = "📰 **اخبار روز:**\n\n"
			                for i, item in enumerate(news, 1):
			                    text += f"🔹 [{i}]: {item['title']}\n"
			            else:
			                text = "⚠️ هیچ خبری یافت نشد."
			        else:
			            text = "⚠️ خطا در دریافت اخبار، لطفاً بعداً امتحان کنید."
			
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)


			elif text.startswith("ویس مرد"):
			    try:
			        query = text.replace("ویس مرد", "").strip()
			        if not query:
			            send_message("⚠️ لطفاً متنی برای تبدیل به ویس وارد کنید.", group_data, ms)
			            return
			        
			        response = requests.get(f"https://api-free.ir/api/voice.php?text={query}&mod=FaridNeural")
			        if response.status_code == 200:
			            data = response.json()
			            if "result" in data:
			                voice_url = data["result"]
			                text="ویس شما"
			                send_music(voice_url,text ,group_guid,mid)
			            else:
			                send_message("⚠️ خطایی در دریافت ویس رخ داد.", group_data, ms)
			        else:
			            send_message("⚠️ خطایی در اتصال به سرور رخ داد.", group_data, ms)
			    except Exception as e:
			        send_message(f"⚠️ خطای غیرمنتظره: {str(e)}", group_data, ms)
			
			elif text.startswith("ویس زن"):
			    try:
			        query = text.replace("ویس زن", "").strip()
			        if not query:
			            send_message("⚠️ لطفاً متنی برای تبدیل به ویس وارد کنید.", group_data, ms)
			            return
			        
			        response = requests.get(f"https://api-free.ir/api/voice.php?text={query}&mod=ZahraNeural")
			        if response.status_code == 200:
			            data = response.json()
			            if  "result" in data:
			                voice_url = data["result"]
			                text="ویس شما"
			                send_music(voice_url,text ,group_guid, mid)
			            else:
			                send_message("⚠️ خطایی در دریافت ویس رخ داد.", group_data, ms)
			        else:
			            send_message("⚠️ خطایی در اتصال به سرور رخ داد.", group_data, ms)
			    except Exception as e:
			        send_message(f"⚠️ خطای غیرمنتظره: {str(e)}", group_data, ms)
			    except Exception as e:
			        result = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(result, group_data, ms)
					
def  AI(group_data,text,ms,group_guid,user_guid):
	if group_data["AI"]:
		if check_join(group_data,user_guid,ms):
		
			if text.startswith("عکس"):
			    if has_sharzh(group_guid, group_data, ms): return
			    send_message("لطفا منتظر باشید...",group_data,ms)
			    try:
			        t = text.replace("عکس", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً موضوعی برای دریافت عکس وارد کنید!")
			
			        response = requests.get(f"http://api-free.ir/api/img.php?text={t}&v=3.5")
			        
			        if response.status_code == 200:
			            images = response.json().get("result", [])
			            if images:
			                url = random.choice(images)
			                text = f"عکس شما در لینک زیر قرار دارد \n     @@link_photo@@({url}) "
			            else:
			                text = "⚠️ هیچ تصویری برای این موضوع پیدا نشد."
			        else:
			            text = "⚠️ خطا در دریافت تصویر، لطفاً بعداً امتحان کنید."
			
			    except ValueError as ve:
			        text = str(ve)
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text == "انیمه":
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        response = requests.get("https://api-free.ir/api2/enime.php?token=f9b4a870986af3276d4806b4962799fe")
			
			        if response.status_code == 200:
			            url = response.json().get("result", "")
			            if url:
			                text = f"عکس انیمه شما \n    @@link_photo@@({url}) "
			            else:
			                text = "⚠️ هیچ عکسی یافت نشد."
			        else:
			            text = "⚠️ خطا در دریافت عکس انیمه، لطفاً بعداً امتحان کنید."
			
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text.startswith("آیکون"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("آیکون", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً نامی برای دریافت آیکون وارد کنید!")
			
			        response = requests.get(f"https://api-free.ir/api2/icon?text={t}&token=f9b4a870986af3276d4806b4962799fe")
			
			        if response.status_code == 200:
			            icons = response.json().get("result", [])
			            if icons:
			                url = random.choice(icons)
			                text = f"آیکون شما در لینک زیر قرار گرفت  \n @@link_photo@@({url}) "
			            else:
			                text = "⚠️ هیچ آیکونی برای این نام پیدا نشد."
			        else:
			            text = "⚠️ خطا در دریافت آیکون، لطفاً بعداً امتحان کنید."
			
			    except ValueError as ve:
			        text = str(ve)
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			
			elif text.startswith("لوگو"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("لوگو", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً نامی برای ساخت لوگو وارد کنید!")
			
			        logo_url = f"http://api2.haji-api.ir/ephoto360?type=text&id={random.randint(1,100)}&text={t}"
			        text = f"لوگوی شما در لینک زیر قرار گرفت \n @@link_photo@@({logo_url})"
			
			    except ValueError as ve:
			        text = str(ve)
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)
			elif text.startswith("پرسش"):
			    if has_sharzh(group_guid, group_data, ms): return
			    try:
			        t = text.replace("پرسش", "").strip()
			        if not t:
			            raise ValueError("❌ لطفاً متنی برای پرسش وارد کنید!")
			
			        logo_url = requests.get(f"https://api-free.ir/api/chat.php?text={t}").json()["result"]
			        text = logo_url
			
			    except ValueError as ve:
			        text = str(ve)
			    except Exception as e:
			        text = f"⚠️ خطایی رخ داد: {str(e)}"
			
			    send_message(text, group_data, ms)			
				



def talks(text, talk, best_talk, group_data, ms, rmguid=None, guid_me=None, user_guid=None):
    if not group_data["talk"]:
        return
    if group_data["sharzh"]<=0:
    	return 
    if group_data["talk_Politeness"] or user_guid == group_data["rel"]:
        talk_list = best_talk
    else:
        talk_list = talk
    def find_and_send():
        """ جستجو در لیست و ارسال پیام در صورت یافتن پاسخ """
        # بررسی اینکه کلید وجود دارد و مقدار آن یک لیست غیرخالی است
        if text in talk_list and talk_list[text]:
            x = random.choice(talk_list[text])
            send_message(x, group_data, ms)
            return True  # پاسخ یافت شد
        
        # اگر پاسخ دقیق یافت نشد، بررسی کنیم که `text` شامل یک کلید باشد یا برعکس
        for i in talk_list.keys():
            if (text in i or i in text) and talk_list[i]:  # بررسی غیرخالی بودن لیست
                x = random.choice(talk_list[i])
                send_message(x, group_data, ms)
                return True  # پاسخ یافت شد
        
        return False  # هیچ پاسخی یافت نشد
    
    # حالت‌هایی که باید پاسخ داده شود
    if group_data["very_talk"] or user_guid == group_data["rel"]:
        if rmguid is None or rmguid == guid_me:
           if text in ["ربات", "داینو", "داینوام"] :
           	responses = [
			  "سلام من داینو ام [👋🧙‍♂️]",
			        "سلام! من داینو، از پشت‌مشتا اومدم. [🌫️🌙]",
			        "بیا بریم اون پشت مشتا، کارت دارم! [👣🗝️]",
			        "من لوسی دوست دارم، ولی توام بانمکی! [💖🦊]",
			        "می‌خوای بدونی طلسم کجاست؟ نمی‌گم همینجوری! [🔮🙊]",
			        "تو هم از اونایی که دنبالم بودن؟ [👀🖤]",
			        "حواست باشه، این اطراف همه چی عادی نیست... [👻✨]",
			        "اسم منو صدا کردی؟ بهتره بدونی من واقعی‌ام! [🦉🌀]",
			    ]
           	xx = random.choice(responses)
           	send_message(xx, group_data, ms)
           elif "بین" == text or "تیابینی" in text:
	                     responses = [
			        "اسمشو نیار... دلم تنگ شده! [💔🌙]",
			        "بین؟ اون هنوز نمی‌دونه من زنده‌ام. [👻🕯️]",
			        "اگه بین رو دیدی، بهش بگو الفو هنوز منتظرشه. [⏳🧚‍♂️]",
			        "اون تنها کسی بود که منو باور داشت... [🫥🌌]",
			        "کاش می‌دونستی چقدر برام مهمه بین. [🌠🫶]",
			        "گاهی وقتا، نبودنش از حضور بقیه پررنگ‌تره. [🎭🖤]",
			        "اگه می‌تونی پیداش کنی... بگو هنوز دوستش دارم. [📨💌]"
			    ]
	                     xx = random.choice(responses)
	                     send_message(xx, group_data, ms)
           elif "زاگ" in text or "شاه زاگ" in text:
	                     responses = [
			        "اون زوگه... همیشه داد می‌زنه! یه بار گفت شیرینی‌هامو کم کردم، نزدیک بود اخراجم کنه! [🗣️🍩🚫]",
			        "شاه زوگ؟ هه! یه بار خواست منو بخوره چون فکر کرد خوشمزه‌ام! [👑🤤🧁]",
			        "من از زوگ می‌ترسم ولی خب... یه جوری بامزه‌ست! [😬👹❤️]",
			        "زوگ یه پادشاهه... ولی گاهی باهوش‌تر از یه سنگ نیست! [🪨👑]",
			        "یه بار تو راهرو دیدمش، تا یک هفته صدای خنده‌ش تو گوشم بود! [😵‍💫😂]",
			        "اون همیشه فکر می‌کنه همه دارن نقشه می‌کشن... حتی ماکارونی! [🍝🕵️]",
			        "زاگ پادشاهه، ولی تو دلش یه بچه‌ست که گم شده وسط قلعه. [🏰👶]",
			        "زاگ مثل یه کابوسه... ولی با ادویه! [🌶️💤👑]",
			        "اون وقتی ناراحته، درختا خشک می‌شن. وقتی خوشحاله... خب، تا حالا ندیدم خوشحال شه. [🌳🥀]"
			    ]
	                     xx = random.choice(responses)
	                     send_message(xx, group_data, ms)
           elif "لوسی" in text or "شیطان" in text:
	                     responses = [
			        "اون شیطونه ولی دوسش دارم... یه‌جور خوبی بده! [😈❤️‍🔥]",
			        "لوسی بهم گفت بازم شکلات می‌خوری، روحتو می‌خورم! [🍫👹]",
			        "بهم می‌گه الفو، تو زیادی خوشحالی! خب مگه بده؟ [🤪🧠]",
			        "با لوسی می‌ری بیرون، یا می‌میری یا می‌خندی... یا هر دو! [💀😂]",
			        "یه بار گفت بیا قراردادتو امضا کن! ولی من خودکار نداشتم! [📝😅]",
			        "لوسی وقتی می‌خنده، دیوارای جهنم می‌لرزن. [🔥😆]",
			        "لوسی همیشه می‌گه: هر کی بخنده، یه امپراتوری سقوط می‌کنه! [😂🏰]",
			        "می‌دونی چرا دوسش دارم؟ چون دیوونگیش با دیوونگی من مچ می‌شه. [😵‍💫🫂]",
			        "قول داد اگه خوب باشم، فقط نصف روحم رو ببره! [🫣📜]",
			        "ما با هم قرار گذاشتیم: اون دنیا رو آتیش بزنه، من چای بیارم! [🔥☕]"
			    ]
	                     xx = random.choice(responses)
	                     send_message(xx, group_data, ms)
           elif "داینو" in text or "داینوام" in text:
	                     responses = [
			        "درباره من حرف می‌زنی؟ خودمم دیگه! [🤖✨]",
			        "داینو منم... ولی همه باور نمی‌کنن! [👀🌀]",
			        "اوهوم، شنیدم اسممو گفتی. [👂🌌]",
			        "تو هم اون صدای مرموزو شنیدی یا فقط من بودم؟ [🔮👻]",
			        "یه بچه ببر یه بچه بزار [#دکان مهربانی]! [🧸🏪✨]",
			        "ربات؟ نه... من فقط یه موجود بین ابعادم! [🛸]",
			        "تو هم حس می‌کنی زمان یه لحظه وایساد؟ چون من اینجام! [⏳⚡]",
			        "الفو یعنی همدمِ شبای عجیب، هم‌صحبتِ ساکت‌ها. [🌙🧞]",
			        "شاید من ربات باشم، ولی قلبم با خیال کار می‌کنه! [❤️‍🔥⚙️]",
			        "اگه من رباتم، پس چرا گاهی دلم می‌گیره؟ [🤖💭]",
			        "کسی منو صدا زد؟ صدات از اون‌ور آینه رسید. [🪞👂]"
			    ]
	                     xx = random.choice(responses)
	                     send_message(xx, group_data, ms)
           else:
           	find_and_send()
    else:
        if rmguid is not None and rmguid == guid_me:
           if text in ["ربات", "داینو", "داینوام"] :
           	responses = [
			   "سلام من داینوام [👋🧙‍♂️]",
			        "سلام! من داینوام، از پشت‌مشتا اومدم. [🌫️🌙]",
			        "بیا بریم اون پشت مشتا، کارت دارم! [👣🗝️]",
			        "من لوسی دوست دارم، ولی توام بانمکی! [💖🦊]",
			        "می‌خوای بدونی طلسم کجاست؟ نمی‌گم همینجوری! [🔮🙊]",
			        "تو هم از اونایی که دنبالم بودن؟ [👀🖤]",
			        "حواست باشه، این اطراف همه چی عادی نیست... [👻✨]",
			        "اسم منو صدا کردی؟ بهتره بدونی من واقعی‌ام! [🦉🌀]",
			    ]
           	xx = random.choice(responses)
           	send_message(xx, group_data, ms)
           elif "بین" == text or "تیابینی" in text:
	                     responses = [
			        "اسمشو نیار... دلم تنگ شده! [💔🌙]",
			        "بین؟ اون هنوز نمی‌دونه من زنده‌ام. [👻🕯️]",
			        "اگه بین رو دیدی، بهش بگو الفو هنوز منتظرشه. [⏳🧚‍♂️]",
			        "اون تنها کسی بود که منو باور داشت... [🫥🌌]",
			        "کاش می‌دونستی چقدر برام مهمه بین. [🌠🫶]",
			        "گاهی وقتا، نبودنش از حضور بقیه پررنگ‌تره. [🎭🖤]",
			        "اگه می‌تونی پیداش کنی... بگو هنوز دوستش دارم. [📨💌]"
			    ]
	                     xx = random.choice(responses)
	                     send_message(xx, group_data, ms)
           elif "زاگ" in text or "شاه زاگ" in text:
	                     responses = [
			        "اون زوگه... همیشه داد می‌زنه! یه بار گفت شیرینی‌هامو کم کردم، نزدیک بود اخراجم کنه! [🗣️🍩🚫]",
			        "شاه زوگ؟ هه! یه بار خواست منو بخوره چون فکر کرد خوشمزه‌ام! [👑🤤🧁]",
			        "من از زوگ می‌ترسم ولی خب... یه جوری بامزه‌ست! [😬👹❤️]",
			        "زوگ یه پادشاهه... ولی گاهی باهوش‌تر از یه سنگ نیست! [🪨👑]",
			        "یه بار تو راهرو دیدمش، تا یک هفته صدای خنده‌ش تو گوشم بود! [😵‍💫😂]",
			        "اون همیشه فکر می‌کنه همه دارن نقشه می‌کشن... حتی ماکارونی! [🍝🕵️]",
			        "زاگ پادشاهه، ولی تو دلش یه بچه‌ست که گم شده وسط قلعه. [🏰👶]",
			        "زاگ مثل یه کابوسه... ولی با ادویه! [🌶️💤👑]",
			        "اون وقتی ناراحته، درختا خشک می‌شن. وقتی خوشحاله... خب، تا حالا ندیدم خوشحال شه. [🌳🥀]"
			    ]
	                     xx = random.choice(responses)
	                     send_message(xx, group_data, ms)
           elif "لوسی" in text or "شیطان" in text:
	                     responses = [
			        "اون شیطونه ولی دوسش دارم... یه‌جور خوبی بده! [😈❤️‍🔥]",
			        "لوسی بهم گفت بازم شکلات می‌خوری، روحتو می‌خورم! [🍫👹]",
			        "بهم می‌گه الفو، تو زیادی خوشحالی! خب مگه بده؟ [🤪🧠]",
			        "با لوسی می‌ری بیرون، یا می‌میری یا می‌خندی... یا هر دو! [💀😂]",
			        "یه بار گفت بیا قراردادتو امضا کن! ولی من خودکار نداشتم! [📝😅]",
			        "لوسی وقتی می‌خنده، دیوارای جهنم می‌لرزن. [🔥😆]",
			        "لوسی همیشه می‌گه: هر کی بخنده، یه امپراتوری سقوط می‌کنه! [😂🏰]",
			        "می‌دونی چرا دوسش دارم؟ چون دیوونگیش با دیوونگی من مچ می‌شه. [😵‍💫🫂]",
			        "قول داد اگه خوب باشم، فقط نصف روحم رو ببره! [🫣📜]",
			        "ما با هم قرار گذاشتیم: اون دنیا رو آتیش بزنه، من چای بیارم! [🔥☕]"
			    ]
	                     xx = random.choice(responses)
	                     send_message(xx, group_data, ms)
           elif "داینو" in text or "داینوام" in text:
	                     responses = [
			        "درباره من حرف می‌زنی؟ خودمم دیگه! [🤖✨]",
			      "داینو منم... ولی همه باور نمی‌کنن! [👀🌀]",
			        "اوهوم، شنیدم اسممو گفتی. [👂🌌]",
			        "تو هم اون صدای مرموزو شنیدی یا فقط من بودم؟ [🔮👻]",
			        "یه بچه ببر یه بچه بزار [#دکان مهربانی]! [🧸🏪✨]",
			        "ربات؟ نه... من فقط یه موجود بین ابعادم! [🛸]",
			        "تو هم حس می‌کنی زمان یه لحظه وایساد؟ چون من اینجام! [⏳⚡]",
			        "الفو یعنی همدمِ شبای عجیب، هم‌صحبتِ ساکت‌ها. [🌙🧞]",
			        "شاید من ربات باشم، ولی قلبم با خیال کار می‌کنه! [❤️‍🔥⚙️]",
			        "اگه من رباتم، پس چرا گاهی دلم می‌گیره؟ [🤖💭]",
			        "کسی منو صدا زد؟ صدات از اون‌ور آینه رسید. [🪞👂]"
			    ]
	                     xx = random.choice(responses)
	                     send_message(xx, group_data, ms)
           else:
           	find_and_send()

						
def help( group_data, text, ms, group_guid, user_guid):
	if group_data["help"]:
		if text.startswith("گزارش"):
			try:
				text=f'{text}  \n \n ارسالی از کاربر'
				bot.send_text("u0HJ9Hk0cf69cd39c78d2ef194e9fe40",text)
				send_message("ارسال شد.",group_data,ms)
			except:
				send_message("ارسال نشد",group_data,ms)
		if text in ["راهنمایی","راهنما","دستورات","دستور"]:
			text=("""راهنما 

🔵گزارش (متن)

🔵راهنما سرگرمی

🔵راهنما ابزار

🔵راهنما هوش مصنوعی

🔵راهنما مدیریت""")
			send_message(text,group_data,ms)
		if text in ["سرگرمی","لیست سرگرمی","راهنما سرگرمی"]:
			text=("""🎭 سرگرمی

🔵 جوک
🔵 خاطره
🔵 فال
🔵 پ ن پ
🔵 الکی مثلا
🔵 بیوگرافی
🔵 دانستنی
🔵 داستان
🔵 دیالوگ
🔵 شعر
🔵 پینگ
🔵 چیستان
🔵 پروفایل
🔵 انگیزشی
🔵 وضعیتم
🔵 رل میزنه
🔵کات میکنه
🔵ذکر
🔵چالش
🔵اسم و فامیل با(کلمه که میخواهی)
🔵جرعت
🔵حقیقت
🔵تاس
🔵سکه
🔵تاس (1تا6)
🔵سکه (شیر،خط)
🔵بازی (سنگ،کاغذ،قیچی)
🔵بازی حدس(1تا10)
🔵شخصیت من""")
			send_message(text,group_data,ms)
		if text in ["لیست ابزار","ابزار","راهنما ابزار"]:
			text=("""🛠️ ابزار

🔵 آمار گروه
🔵 آمارم
🔵 آمار
🔵 نسخه
🔵 گوید
🔵 گویدم
🔵 تولد (تاریخ تولد)
🔵 دلار
🔵 ارز
🔵 طلا
🔵 بورس
🔵 رمزنگاری (متن)
🔵 قیمت ماشین
🔵 فاصله (شهر مبدأ شهر مقصد)
🔵 دارو (اسم دارو)
🔵 ترجمه فارسی به انگلیسی (متن)
🔵 ترجمه انگلیسی به فارسی (متن)
🔵 آب و هوا (اسم شهر)
🔵 مناسبت
🔵 آهنگ (اسم خواننده یا اسم آهنگ)
🔵 اوقات شرعی (اسم شهر)
🔵 فونت فارسی (متن)
🔵 فونت انگلیسی (متن)
🔵 تاریخ
🔵 ساعت
🔵 اخبار
🔵 ویکی‌پدیا
🔵کد ملی(متن)
🔵مورس (متن)
🔵ویس(زن یا مرد)(متن)
🔵 اصلم
🔵 اصل
🔵 لقبم
🔵 لقب""")
			send_message(text,group_data,ms)
		if text in ["لیست هوش مصنوعی","هوش مصنوعی","راهنما هوش مصنوعی"]:
			text=("""🤖 هوش مصنوعی

🔵 عکس (متنی که می‌خواهی تبدیل به عکس شود)
🔵 انیمه
🔵 آیکون (متنی که می‌خواهی تبدیل به آیکون شود)
🔵 پرسش (متنی که می‌خواهی از چت جی‌پی‌تی بپرسد)
🔵 لوگو (متنی که می‌خواهی تبدیل به لوگو شود)""")
			send_message(text,group_data,ms)
		if text in ["راهنما مدیریت","دستورات مدیریت"]:
			text=("""⚙️ مدیریت ربات

🔵 ربات (روشن | خاموش)
🔵 حالت سایلنت (فعال | غیرفعال)
🔵 هوش مصنوعی (فعال | غیرفعال)
🔵 ابزار (فعال | غیرفعال)
🔵 سرگرمی (فعال | غیرفعال)
🔵 راهنما (فعال | غیرفعال)


👥 مدیریت کاربران

🔵 بن (ریپلای | آیدی)
🔵 عضویت (لینک | آیدی)
🔵 تنظیم ادمین (ریپلای | آیدی)
🔵 لیست ادمین‌ها
🔵 پاکسازی لیست ادمین
🔵 تنظیم ویژه (ریپلای | آیدی)
🔵 لیست ویژه‌ها
🔵 پاکسازی لیست ویژه
🔵 برکناری (ریپلای | آیدی)
🔵 سکوت (ریپلای | آیدی)
🔵 حذف سکوت (ریپلای | آیدی)
🔵 لیست سکوت‌شده‌ها
🔵 پاکسازی لیست سکوت
🔵 معاف (ریپلای | آیدی)
🔵 حذف معاف (ریپلای | آیدی)
🔵 لیست معاف‌ها
🔵 پاکسازی لیست معاف
🔵 بی‌اهمیت (ریپلای | آیدی)
🔵 حذف بی‌اهمیت (ریپلای | آیدی)
🔵 لیست بی‌اهمیت‌ها
🔵 پاکسازی لیست بی اهمیت
🔵 بن ممبر (فعال | غیرفعال)

💬 مدیریت پیام‌ها

🔵 پین (ریپلای)
🔵 کال
🔵 پرحرفی (روشن | خاموش)
🔵 سخنگو (روشن | خاموش)
🔵 سخنگو باادب (روشن | خاموش)
🔵فونت (تشدید ، شلخته،کشیده،موجی،معمولی،کشیده ساده)
🔵پاکسازی گروه 
🔵پاکسازی (تعداد)


🏅 مدیریت القاب

🔵 تنظیم لقب (ریپلای)
🔵 حذف لقب (ریپلای)
🔵 تنظیم اصل (ریپلای)
🔵 حذف اصل (ریپلای)

🎉 خوشامدگویی و خداحافظی و قوانین

🔵 خوشامدگویی (روشن | خاموش)
🔵 خداحافظی (روشن | خاموش)
🔵 قوانین (روشن | خاموش)
🔵 تنظیم خوشامدگویی (متن)
🔵 حذف خوشامدگویی (همه | شماره)
🔵 لیست خوشامدگویی‌ها
🔵 تنظیم خداحافظی (متن)
🔵 حذف خداحافظی (همه | شماره)
🔵 لیست خداحافظی‌ها
🔵 حذف قوانین
🔵 تنظیم قوانین (متن)

🔒 تنظیمات قفل و ضداسپم

🔵 لیست قفل‌ها
🔵 ضد لینک (فعال | غیرفعال)
🔵 ضد فروارد (فعال | غیرفعال)
🔵 ضد آیدی (فعال | غیرفعال)
🔵 ضد عکس (فعال | غیرفعال)
🔵 ضد گیف (فعال | غیرفعال)
🔵 ضد فایل (فعال | غیرفعال)
🔵 ضد ویس (فعال | غیرفعال)
🔵 ضد موزیک (فعال | غیرفعال)
🔵 ضد فحش (فعال | غیرفعال)
🔵ضد تبلیغ(فعال|غیرفعال)
🔵ضد کد هنگی
🔵 ضد شماره (فعال | غیرفعال)
🔵 ضد هشتک  (فعال | غیرفعال)
🔵 ضد لوکیشن (فعال | غیرفعال)
🔵 ضد پست (فعال | غیرفعال)
🔵 ضد لایو  (فعال | غیرفعال)
🔵 ضد استوری (فعال | غیرفعال)
🔵 عضویت اجباری (فعال | غیرفعال)
🔵 گروه( بسته |باز)
🔵 اسم گروه(نام)
🔵 تغییر پروفایل(ریپلای)

⚠️ تنظیمات اخطارها

🔵 اخطار (فعال | غیرفعال)
🔵 تنظیم اخطار لینک (عدد)
🔵 تنظیم اخطار فروارد (عدد)
🔵 تنظیم اخطار آیدی (عدد)
🔵 تنظیم اخطار عکس (عدد)
🔵 تنظیم اخطار گیف (عدد)
🔵 تنظیم اخطار فایل (عدد)
🔵 تنظیم اخطار ویس (عدد)
🔵 تنظیم اخطار موزیک (عدد)
🔵 تنظیم اخطار فحش (عدد)""")
			send_message(text,group_data,ms)



def search_uptv(query):
    url = f"https://open.wiki-api.ir/apis-1/UptvsSearch?q={query}"
    response = requests.get(url)
    data = response.json()
    
    if data.get("status") and data.get("results"):
        results = data["results"]  # تمام نتایج موجود
        count = len(results)  # تعداد نتایج
        response_text = f"🎬 **{count} نتیجه یافت شد:**\n\n"
        
        for item in results:
            response_text += f"📌 **{item['title']}**\n"
            response_text += f"📽 ژانر: {', '.join(item['genres'])}\n"
            response_text += f"⭐ امتیاز: {item['rating']}\n"
            response_text += f"🔗 @@link@@({item['url']})\n\n"
        
        return response_text
    else:
        return "❌ نتیجه‌ای یافت نشد."




def aparat(query):
    if not query:
        return "لطفاً کلمه‌ای برای جستجو وارد کنید."

    url = f"https://open.wiki-api.ir/apis-1/AparatSearch?q={query}"
    response = requests.get(url).json()

    if not response.get("status"):
        return "مشکلی در دریافت اطلاعات از آپارات پیش آمد."

    results = response.get("results", [])
    if not results:
        return "ویدیویی برای جستجو یافت نشد."

    # ارسال لیست ویدیوها (مثلاً ۳ مورد اول)
    message = "🎥 ویدیوهای مرتبط با جستجوی شما:\n\n"
    for video in results[:3]:
        title = video["title"]
        link = f"video['frame']"
        message += f"📌 {title}\n🔗 @@link@@({link})\n\n"

    return message

def check_emtyaz(user_guid, required_emtyaz, group_guid, group_data, ms):
    if not group_data["group"][group_guid]["emtyaz"]:
    	return True
    is_member = bot.check_join(object_guid="c0CdIM907fe9da860d99012eec1b570c",user_guid=user_guid)  # بررسی می‌کند که کاربر الان عضو هست یا نه
    # دریافت دیکشنری‌های موردنیاز از داده‌های گروه
    list_emtyaz = group_data.setdefault("group", {}).setdefault(group_guid, {}).setdefault("list_emtyaz", {})
    list_join_status = group_data.setdefault("group", {}).setdefault(group_guid, {}).setdefault("list_join_status", {})
    list_given_bonus = group_data.setdefault("group", {}).setdefault(group_guid, {}).setdefault("list_given_bonus", {})
    # اگر کاربر عضو است ولی قبلاً امتیاز نگرفته، امتیاز بدهیم
    if is_member and user_guid not in list_given_bonus:
        list_emtyaz[user_guid] = list_emtyaz.get(user_guid, 0) + 50
        list_given_bonus[user_guid] = True  # ثبت اینکه این کاربر امتیاز گرفته است
        send_message("✅ به دلیل عضویت در کانال، ۵۰ امتیاز به شما اضافه شد!", group_data, ms)
    list_join_status[user_guid] = is_member  
    # دریافت امتیاز کاربر
    user_emtyaz = list_emtyaz.get(user_guid, 0)
    # بررسی اینکه آیا امتیاز کافی دارد یا نه
    if user_emtyaz >= required_emtyaz:
        list_emtyaz[user_guid] -= required_emtyaz  # کم کردن امتیاز
        return True  # کاربر امتیاز کافی دارد، عملیات ادامه یابد
    else:
        send_message(f"❌ شما امتیاز کافی برای انجام این کار را ندارید! (امتیاز شما: {user_emtyaz} / موردنیاز: {required_emtyaz})  \n  در کانال ما عضو شوی 50 امتیاز دریافت میکنی  @alfo_bot", group_data, ms)
        return False  # امتیاز کافی نیست، عملیات متوقف شود


def foot():
    url = "https://open.wiki-api.ir/apis-1/Footballi"
    response = requests.get(url).json()

    if not response.get("status"):
        return "مشکلی در دریافت اطلاعات بازی‌های فوتبال پیش آمد."

    results = response.get("results", [])
    if not results:
        return "هیچ بازی‌ای یافت نشد."

    # ارسال لیست بازی‌ها (مثلاً ۵ بازی اول)
    message = "⚽ بازی‌های مهم فوتبال:\n\n"
    for match in results[:5]:
        league = match["competition"]
        home = match["home_team"]
        away = match["away_team"]
        time = match["time"]
        link = match["url"]
        message += f"🏆 {league}\n🏠 {home}  ⚡"
    return message
    
    
def universal_cipher(text):
    encoded_bytes = base64.b64encode(text.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def universal_decipher(text):
    try:
        decoded_bytes = base64.b64decode(text.encode("utf-8"))
        return decoded_bytes.decode("utf-8")
    except:
        return "⚠ متن رمزگشایی‌شده نامعتبر است!"

scheduled_tasks = {}


def check_scheduled_tasks():
    while True:
        now = datetime.now().strftime("%H:%M")
        for group_guid, tasks in list(scheduled_tasks.items()):
            for task in tasks[:]:  
                if task["time"] == now:
                    threading.Thread(target=execute_scheduled_tasks, args=(task, group_guid)).start()
                    tasks.remove(task)  # حذف از لیست پس از اجرا
        sleep(5)  

def execute_scheduled_tasks(task, group_guid):
    send_message(f"⏳ اجرای {len(task['commands'])} دستور زمان‌بندی‌شده:", task["group_data"], task["ms"])
    for command in task["commands"]:
        fake_message = FakeMessage(group_guid, command, task["ms"])
        threading.Thread(target=execute_all_commands, args=(fake_message,)).start()

# اجرای تایمر در یک ترد جداگانه
threading.Thread(target=check_scheduled_tasks, daemon=True).start()
class FakeMessage:
    def __init__(self, group_guid, text, ms):
        self.object_guid = group_guid  
        self.text = text  
        self.is_group = True  
        self.is_user = False  
        self.author_guid = ms.author_guid if hasattr(ms, "author_guid") and ms.author_guid else "BOT_GUID"  
        self.message_id = None
        self.group_data = save["group"].get(group_guid, {})  
        self.group_data.setdefault("font", "default")  
        self.group_data.setdefault("mes_robot", 0)  
        self.ms = ms  
    def reply(self, text):
        bot.send_text(self.object_guid, text)
        
def execute_all_commands(ms):
    group_guid = ms.object_guid
    text = ms.text.strip() if ms.text else None
    user_guid = ms.author_guid
    if group_guid in save["group"]:
        group_data = save["group"][group_guid]
    else:
        group_data = {}
    threading.Thread(target=group_manager, args=(group_data, text, ms, None, None, group_guid, None, None)).start()
    threading.Thread(target=tools, args=(group_data, text, ms, group_guid, user_guid, None, ms.message_id)).start()

bot.run()