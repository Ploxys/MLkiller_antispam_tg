import telebot 
import config
bot = telebot.TeleBot(config.token)

def smile_defender(message):
    try:
        if len(message.json["entities"]) > 8:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        #Тут должно быть сообщение оповещение которое удаляется через 2 минуты о том что пользователь заблокирован за подозрительную спам активность
    except:
        pass