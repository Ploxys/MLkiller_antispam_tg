from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import telebot
import config
import re
import db
import sklearn
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
import sys
import numpy as np
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.ensemble import GradientBoostingRegressor
from db import analy,get_settings,youtu_db
from pytube import YouTube
from pytube import Channel
from lang import ru
bot = telebot.TeleBot(config.token)
def detector_spamer(message): #GradientBoostingRegressor.sav
    if message.text is not None:
            text = message.text
    if message.caption is not None:
            text = message.caption
    link = link_detector(text)
    sobaka = find_sobaka(text)
    slovo = find_slovo(text)
    cl = ciril_latin(text)
    money = numbers_money(text)
    itog = int(link) + int(sobaka) + int(slovo) + int(cl) + int(money)
    if itog > 0:
        analy.system_active_detection(message,"Статичная защита")



def user_name_filter(message):
    spam_names = ["работ","Авиабилеты","Менеджер"]
    first_name = str(message.from_user.first_name).lower()
    last_name = str(message.from_user.last_name).lower()
    for s in spam_names:
        if first_name.find(str(s)) != -1:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        if last_name.find(str(s)) != -1:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())
def match2(text, alphabet=set('qwertyuiopasdfghjklzxcvbnm')):
    return not alphabet.isdisjoint(text.lower())
def match3(text, alphabet=set('@')):
    return not alphabet.isdisjoint(text.lower())

def simvols(text, alphabet=set('р$')):
    return not alphabet.isdisjoint(text.lower())
def numbers(text, alphabet=set("0123456789")):
    return not alphabet.isdisjoint(text.lower())

def numbers_money(text):
    text = str(text).split(" ")
    for text in text:
        if simvols(text) == True and numbers(text) == True:
            return 1
    return 0


def ciril_latin(text):
    text = str(text).split(" ")
    for text in text:
        if match2(text) == True and match(text) == True:
            return 1
    return 0

def ciril_latin_passive(message):
    if message.text is not None:
            text = message.text
    if message.caption is not None:
            text = message.caption
    text = str(text).split(" ")
    for text in text:
        if match2(text) == True and match(text) == True:
            db.system_passive_detection(message,"Символьный")
            break

def link_detector(message):
    regex = r"(?P<domain>\w+\.\w{2,3}\D+\w+)"
    matches = re.finditer(regex, str(message), re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        ss = str("{match}").format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
        dd = str(ss).split("/")
        if dd[0] == "t.me" or dd[0] == "telegram.me":
            return 1
    return 0

def link_detector_wat(message):
    regex = r"(?P<domain>\w+\.\w{2,3}\D+\w+)"
    matches = re.finditer(regex, str(message), re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        ss = str("{match}").format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
        dd = str(ss).split("/")
        if dd[0] == "t.me" or dd[0] == "telegram.me":
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

def youtube_detector(message):
    regex = r"(?P<domain>\w+\.\w{2,3}\D+\w+)"
    matches = re.finditer(regex, str(message), re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        ss = str("{match}").format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
        dd = str(ss).split("/")
        if dd[0] == "youtu.be" or dd[0] == "youtu.be" or dd[0] == "www.youtube.com":
            video = str(ss)
            x= YouTube(video)
            result = youtu_db.get_chanals(message,x.channel_id)
            print(result)
            if result != None:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                bot.send_message(chat_id=message.chat.id, text=ru.event_block_youtube_chanal)
                break


def find_sobaka(text):
    text = str(text).split(" ")
    for t in text:
        if match2(t) == True and match3(t) == True:
            return 1
    return 0

def find_slovo(text):
    slovar = ["ищу","требуются","подpабoтка","заработок",
    "тысяч","$","работу","зapaбoтoк","лс","лс","оплaта",
    "халтурка","пoдpаботк","тpeбyютcя","вaкaнcия","шaа6aaшк",
    "деньги","заpaбoтaть","нужны","лaве","разнорабочий",
    "пpeдпрuятиe","в день","срочно","требуется","зарабатывать","бесплатно","платно","удалёнке","удалёнка",
    'удаленке','удаленка','долларов',"рублей",'долл',"₽","халтура",'денюжкой','денюгами','денюжками','поможет','набор','ллюдей',
    'пишите','заинтересованы','заинтересовал']
    for t in slovar:
        if str(text).lower().find(t) != -1:
            return 1
    return 0
