import telebot 
from db import get_settings
from lang import ru
import config
bot = telebot.TeleBot(config.token)

def one(message):
    print("1231212")
    print(get_settings.get_bch(message))
    if get_settings.get_bch(message) != None:
        bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)
        bot.send_message(chat_id=message.chat.id,text=ru.delete_chanal)
    