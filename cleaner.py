import telebot
import config
bot = telebot.TeleBot("7751137910:AAErzifxmNaLmc6ZKYpvn4m_wXjArO83MEs")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    print(message.forward_origin.chat.id)

bot.polling(none_stop=True)
