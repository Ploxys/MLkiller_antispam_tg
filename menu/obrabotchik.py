import telebot
from lang import ru
from menu import razemntka
from db import edit_antispam,join
import config
from lang import ru
import re
import config
bot = telebot.TeleBot(config.token)

def main(message):
    menu = razemntka.menu()
    if message.chat.id > 0:
        bot.reply_to(message, ru.comand_menu_private)
    else:
        bot.reply_to(message, ru.comand_menu_group,reply_markup=menu)

def command_ban_youtube(message):
    if message.text is not None:
        text = message.text
    if message.caption is not None:
        text = message.caption
    regex = r"(?P<domain>\w+\.\w{2,3}\D+\w+)"
    matches = re.finditer(regex, str(message), re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        ss = str("{match}").format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
        dd = str(ss).split("/")
        if dd[0] == "youtu.be" or dd[0] == "youtu.be" or dd[0] == "www.youtube.com":
            ssd = edit_antispam.ban_youtube(message,ss)
            if ssd == True:
                bot.reply_to(message,text=ru.event_add_black_list_youtube)
            if ssd == False:
                bot.reply_to(message,text=ru.event_add_black_list_youtube_faill)
            break

def command_white_list_add(message):
    if message.text is not None:
        text = message.text
    if message.caption is not None:
        text = message.caption
    if message.reply_to_message is not None:
        edit_antispam.white_list_add(message)
        bot.reply_to(message,text=ru.good_white_list_add)
    else:
        bot.reply_to(message,text=ru.error_white_list,reply_markup=razemntka.welcome_but())

def command_white_list_delete(message):
    if message.text is not None:
        text = message.text
    if message.caption is not None:
        text = message.caption
    if message.reply_to_message is not None:
        edit_antispam.white_list_delete(message)
        bot.reply_to(message,text=ru.good_white_list_delete)
    else:
        bot.reply_to(message,text=ru.error_white_list,reply_markup=razemntka.welcome_but())

def command_unban_youtube(message):
    if message.text is not None:
        text = message.text
    if message.caption is not None:
        text = message.caption
    regex = r"(?P<domain>\w+\.\w{2,3}\D+\w+)"
    matches = re.finditer(regex, str(message), re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        ss = str("{match}").format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
        dd = str(ss).split("/")
        if dd[0] == "youtu.be" or dd[0] == "youtu.be" or dd[0] == "www.youtube.com":
            print("very")
            ssd = edit_antispam.unban_youtube(message,ss)
            bot.reply_to(message,text=ru.event_add_black_list_youtube_unban)
            break

def click_close_url(message,call):
    edit_antispam.change_filters(call,message)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

def clik_tme(message,call):
    edit_antispam.change_filters_url(call,message)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

def click_smile(message,call):
    edit_antispam.change_filters_smile(call,message)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
def click_capcha(message,call):
    edit_antispam.change_filters_capcha(call,message)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

def filt_men(message,call):
    menu = razemntka.filters_menu(message)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.id,text=ru.comand_antispam_url_filt,reply_markup=menu)


def antispam_menu(message,call):
    menu = razemntka.antispam_algoritms()
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.id,text=ru.comand_antispam_settings,reply_markup=menu)

def click_frost_plus(message):
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.id,text=ru.click_subzero)
    s = edit_antispam.change_antispam(message,"frost_plus")

def click_subzero(message):
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.id,text=ru.click_subzero)
    s = edit_antispam.change_antispam(message,"subzero")

def click_hotary(message):
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.id,text=ru.click_hotary)
    s = edit_antispam.change_antispam(message,"hotary")

def click_frost(message):
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.id,text=ru.click_frost)
    s = edit_antispam.change_antispam(message,"frost")

def click_welcome(message,call):
    info = join.click_welcome(message.chat.id,message.id,call.from_user.id)
    print(info)
    if info != None:
        if info["chat"] == message.chat.id and info['message_id'] == message.id and info['user'] == call.from_user.id:
            bot.restrict_chat_member(chat_id=message.chat.id,user_id=call.from_user.id,can_send_messages= True)
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)