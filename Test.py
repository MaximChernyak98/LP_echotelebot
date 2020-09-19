import datetime

import ephem


def planet_dialogue():
    date_now = datetime.date.today().strftime("%y/%m/%d")
    planet_for_search = ephem.Planet
    planet_name = input('Введите имя планеты: ').capitalize()
    # Search planet in planet list
    planet = getattr(ephem, planet_name)()
    planet_test = ephem.Mars()
    print(planet)
    print(planet_test)
    print(planet == planet_test)
    print(planet.compute(date_now))
    # if planet:
    #     if planet.__name == ephem.Earth():
    #         print(
    #             'We are on Earth, from our point of view, '
    #             'we are not in a constellation')
    #     else:
    #         planet_for_search = planet
    # # except AttributeError:
    # #     print('Planet not found')
    # #     return
    # # calculate actual constellation fot planet
    # planet_for_search.compute(date_now)
    # constellation_text = ephem.constellation(planet_for_search)[1]
    # print(f'This planet is now in constellation '
    #       f'{constellation_text}')


planet_dialogue()
