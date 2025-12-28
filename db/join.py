from pymongo import MongoClient
from menu import razemntka
import telebot
import config
from lang import ru
from datetime import datetime, timedelta
bot = telebot.TeleBot(config.token)

client = MongoClient()
db = client['burgerdefenser']
groups = db.groups
captha = db.captha

def mes_jo(message):
    request = groups.find_one({"chat": message.chat.id})
    if request == None:
        globalis = {"title": message.chat.title,
                "chat": message.chat.id,
                "antispam": "hotary",
                "but_kill": True,
                "link": True,
                "smile": True,
                "capcha": False}
        post_id = groups.insert_one(globalis).inserted_id
        bot.send_message(chat_id=message.chat.id,text=ru.welcom_messages,reply_markup=razemntka.welcome_but())

def join_request(message):
    request = groups.find_one({"chat": message.chat.id})
    if request == None:
        globalis = {"title": message.chat.title,
                "chat": message.chat.id,
                "antispam": "hotary",
                "but_kill": True,
                "link": True,
                "smile": True,
                "capcha": False}
        post_id = groups.insert_one(globalis).inserted_id
    s = razemntka.welcome_but()
    bot.send_message(chat_id=message.chat.id,text=ru.welcom_messages,reply_markup=s)

def generation_captha(message):
    #Отправляем сообщение указываем юзера получаем id заносим в базу при нажатии кнопки удаляем с базы если кнопка не была нажата кикаем пользователя по таймеру
    print(4)
    bot.restrict_chat_member(chat_id=message.chat.id,user_id=message.from_user.id,can_send_messages= False)
    print(5)
    s = bot.send_message(chat_id=message.chat.id,text= "👨‍🦱 " + "[" + message.from_user.first_name +  "]" + "(tg://user?id=" + str(message.from_user.id) + ") " + "для входа в чат нажмите кнопку войти",parse_mode="Markdown",reply_markup=razemntka.capcha())
    globalis = {"chat": message.chat.id,
                "user": message.from_user.id,
                "message_id": s.id,
                "time": datetime.strftime(datetime.now() + timedelta(minutes=2), '%H:%M')}
    post_id = captha.insert_one(globalis).inserted_id

def click_welcome(chat,mes,user):
    request = captha.find_one({"chat": chat,
                                "user": user,
                                "message_id": mes})
    if request != None:
        db.captha.delete_one({"chat": chat,
                              "user": user,
                              "message_id": mes})
    return request

def get_welcome(chat,message_id,user):
    request = captha.find_one({"chat": chat,
                                "user": user,
                                "message_id": message_id})
    return request
#При нажатии на кнопку сравниваем привязаный message_id с chat_id и айди юзера при правильном нажатии удаляем сообщение и удаляем из базы
#5 типа антиспама
#Саб-Зиро default
#Фредди Крюгер #cracken
#Хотару neurofighter
#Фрост #last_stronghold
