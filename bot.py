import os
import telebot
from yt_dlp import YoutubeDL

BOT_TOKEN = os.getenv("8258797267:AAHyqL4JJRV380I1rLYFg1J9NKnyNonCNpw")
bot = telebot.TeleBot("8258797267:AAHyqL4JJRV380I1rLYFg1J9NKnyNonCNpw")
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Kirim link YouTube untuk download lagunya!")

@bot.message_handler(func=lambda m: True)
def download(message):
    url = message.text
    bot.reply_to(message, "Sedang download...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm", ".mp3")

    with open(filename, 'rb') as f:
        bot.send_audio(message.chat.id, f)

bot.polling()
