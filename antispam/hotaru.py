import pickle
import telebot
import config
from db import analy,timer_msg,statistic
from filters import passive_defence
import warnings
def warn(*args, **kwargs):
    pass
warnings.warn = warn
filename3 = 'datasets/MLPClassifier.sav'
loaded_mode3 = pickle.load(open(filename3, 'rb'))
bot = telebot.TeleBot(config.token)

def antispam(message):
    if message.text is not None:
        text = message.text
    if message.caption is not None:
        text = message.caption
    neuro_fighter = loaded_mode3.predict([text])
    if int(neuro_fighter[0]) == 2:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        analy.system_active_detection(message,"Хатару")
        s = bot.send_message(chat_id=message.chat.id,text="🛡 Обнаружен спам\n⚙️ Алгоритм: Хаттару\n🤖 Пользователь: " + " " + "[" + message.from_user.first_name +  "]" + "(tg://user?id=" + str(message.from_user.id) + ") " + "\n\n👊 Действие: удалить сообщение и заблокировать",parse_mode="Markdown")
        timer_msg.mmm(s)
        statistic.set_stat("hotaru",0)
    else:
        passive_defence.detector_spamer(message)
