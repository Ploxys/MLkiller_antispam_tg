from pymongo import MongoClient
from menu import razemntka
import telebot
from lang import ru
import config
bot = telebot.TeleBot(config.token)

client = MongoClient()
db = client['burgerdefenser']
youtu = db.youtube

def get_chanals(message,channal):
    request = youtu.find_one({"chat": message.chat.id,"youtube": channal})
    return request
