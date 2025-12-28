import telebot
from lang import ru
from db import join,analy,get_settings,edit_antispam
from menu import obrabotchik,razemntka
from analytics import sendr
from antispam import sub_zero,hotaru,forst,frost_plus
import time
import config
from filters import but_kill,passive_defence,smile_defender,chanal_defender
import threading
import timer
bot = telebot.TeleBot(config.token)

def osn(message):
    print(message.chat.id)
    if message.chat.id < 0:
            join.mes_jo(message)
            if get_settings.get_white(message) == None and bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status != "creator" and bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status != "administrator":
        #if bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status != "creator" and bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status != "administrator":
                #print(122222222333)
                if message.text is not None:
                    text = message.text
                if message.caption is not None:
                    text = message.caption
                chanal_defender.one(message)
                d = get_settings.get_antispam(message)
                dd = get_settings.get_spambase(text,message)
                ddd = get_settings.get_white_list(text)
                dddd = get_settings.get_white_user(message.from_user.id)
                ddddd = get_settings.get_link(message)
                youtube = passive_defence.youtube_detector(message)
                dddddd = get_settings.get_smile(message)
                if dddddd == False:
                    smile_defender.smile_defender(message)
                if ddddd == False:
                    passive_defence.link_detector_wat(message)
                passive_defence.delete_spam_list(message)
                but_kill.kill(message)
                if d == "frost_plus" and dd == None and ddd == None and dddd == None:
                    frost_plus.last_defence(message)
                if d == "subzero" and dd == None and ddd == None and dddd == None:
                    print("s")
                    sub_zero.antispam(message)
                if d == "hotary" and dd == None and ddd == None and dddd == None:
                    print("h")
                    hotaru.antispam(message)
                if d == "frost" and dd == None and ddd == None and dddd == None:
                    print("f")
                    forst.last_defence(message)

    print(2)

@bot.message_handler(commands=['add_channel'])
def start(message):
    if bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "creator" or bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "administrator":
        if message.reply_to_message is not None:
            edit_antispam.chanal_add(message)
            bot.reply_to(message,text=ru.add_db_chanal)
        else:
            bot.reply_to(message,text=ru.error_white_list,reply_markup=razemntka.welcome_but())
@bot.message_handler(commands=['del_channel'])
def start(message):
    if bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "creator" or bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "administrator":
        if message.reply_to_message is not None:
            edit_antispam.chanal_delete(message)
            bot.reply_to(message,text=ru.delete_db_chanal)
        else:
            bot.reply_to(message,text=ru.error_white_list,reply_markup=razemntka.welcome_but())

@bot.message_handler(commands=['white_delete'])
def start(message):
    print(1234)
    print(bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status )
    if bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "creator" or bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "administrator":
        obrabotchik.command_white_list_delete(message)

@bot.message_handler(commands=['white_add'])
def start(message):
    print(1234)
    print(bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status )
    if bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "creator" or bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "administrator":
        obrabotchik.command_white_list_add(message)
@bot.message_handler(commands=['ban_youtube'])
def start(message):
    print(1234)
    print(bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status )
    if bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "creator" or bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "administrator":
        obrabotchik.command_ban_youtube(message)

@bot.message_handler(commands=['unban_youtube'])
def start(message):
    if bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "creator" or bot.get_chat_member(chat_id=message.chat.id,user_id=message.from_user.id).status == "administrator":
        obrabotchik.command_unban_youtube(message)

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id > 0:
        bot.reply_to(message, ru.command_start_private,reply_markup=razemntka.welcome_but())
        bot.send_message(chat_id=6826006303,text="Бот запущен в приватном чате")
    else:
        bot.reply_to(message, ru.comand_start_group,reply_markup=razemntka.welcome_but())


@bot.message_handler(commands=['menu'])
def menu(message):
    obrabotchik.main(message)


@bot.message_handler(content_types=["animation"])
def handle_animation(message):
    osn(message)

@bot.message_handler(content_types=["audio"])
def handle_audio(message):
    osn(message)

@bot.message_handler(content_types=["document"])
def handle_document(message):
    osn(message)


@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    osn(message)


@bot.message_handler(content_types=["video"])
def handle_video(message):
    osn(message)


@bot.message_handler(content_types=["voice"])
def handle_voice(message):
    osn(message)



@bot.message_handler(content_types=["file"])
def handle_file(message):
    osn(message)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    osn(message)


@bot.message_handler(content_types=["video"])
def handle_text(message):
    osn(message)

@bot.callback_query_handler(func=lambda call: True)
def ans(call):
    message = call.message
    if call.data == 'welcome':
        print("click")
        obrabotchik.click_welcome(message,call)
    if bot.get_chat_member(chat_id=message.chat.id,user_id=call.from_user.id).status == "creator" or bot.get_chat_member(chat_id=message.chat.id,user_id=call.from_user.id).status == "administrator":
        if call.data == 'antispam':
            obrabotchik.antispam_menu(message,call)
        if call.data == 'frost_plus':
            obrabotchik.click_frost_plus(message)
        if call.data == 'subzero':
            obrabotchik.click_subzero(message)
        if call.data == 'hotary':
            obrabotchik.click_hotary(message)
        if call.data == 'frost':
            obrabotchik.click_frost(message)
        if call.data == "filters":
            obrabotchik.filt_men(message,call)
        if call.data == "url_close" or call.data == "url_open":
            obrabotchik.click_close_url(message,call)
        if call.data == "link_close" or call.data == "link_open":
            obrabotchik.clik_tme(message,call)
        if call.data == "smile_close" or call.data == "smile_open":
            obrabotchik.click_smile(message,call)
        if call.data == "capcha_close" or call.data == "capcha_open":
            obrabotchik.click_capcha(message,call)

    if call.data == 'spam' or call.data == 'warning' or call.data == 'good' or call.data == 'good_white':
        print("ole")
        analy.one(message,call)



@bot.message_handler(content_types=["new_chat_members"])
def handle_text(message):
    for im in message.new_chat_members:
        if im.id == config.bot_id:
            join.join_request(message)
            bot.send_message(chat_id=config.god,text="Бот запущен в публичном чате " + str(message.chat.title))
        else:
            if get_settings.get_capha(message) != True:
                join.generation_captha(message)
t2 = threading.Thread(target=timer.timer, daemon=True)
t2.start()
print(1)
while 1:
    try:
            bot.polling(none_stop=True)
    except:
        time.sleep(15)