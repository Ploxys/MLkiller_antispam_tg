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
white = db.white_group
black_chanal = db.bchanal


def get_bch(message):
    try:
        request = black_chanal.find_one({"chat": message.chat.id,"chanal":message.forward_origin.chat.id})
        return request
    except:
        pass
def get_capha(message):
    request = groups.find_one({"chat": message.chat.id})
    return request["capcha"]
def get_white(message):
    request = white.find_one({"chat": message.chat.id,"user":message.from_user.id})

def get_smile(message):
    request = groups.find_one({"chat": message.chat.id})
    return request["smile"]

def get_link(message):
    request = groups.find_one({"chat": message.chat.id})
    return request["link"]

def get_antispam(message):
    request = groups.find_one({"chat": message.chat.id})
    if request != None:
        return request["antispam"]

def get_but_kill(message):
    request = groups.find_one({"chat": message.chat.id})
    if request != None:
        print(request)
        return request["but_kill"]


def get_spambase(text,message):
    request = spam.find_one({"text": text})
    if request != None:
        print(1234123)
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    #bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    return request

def get_white_list(text):
    request = white_list.find_one({"text": text})
    return request

def get_white_user(ids):
    request = white_user.find_one({"user_id": ids})
    return request

def get_settigs_url(message):
    request = groups.find_one({"chat": message.chat.id})
    return request["but_kill"]
