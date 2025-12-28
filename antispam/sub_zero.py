import pickle
import telebot
import config
from db import analy,timer_msg,statistic
from filters import passive_defence
import warnings
def warn(*args, **kwargs):
    pass
warnings.warn = warn
filename1 = 'datasets/RandomForestRegressor.sav'
loaded_model = pickle.load(open(filename1, 'rb'))
bot = telebot.TeleBot(config.token)

def antispam(message):
    if message.text is not None:
        text = message.text
    if message.caption is not None:
        text = message.caption
    res = loaded_model.predict([text])[0]*100 #Calculate percentage accuracy
    if res > 79:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        analy.system_active_detection(message,"Sub-Zero\n\n🔍Вероятность: " + str(res) + "%")
        bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        s = bot.send_message(chat_id=message.chat.id,text="🛡 Обнаружен спам\n⚙️ Алгоритм: Саб-Зиро\n🤖 Пользователь: " + " " + "[" + message.from_user.first_name +  "]" + "(tg://user?id=" + str(message.from_user.id) + ") " + "\n\n👊 Действие: удалить сообщение и заблокировать",parse_mode="Markdown")
        timer_msg.mmm(s)
        statistic.set_stat("sub_zero",0)
    if res > 60 and res < 80:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        analy.system_active_detection(message,"Sub-Zero\n\n🔍Вероятность: " + str(res) + "%")
        s = bot.send_message(chat_id=message.chat.id,text="🛡 Обнаружен спам\n⚙️ Алгоритм: Саб-Зиро\n🤖 Пользователь: " + " " + "[" + message.from_user.first_name +  "]" + "(tg://user?id=" + str(message.from_user.id) + ") " + "\n\n👊 Действие: удалить сообщение",parse_mode="Markdown")
        timer_msg.mmm(s)
        statistic.set_stat("sub_zero",0)
    if res > 25 and res < 51:
        analy.system_active_detection(message,"Sub-Zero\n\n🔍Вероятность: " + str(res) + "%")
    if res < 26:
        passive_defence.detector_spamer(message)
