from socket import getnameinfo
import telebot
from telebot import types


token = '6027879652:AAE1_b4KZ_bgixkdyYhKD-9j4pZ6vM5UY5Q'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(content_types=['text'])
def answer(message):
     if message.text == "Привет":
         bot.send_message(message.from_user.id, "Я покажу чему научился?")
     elif message.text == "/help":
          bot.send_message(message.from_user.id, "Покажи")
     
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, getnameinfo); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')








bot.polling(non_stop=True)