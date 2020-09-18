from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackQueryHandler,
)
import logging
import os

# from config import TELEGRAM_BOT_ID
import config
from states import States
from handlers.greeting import greeting


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

            States.START: [CommandHandler('start', greeting)]
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
