from pymongo import MongoClient
from menu import razemntka
import telebot
from lang import ru
import config
bot = telebot.TeleBot(config.token)

client = MongoClient()
db = client['burgerdefenser']
groups = db.groups
spam = db.spam
white_list = db.white_list
white_user = db.white_user
