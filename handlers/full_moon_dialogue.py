# standart module
import datetime

# pip module
import ephem


def full_moon_dialogue(update, context):
    if update.message.text == 'Когда ближайшее полнолуние?':
        date_now = datetime.date.today().strftime("%Y/%m/%d")
        reply_next_full_moon = ephem.next_full_moon(date_now)
        update.message.reply_text(reply_next_full_moon)
    else:
        update.message.reply_text('Могу сказать только про полнолуние')
