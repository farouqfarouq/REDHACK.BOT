
from keep_alive import keep_alive
import logging
import json
import random
import string
from datetime import datetime, timedelta
import pytz
from telegram import (
    Update, InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters,
    ContextTypes, ConversationHandler, CallbackQueryHandler
)

keep_alive()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

ADMIN_ID = 5050261460
BOT_TOKEN = "7127546371:AAHD8uxzigfMMg7sN9EQAbr2bFOUeOOPOqk"

CHOOSE_TYPE, ASK_DURATION, ASK_NAME, ASK_TG_USERNAME, AWAIT_DISCOUNT_CODE, ACCEPT_POLICY = range(6)

subscriptions_world = {
    "Saturday": 10,
    "Sunday": 10,
    "Monday": 7,
    "Tuesday": 5,
    "Wednesday": 5,
    "Thursday": None,
    "Friday": None,
}

subscriptions_lite = {
    "أسبوع": 10,
    "شهر": 15,
    "سنة": 25,
    "دائم": 40
}

user_data_temp = {}
subscribers = {}
discount_codes = {}

DISCOUNT_CODES_FILE = "discount_codes.json"
SUBSCRIBERS_FILE = "subscribers.json"

def load_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

discount_codes = load_json(DISCOUNT_CODES_FILE)
subscribers = load_json(SUBSCRIBERS_FILE)

def generate_discount_code(length=8):
    letters_digits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters_digits) for _ in range(length))

def time_until_friday_5am():
    tz = pytz.timezone('Asia/Riyadh')
    now = datetime.now(tz)
    friday_5am = now.replace(hour=5, minute=0, second=0, microsecond=0)
    while friday_5am.weekday() != 4 or friday_5am <= now:
        friday_5am += timedelta(days=1)
    diff = friday_5am - now
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    return days, hours, minutes

POLICY_TEXT = (
    "‏شروط الاستخدام و ضمان حق المشتركين:

"
    "‏- عند الاشتراك بالهكر بواسطة حساب لعبة أو أي حساب...
"
    "‏- عند محاولة إعادة أخذ الحساب أو طلب استرداد أو محاولة تلاعب سيتم إيقاف المفتاح فورا.
"
    "‏- عند إعطاء ملف الهكر أو المفتاح لشخص آخر يتم إيقاف المفتاح فورا.
"
    "‏- عند نشر منشورات غير مناسبة أو الكلام خارج الأدب يتم الإيقاف والحظر.
"
    "‏- عند إيقاف الهكر بسبب تحديث أو توقف يتم تقسيم الأيام واسترداد المبلغ أو تعويض متفق عليه.
"
    "‏- إذا لم يعمل الهكر بجهازك مع إبلاغ المطور قبل الاشتراك يمكنك استرجاع المبلغ.

"
    "‏يرجى الموافقة على الشروط للاستمرار."
)

# الباقي من الكود يبقى مثل اللي سويناه مسبقاً

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # ... ضيف الهاندلرات هنا مثل ما اتفقنا (ConversationHandler و CallbackQueryHandler) ...

    print("✅ البوت يعمل...")
    app.run_polling()

if __name__ == '__main__':
    main()
