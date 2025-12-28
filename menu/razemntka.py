from telebot import types
from db import get_settings
def antispam_algoritms():
    markup3 = types.InlineKeyboardMarkup()
    subzero = types.InlineKeyboardButton("Саб-Зиро", callback_data='subzero')
    fredy = types.InlineKeyboardButton("Фредди Крюгер", callback_data='fredy')
    hotary = types.InlineKeyboardButton("Хотару", callback_data='hotary')
    frost = types.InlineKeyboardButton("Фрост", callback_data='frost')
    frost_plus = types.InlineKeyboardButton("Фрост++", callback_data='frost_plus')
    markup3.add(subzero,hotary,frost,frost_plus)
    return markup3

def filters_menu(message):
    s = get_settings.get_settigs_url(message)
    link = get_settings.get_link(message)
    smile = get_settings.get_smile(message)
    capcha = get_settings.get_capha(message)
    markup3 = types.InlineKeyboardMarkup()
    print(s)
    if s == False:
        antispam = types.InlineKeyboardButton("Разрешить URL кнопки", callback_data='url_open')
        markup3.add(antispam)
    if s == True:
        antispam1 = types.InlineKeyboardButton("Запретить URL кнопки", callback_data='url_close')
        markup3.add(antispam1)
    if link == False:
        antispam = types.InlineKeyboardButton("Разрешить ссылки t.me", callback_data='link_open')
        markup3.add(antispam)
    if link == True:
        antispam1 = types.InlineKeyboardButton("Запретить ссылки t.me", callback_data='link_close')
        markup3.add(antispam1)
    if smile == False:
        antispam = types.InlineKeyboardButton("Смайл-защита вкл", callback_data='smile_open')
        markup3.add(antispam)
    if smile == True:
        antispam1 = types.InlineKeyboardButton("Смайл-защита выкл", callback_data='smile_close')
        markup3.add(antispam1)
    if capcha == False:
        antispam = types.InlineKeyboardButton("Капча вкл", callback_data='capcha_open')
        markup3.add(antispam)
    if capcha == True:
        antispam1 = types.InlineKeyboardButton("Капча выкл", callback_data='capcha_close')
        markup3.add(antispam1)
    return markup3

def menu():
    markup3 = types.InlineKeyboardMarkup()
    antispam = types.InlineKeyboardButton("Антиспам", callback_data='antispam')
    filters = types.InlineKeyboardButton("Фильтры", callback_data='filters')
    markup3.add(antispam,filters)
    return markup3

def welcome_but():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("FAQ", url='http://mlkiller.ru/sample-page/')
    button2 = types.InlineKeyboardButton("Новости бота", url='https://t.me/mlkill_dev')
    button3 = types.InlineKeyboardButton("Поддержка", url='https://t.me/baby_burgers')
    button4 = types.InlineKeyboardButton("Презентация бота", url='https://mlkiller.ru/')

    markup.add(button1,button2,button3,button4)
    return markup

def create_admin_panel():
    markup = types.InlineKeyboardMarkup()
    spam = types.InlineKeyboardButton("🗑", callback_data='spam')
    warning = types.InlineKeyboardButton("☢️", callback_data='warning')
    good = types.InlineKeyboardButton("🟢", callback_data='good')
    white = types.InlineKeyboardButton("👼", callback_data='good_white')
    markup.add(spam,warning,good,white)
    return markup

def capcha():
    markup = types.InlineKeyboardMarkup()
    spam = types.InlineKeyboardButton("Войти", callback_data='welcome')
    markup.add(spam)
    return markup