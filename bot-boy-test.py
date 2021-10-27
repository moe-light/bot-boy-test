import os
import telebot
from telebot import types

token = os.environ['API_Token']

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(msg):
  markup = types.ReplyKeyboardMarkup(row_width=2)
  itembtn1 = types.KeyboardButton('salam')
  itembtn2 = types.KeyboardButton('oodafez')
  markup.add(itembtn1, itembtn2)
  bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)



bot.infinity_polling()
