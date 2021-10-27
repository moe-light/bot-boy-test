import os
import telebot

token = os.environ['API_Token']

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(msg):
  bot.reply_to(msg, 'سلام من هنوز زندم')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
  
bot.polling()
