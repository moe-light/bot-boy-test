import os
import telebot
from telebot import types

token = os.environ['API_Token']

bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('a')
itembtnv = types.KeyboardButton('v')
itembtnc = types.KeyboardButton('c')
itembtnd = types.KeyboardButton('d')
itembtne = types.KeyboardButton('e')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)

@bot.message_handler(commands=['start'])
def start(msg):
  bot.reply_to(msg, 'سلام من هنوز زندم')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)



bot.infinity_polling()
