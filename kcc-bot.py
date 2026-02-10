import telebot

TOKEN = "8466452797:AAHKB85Uf3_Tnp6tqDnfGMgoNLtJO8iQZfY"   # BotFather token

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 KCC Bot working!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

print("Bot running...")
bot.infinity_polling()
