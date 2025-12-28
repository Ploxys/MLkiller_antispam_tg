import pickle
import telebot
import config
from db import analy,timer_msg,statistic
from filters import passive_defence
import warnings
def warn(*args, **kwargs):
    pass
warnings.warn = warn
filename3 = 'datasets/RidgeClassifier.sav'
loaded_mode4 = pickle.load(open(filename3, 'rb'))
bot = telebot.TeleBot(config.token)
def last_defence(message): #RidgeClassifier.sav
    if message.text is not None:
        text = message.text
    if message.caption is not None:
        text = message.caption
    last_stronghold = loaded_mode4.predict([text])
    if int(last_stronghold[0]) == 2:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        analy.system_active_detection(message,"Фрост")
        s = bot.send_message(chat_id=message.chat.id,text="🛡 Обнаружен спам\n⚙️ Алгоритм: Фрост\n🤖 Пользователь: " + " " + "[" + message.from_user.first_name +  "]" + "(tg://user?id=" + str(message.from_user.id) + ") " + "\n\n👊 Действие: удалить сообщение и заблокировать",parse_mode="Markdown")
        timer_msg.mmm(s)
        statistic.set_stat("frost",0)
    else:
        passive_defence.detector_spamer(message)
