import datetime

import ephem


def planet_dialogue(update, context):
    date_now = datetime.date.today().strftime("%y/%m/%d")
    planet_for_search = ephem.Planet
    planet_name = update.message.text.split('/planet')[1].capitalize().strip()
    # Search planet in planet list
    try:
        planet = getattr(ephem, planet_name)
        if planet:
            if planet == ephem.Earth():
                update.message.reply_text(
                    'We are on Earth, from our point of view, '
                    'we are not in a constellation')
            else:
                planet_for_search = planet
    except AttributeError:
        update.message.reply_text('Planet not found')
        return
    # calculate actual constellation fot planet
    planet_for_search.compute(date_now)
    constellation_text = ephem.constellation(planet_for_search)[1]
    update.message.reply_text(f'This planet is now in constellation '
                              f'{constellation_text}')
