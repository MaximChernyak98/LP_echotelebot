import datetime

import ephem


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
