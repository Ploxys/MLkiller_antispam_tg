from pymongo import MongoClient
from menu import razemntka
import telebot
from lang import ru
import config
bot = telebot.TeleBot(config.token)

client = MongoClient()
db = client['burgerdefenser']
groups = db.groups
reports = db.reports
neuro = db.neuro_base
spam = db.spam
white_list = db.white_list
white_user = db.white_user
def one(message,call):
    request = reports.find_one({"message_id_a": message.id})
    globalis = {"text": request["text"]}
    if call.data == "spam":
        globalis = {"text": request["text"],
                    "status": 2}
        post_id = neuro.insert_one(globalis).inserted_id
        try:
            bot.delete_message(chat_id=request["chat"], message_id=request["message_id_d"])
        except:
            pass

    if call.data == "warning":
        post_id = spam.insert_one(globalis).inserted_id
        try:
            bot.delete_message(chat_id=request["chat"], message_id=request["message_id_d"])
        except:
            pass

    if call.data == "good":
        post_id = white_list.insert_one(globalis).inserted_id
        globalis = {"text": request["text"],
                    "status": 0}
        post_id = neuro.insert_one(globalis).inserted_id

    if call.data == "good_white":
        post_id = white_list.insert_one(globalis).inserted_id
        globalis = {"text": request["text"],
                    "status": 0}
        post_id = white_user.insert_one({"user_id": request["user"]}).inserted_id
        post_id = neuro.insert_one(globalis).inserted_id
    db.reports.delete_one({"message_id_a": message.id})
    bot.delete_message(message_id=message.id, chat_id=message.chat.id)

def system_active_detection(message,system):
    if message.text is not None:
        text = message.text
    if message.caption is not None:
        text = message.caption
    s = razemntka.create_admin_panel()
    dd = bot.send_message(chat_id=config.god,text="💬 Чат: " + str(message.chat.title) + "\n🌍 Алгоритм: " + str(system) + "\n\n" + str(text),reply_markup=s)
    globalis = {"chat": message.chat.id,
                "user": message.from_user.id,
                "text": text,
                "message_id_d": message.id,
                "message_id_a": dd.id,
                "id_admin": config.god}
    post_id = reports.insert_one(globalis).inserted_id
