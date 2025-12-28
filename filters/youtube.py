from pytube import YouTube
from pytube import Channel
from db import youtu_db
import telebot
bot = telebot.TeleBot(config.token)

def search(message):
    video = "https://www.youtube.com/watch?v=p2IKvHnzyS8"
    x= YouTube(video)
    youtu_db.get_chanals(message,x.channel_id)
    bot.send_message(chat_id=message.chat.id)
