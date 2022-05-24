import requests as r
from datetime import datetime

def get_wether(citi):
    key = '1436b9b77788b942076019327b6abc1d'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    headers = {
        'q': citi.capitalize(),
        'appid': key,
        'lang': 'ru',
        'units': 'metric'
    }
    response = r.get(url, params=headers)
    if response.status_code == 200:
        data = response.json()
        today = datetime.today()
        forecats = []
        for line in data['list']:
            date = datetime.fromtimestamp(line['dt'])
            if date.day == today.day:
                day = {'date': date,
                       'temp': line['main']['temp'],
                       'weather': line['weather'][0]['description']}
                forecats.append(day)
            elif date.day == today.day + 1:
                day = {'date': date,
                       'temp': line['main']['temp'],
                       'weather': line['weather'][0]['description']}
                forecats.append(day)
        return forecats
    else:
        return None
whether = get_wether('Москва')

for day in whether:
    print(datetime.strftime(day['date'], '%d.%m, %H:%M'), day['temp'], day['weather'])