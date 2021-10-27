import os
import telebot

token = os.environ['API_Token']

bot = telebot.TeleBot('1623472418:AAF2w6XOtXqyqCqiNL709SG-3mDshlRO8to')

@bot.message_handler(commands=['start'])
def start(msg):
  bot.reply_to(msg, 'سلام من هنوز زندم')

bot.polling()
