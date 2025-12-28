from datetime import datetime, timedelta
import telebot
import config
from pymongo import MongoClient
import time
client = MongoClient()
db = client['burgerdefenser']
captha = db.captha
time_msg = db.timer_msg

bot = telebot.TeleBot(config.token)
def timer():
    while 1:
        try:
            s = datetime.strftime(datetime.now(), '%H:%M')
            request = captha.find({"time": s})
            requests = time_msg.find({"time": s})
            for r in request:
                db.captha.delete_one({"time": s})
                bot.delete_message(chat_id=r["chat"], message_id=r["message_id"])
                bot.kick_chat_member(chat_id=r["chat"], user_id=r['user'])
            for r in requests:
                db.timer_msg.delete_one({"time": s})
                bot.delete_message(chat_id=r["chat"], message_id=r["message_id"])
            time.sleep(1)
        except:
            pass
        #ищем по времени в бд баним пользователя удаляем запись
    
