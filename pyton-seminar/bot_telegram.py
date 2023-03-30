import telebot
import wikipedia
import re
bot = telebot.TeleBot('6027879652:AAE1_b4KZ_bgixkdyYhKD-9j4pZ6vM5UY5Q')
wikipedia.set_lang("ru")



    


# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет')

# @bot.message_handler(content_types=['text'])
# def answer(message):
#      if message.text == "Привет":
#          bot.send_message(message.from_user.id, "Показать что есть на википедии?")
#      elif message.text == "Покажи":
#           bot.send_message(message.from_user.id, "Ща")


@bot.message_handler(commands=["go"])
def go(m, res=False):
    bot.send_message(
        m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')





@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


def getwiki(s):
    try:
        ny = wikipedia.page(s)

        wikitext = ny.content[:1000]

        wikimas = wikitext.split('.')

        wikimas = wikimas[:-1]

        wikitext2 = ''

        for x in wikimas:
            if not ('==' in x):

                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2+x+'.'
            else:
                break

        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'В энциклопедии нет информации об этом'




bot.polling(none_stop=True, interval=0)