 import requests

city = 'Moscow,RU'
appid = 'a988307c5269b41d73cce2563aa879d8'

res = requests.get("https://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("\nТекущий прогноз погоды:")
print("\nГород:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Видимость:", data['visibility'])
print("Скорость ветра:", data['wind']['speed'])

res2 = requests.get("https://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data2 = res2.json()

print("\nПрогноз погоды на неделю:\n")
for i in data2['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",
    '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], "> \r\nСкорость ветра < ", i['wind']['speed'], " > \r\nВидимость < ", i['visibility'], " >")
    print("____________________________")
