import requests as r

url = 'https://api.coinbase.com/v2/currencies'
response = r.get(url)

with open('texts/currencies.txt', 'w', encoding='utf8') as file:
    data = response.json()
    for currency in data['data']:
        file.write(f'{currency["name"]} ({currency["id"]})\n')