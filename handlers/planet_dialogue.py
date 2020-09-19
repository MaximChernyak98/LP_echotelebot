import datetime

import ephem


def planet_dialogue(update, context):

    date_now = datetime.date.today().strftime("%y/%m/%d")
    planet_name_b = update.message.text.split('/planet')[1].strip()
    planet_name = planet_name_b.capitalize()
    planets_list = [
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune'
    ]
    # Search planet in planet list
    if planet_name in planets_list:
        if planet_name == 'Earth':
            update.message.reply_text('We are on Earth, from our point of view, '
                                      'we are not in a constellation ')
        else:
            try:
                planet_for_search = getattr(ephem, planet_name)()
            except AttributeError:
                update.message.reply_text('Check planet name')
                return
    else:
        update.message.reply_text('Planet not found')
        return
    # calculate actual constellation fot planet
    planet_for_search.compute(date_now)
    constellation_text = ephem.constellation(planet_for_search)[1]
    update.message.reply_text(f'This planet is now in constellation '
                              f'{constellation_text}')
