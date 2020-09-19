import re


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
