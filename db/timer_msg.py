from pymongo import MongoClient
from menu import razemntka
import telebot
import config
from lang import ru
from datetime import datetime, timedelta
bot = telebot.TeleBot(config.token)

client = MongoClient()
db = client['burgerdefenser']
timer = db.timer_msg

def mmm(s):
    globalis = {"chat": s.chat.id,
                "message_id": s.id,
                "time": datetime.strftime(datetime.now() + timedelta(minutes=5), '%H:%M')}
    post_id = timer.insert_one(globalis).inserted_id