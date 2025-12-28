from pymongo import MongoClient
from menu import razemntka
import telebot
from lang import ru
from pytube import YouTube
from pytube import Channel
import config
bot = telebot.TeleBot(config.token)

client = MongoClient()
db = client['burgerdefenser']
groups = db.groups
youtube = db.youtube
white = db.white_group
black_chanal = db.bchanal

def chanal_add(message):
    request = black_chanal.find_one({"chat": message.chat.id,"chanal":message.reply_to_message.forward_origin.chat.id})
    if request == None:
        globalis = {"chat": message.chat.id,
                    "chanal": message.reply_to_message.forward_origin.chat.id}
        post_id = black_chanal.insert_one(globalis).inserted_id
def chanal_delete(message):
    request = black_chanal.find_one({"chat": message.chat.id,"chanal":message.reply_to_message.forward_origin.chat.id})
    if request != None:
        ss = db.bchanal.delete_one({"chat": message.chat.id,"chanal":message.reply_to_message.forward_origin.chat.id})
        print(ss)
def white_list_add(message):
    request = white.find_one({"chat": message.chat.id,"user":message.reply_to_message.from_user.id})
    if request == None:
        globalis = {"chat": message.chat.id,
                    "user": message.reply_to_message.from_user.id}
        post_id = white.insert_one(globalis).inserted_id

def white_list_delete(message):
    request = white.find_one({"chat": message.chat.id,"user":message.reply_to_message.from_user.id})
    if request != None:
        print("clean")
        ss = db.white_group.delete_one({"chat": message.chat.id,"user":message.reply_to_message.from_user.id})
        print(ss)
def ban_youtube(message,chan):
    video = str(chan)
    x = YouTube(video)
    request = youtube.find_one({"chat": message.chat.id,"youtube":x.channel_id})
    if request == None:
        globalis = {"chat": message.chat.id,
                    "youtube": x.channel_id}
        post_id = youtube.insert_one(globalis).inserted_id
        return True
    else:
        return False

def unban_youtube(message,chan):
    video = str(chan)
    x = YouTube(video)
    db.youtube.delete_one({"youtube": x.channel_id,"chat":message.chat.id})

def change_antispam(message,tup):
    request = groups.find_one({"chat": message.chat.id})
    if tup == "subzero":
        if request != None:
            result = db.groups.update_many({'chat': message.chat.id},
                            {'$set': {'antispam': "subzero"}})
    if tup == "hotary":
        if request != None:
            result = db.groups.update_many({'chat': message.chat.id},
                            {'$set': {'antispam': "hotary"}})
    if tup == "frost":
        if request != None:
            result = db.groups.update_many({'chat': message.chat.id},
                            {'$set': {'antispam': "frost"}})
    if tup == "frost_plus":
        if request != None:
            result = db.groups.update_many({'chat': message.chat.id},
                            {'$set': {'antispam': "frost_plus"}})

def change_filters(call,message):
    if call.data == "url_close":
                    result = db.groups.update_many({'chat': message.chat.id},
                                    {'$set': {'but_kill': False}})
    if call.data == "url_open":
                    result = db.groups.update_many({'chat': message.chat.id},
                                    {'$set': {'but_kill': True}})

def change_filters_url(call,message):
    if call.data == "link_close":
                    result = db.groups.update_many({'chat': message.chat.id},
                                    {'$set': {'link': False}})
    if call.data == "link_open":
                    result = db.groups.update_many({'chat': message.chat.id},
                                    {'$set': {'link': True}})

def change_filters_smile(call,message):
    if call.data == "smile_close":
                    result = db.groups.update_many({'chat': message.chat.id},
                                    {'$set': {'smile': False}})
    if call.data == "smile_open":
                    result = db.groups.update_many({'chat': message.chat.id},
                                    {'$set': {'smile': True}})
def change_filters_capcha(call,message):
    if call.data == "capcha_close":
                    result = db.groups.update_many({'chat': message.chat.id},
                                    {'$set': {'capcha': False}})
    if call.data == "capcha_open":
                    result = db.groups.update_many({'chat': message.chat.id},
                                    {'$set': {'capcha': True}})