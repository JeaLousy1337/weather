import pyowm
city = (input("Введите город:"))
ip = pyowm.OWM('9a841d6c2d67f9309cb359f37e051f6b')
mgr = ip.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
temp = w.temperature('celsius')["temp"]
all_funk = f'городе {city} сейчас {temp} градусов'
print(all_funk)
input()
