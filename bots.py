import telebot
from pymongo import MongoClient
client = MongoClient()
db = client['burgerdefenser']
neuro = db.neuro_base
bot = telebot.TeleBot("7675398426:AAF3SM8Bb88fc80ZWFPQYv6b-Eq5sKyeqh8")
@bot.message_handler(content_types=["text"])
def handle_text(message):
    globalis = {"text": message.text,
                "status": 2}
    post_id = neuro.insert_one(globalis).inserted_id
    print(post_id)
bot.polling(none_stop=True)
