import requests
from bs4 import BeautifulSoup
import datetime
#from parsing import pars
import telebot
import threading
import re
token = ' 6027879652:AAE1_b4KZ_bgixkdyYhKD-9j4pZ6vM5UY5Q'
bot = telebot.TeleBot(token)
nomber = 0

@bot.message_handler(commands=["start"])
def Hello(massage):
    markup = telebot.types.ReplyKeyboardMarkup
    item1 = telebot.types.KeyboardButton('Рандомное число')
    item2 = telebot.types.KeyboardButton('Знак задиака')
    item1 = telebot.types.KeyboardButton('Привет')

bot.polling(none_stop=True, interval=0)