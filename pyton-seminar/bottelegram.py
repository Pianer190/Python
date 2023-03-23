import telebot

token = '6027879652:AAE1_b4KZ_bgixkdyYhKD-9j4pZ6vM5UY5Q'
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(messeg):
    bot.send_message(messeg.chat.id,'Привет,хрен')

@bot.message_handler(content_types=['text'])
def answer(messeg):
    if messeg.text.lower()=='Нормально':
      bot.send_message(messeg.chat.id,'ну и пошёл ты')






bot.polling(non_stop=True)