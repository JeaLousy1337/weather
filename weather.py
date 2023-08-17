from pywebio.input import input as pw_input
from pywebio.output import put_success, put_warning, toast
import pyowm

weather = True

while weather is True:
    if weather is False:
        break
    city = pw_input("Введите свой город:")
    owm = pyowm.OWM('9a841d6c2d67f9309cb359f37e051f6b')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    if temp > 20:
        put_success(f'В городе {city} сейчас {temp} градусов, можно одеваться достаточно легко \U0001F305')
    else:
        put_warning(f'В городе {city} сейчас {temp} градусов, достаточно холодно, одевайся потеплее \U0001F976')
