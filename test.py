from pytube import YouTube
from pytube import Channel
import re
#video = "https://www.youtube.com/watch?v=p2IKvHnzyS8"
#x=YouTube(video)
#print(x.channel_id)
def youtube_detector(message):
    regex = r"(?P<domain>\w+\.\w{2,3}\D+\w+)"
    matches = re.finditer(regex, str(message), re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        ss = str("{match}").format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group())
        dd = str(ss).split("/")
        print(dd[0])
        if dd[0] == "youtu.be" or dd[0] == "youtu.be" or dd[0] == "www.youtube.com":
            pass#bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)