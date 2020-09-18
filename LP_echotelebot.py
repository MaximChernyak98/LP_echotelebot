from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
)
import logging

# from config import TELEGRAM_BOT_ID
import config
from states import States
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
    updater = Updater(
        token=config.TOKEN,
        use_context=True
    )
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', greeting)],

        states={

            States.START: [CommandHandler('start', greeting)],
            States.PLANET: [CommandHandler('planet', planet_dialogue)],
            States.WORDCOUNT: [CommandHandler('wordcount', wordcount_message)],
            States.FULL_MOON: [MessageHandler(Filters.text, full_moon_dialogue)],
            States.ECHO: [MessageHandler(Filters.text, talk_to_me)]
        },

        fallbacks=[
            CommandHandler('start', greeting)
        ]
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
