from db import join,analy,get_settings
import telebot
import config
bot = telebot.TeleBot(config.token)

def kill(message):
    try:
        print("but_kill")
        ss = get_settings.get_but_kill(message)
        print(ss)
        if message.json["reply_markup"]["inline_keyboard"][0][0]["url"] != None and ss == False:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except:
        pass
