'''
Установите модуль ephem
Добавьте в бота команду /planet, которая будет принимать на вход название
планеты на английском, например /planet Mars
В функции-обработчике команды из update.message.text получите
название планеты (подсказка: используйте .split())
При помощи условного оператора if и ephem.constellation
научите бота отвечать, в каком созвездии сегодня находится планета.
'''

import logging
import datetime
import re

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

import config


logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    update.message.reply_text('дошел')
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet_dialogue(update, context):
    date_now = datetime.date.today().strftime("%y/%m/%d")
    planet_for_search = ephem.Planet
    planet_name = update.message.text.split('/planet')[1].lower().strip()
    # Search planet in planet list
    if planet_name == 'mercury':
        planet_for_search = ephem.Mercury()
    elif planet_name == 'venus':
        planet_for_search = ephem.Venus()
    elif planet_name == 'earth':
        update.message.reply_text(
            'We are on Earth, from our point of view,'
            ' we are not in a constellation')
        return
    elif planet_name == 'mars':
        planet_for_search = ephem.Mars()
    elif planet_name == 'jupiter':
        planet_for_search = ephem.Jupiter()
    elif planet_name == 'saturn':
        planet_for_search = ephem.Saturn()
    elif planet_name == 'uranus':
        planet_for_search = ephem.Uranus()
    elif planet_name == 'neptune':
        planet_for_search = ephem.Neptune()
    else:
        update.message.reply_text('Planet not found')
        return
    # calculate actual constellation fot planet
    planet_for_search.compute(date_now)
    constellation_text = ', '.join(ephem.constellation(planet_for_search))
    update.message.reply_text(
        'This planet is now in constellations ' + constellation_text)


def wordcount_message(update, context):
    user_message = update.message.text.split('/wordcount')[1].strip()
    words_list = user_message.split(" ")
    good_words = []
    ban_words = []
    # separating understandable words from symbols
    for word in words_list:
        word = re.sub('[, .!?]', '', word)
        if word.isalpha():
            good_words.append(word)
        else:
            ban_words.append(word)
    if user_message:
        # choosing the correct ending
        num_words = len(good_words)
        num_w_rem_10 = num_words % 10
        num_w_rem_100 = num_words % 100
        text_words = ''
        # 1, 21, 31... 101, 201 but not 11, 111, 211
        if num_w_rem_10 == 1 and num_w_rem_100 != 11:
            text_words = 'слово'
        # 2, 3, 4... 102, 103 but not 12, 13, 14, 112, 113...
        elif num_w_rem_10 in [2, 3, 4] and num_w_rem_100 not in [12, 13, 14]:
            text_words = 'слова'
        else:
            text_words = 'слов'
        # print result
        update.message.reply_text(f'Введено {len(good_words)} {text_words}')
        if ban_words:
            update.message.reply_text('Данные слова не засчитаны'
                                      f'{", ".join(ban_words)}')
    else:
        update.message.reply_text('В строке не найдены слова')


def full_moon_dialogue(update, context):
    if update.message.text == 'Когда ближайшее полнолуние?':
        date_now = datetime.date.today().strftime("%Y/%m/%d")
        reply_next_full_moon = ephem.next_full_moon(date_now)
        update.message.reply_text(reply_next_full_moon)
    else:
        update.message.reply_text('неа')


def main():
    mybot = Updater(token=config.TELEGRAM_BOT_ID, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('Start', greet_user))
    dp.add_handler(CommandHandler('Planet', planet_dialogue))
    dp.add_handler(CommandHandler('Wordcount', wordcount_message))
    dp.add_handler(MessageHandler(Filters.text, full_moon_dialogue))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
