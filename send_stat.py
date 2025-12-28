import telebot
import time
from pymongo import MongoClient
import datetime
import config
client = MongoClient()
db = client['burgerdefenser']
stat = db.statistic
bot = telebot.TeleBot(config.token)
while 1:
    print(str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute))
    if str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) == str("21:5"):
        request = stat.find_one({"date": str(datetime.datetime.now().date())})
        bot.send_message(chat_id=-1002492414872,text="📅 Отчет за 24 часа\n\n❄️ Саб-Зиро: " + str(request["sub-zero"]) + "\n🥊 Хаттару: " + str(request["hotaru"]) + "\n🤨 Фрост: " + str(request["frost"]) + "\n❤️‍🔥 Фрост++: " + str(request["frost_plus"]) + "\n\n📈 Средняя точность: " + str(sub) + "%")
        time.sleep(70)
    time.sleep(1)
