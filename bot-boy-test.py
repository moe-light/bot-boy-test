import os
import telebot

bot = telebot.TeleBot(API_Token)

@bot.message_handler(commands=['start'])
def start(msg):
  bot.reply_to(msg, 'سلام من هنوز زندم')

bot.polling()
