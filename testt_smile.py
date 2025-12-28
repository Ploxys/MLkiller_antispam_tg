import telebot
from telebot import types
import json
bot = telebot.TeleBot("7751137910:AAErzifxmNaLmc6ZKYpvn4m_wXjArO83MEs")
markup = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton("Подробнее", url='http://wiki.mlkiller.ru/')
markup.add(button1)
bot.send_message(chat_id=-1002218406620,text="Презентация обновления версии 1.0.6 (Pink Pig)\n\nМы рады представить вам новое обновление нашего бота! В версии 1.0.6 мы внедрили несколько значительных улучшений:\n\n• Смайл-защита: Теперь ваша безопасность на первом месте! Узнайте подробнее о смайл-защите, нажав кнопку ниже.\n\n• Редактированное приветственное меню: Мы сделали его более удобным и информативным.\n\n• Оптимизация бота: Улучшена производительность для более быстрого и плавного взаимодействия.\n\n• Изменение меню настроек: Теперь настройки стали еще более интуитивными.\n\nСпасибо, что остаетесь с нами!",reply_markup=markup)
