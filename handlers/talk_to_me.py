from states import States


def talk_to_me(update, context):
    update.message.reply_text('дошел')
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

    return None
