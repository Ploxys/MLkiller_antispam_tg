import pickle
import telebot
import config
from db import analy,timer_msg,statistic
from filters import passive_defence
import warnings
def warn(*args, **kwargs):
    pass
warnings.warn = warn
filename1 = 'datasets/RidgeRegressor.sav'
loaded_mode4 = pickle.load(open(filename1, 'rb'))
filename2 = 'datasets/GradientBoostingRegressor.sav'
loaded_mode4 = pickle.load(open(filename1, 'rb'))
loaded_mode3 = pickle.load(open(filename2, 'rb'))
bot = telebot.TeleBot(config.token)
def last_defence(message): #RidgeClassifier.sav
    if message.text is not None:
        text = message.text
    if message.caption is not None:
        text = message.caption
    res = loaded_mode3.predict([text])[0]*100 #Calculate percentage accuracy
    res2 = loaded_mode4.predict([text])[0]*100 #Calculate percentage accuracy
    if res > 100:
        res = 100
    if res2 > 100:
        res2 = 100
    itog = res + res2 / 2
    print("!!!!!" + str(itog) +  "!!!!")
    if itog > 100:
        itog = 100
    print(itog)
    if itog > 35 and itog < 60:
        analy.system_active_detection(message,"Фрост++\n\n🔍Вероятность: " + str(itog) + "%\n\nДействие: отправвленно на анализ")
        passive_defence.detector_spamer(message)
    if itog > 60 and itog < 80:
        analy.system_active_detection(message,"Фрост++\n\n🔍Вероятность: " + str(itog) + "%\n\nДействие: удаленно")
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        s = bot.send_message(chat_id=message.chat.id,text="🛡 Обнаружен спам\n⚙️ Алгоритм: Фрост++\n🤖 Пользователь: " + " " + "[" + message.from_user.first_name +  "]" + "(tg://user?id=" + str(message.from_user.id) + ") " + "\n\n👊 Действие: удалить сообщение",parse_mode="Markdown")
        timer_msg.mmm(s)
        statistic.set_stat("frost_plus",itog)
    if itog > 79 and itog < 101:
        analy.system_active_detection(message,"Фрост++\n\n🔍Вероятность: " + str(itog) + "%\n\nДействие: удаленно и заблокированно")
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        s = bot.send_message(chat_id=message.chat.id,text="🛡 Обнаружен спам\n⚙️ Алгоритм: Фрост++\n🤖 Пользователь: " + " " + "[" + message.from_user.first_name +  "]" + "(tg://user?id=" + str(message.from_user.id) + ") " + "\n\n👊 Действие: удалить сообщение и заблокировать",parse_mode="Markdown")
        timer_msg.mmm(s)
        statistic.set_stat("frost_plus",itog)
######В разработке ######