from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    RegexHandler
)
import logging

# from config import TELEGRAM_BOT_ID
import config
from handlers.greeting import greeting
from handlers.talk_to_me import talk_to_me
from handlers.planet_dialogue import planet_dialogue
from handlers.wordcount import wordcount_message
from handlers.full_moon_dialogue import full_moon_dialogue

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename="bot.log"
)


def main():
    mybot = Updater(
        token=config.TOKEN,
        use_context=True
    )

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('Start', greeting))
    dp.add_handler(CommandHandler('Planet', planet_dialogue))
    dp.add_handler(CommandHandler('Wordcount', wordcount_message))
    dp.add_handler(RegexHandler(pattern=r'Когда ближайшее полнолуние?',
                                callback=full_moon_dialogue))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
