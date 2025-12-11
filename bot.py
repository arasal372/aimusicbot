import telebot
‎import os
‎
‎BOT_TOKEN = os.getenv("8258797267:AAHyqL4JJRV380I1rLYFg1J9NKnyNonCNpw")
‎
‎bot = telebot.TeleBot("8258797267:AAHyqL4JJRV380I1rLYFg1J9NKnyNonCNpw")
‎
‎@bot.message_handler(commands=['start'])
‎def start(message):
‎    bot.reply_to(message, "Bot online 24 jam di Render!")
‎
‎@bot.message_handler(func=lambda m: True)
‎def echo(message):
‎    bot.reply_to(message, message.text)
‎
‎bot.infinity_polling()	

