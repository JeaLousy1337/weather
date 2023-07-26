import pyowm
city = input("Введите свой город:")
owm = pyowm.OWM('9a841d6c2d67f9309cb359f37e051f6b')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
temp = w.temperature('celsius')["temp"]
print (f'В городе {city} сейчас {temp} градусов')
