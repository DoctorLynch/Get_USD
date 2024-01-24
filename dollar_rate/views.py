import os
import time
from datetime import datetime
from django.shortcuts import render
import requests

Api_key = os.getenv('API_KEY')

new_dollar_rate = {}
last_10_values = []


def index(request):
    for i in range(1, 10):
        response = requests.get(f'https://api.currencyapi.com/v3/latest?apikey={Api_key}&currencies=RUB')
        dollar_rate = response.json()
        new_dollar_rate['Последнее обновление'] = dollar_rate['meta']
        new_dollar_rate['Курс доллара на сегодня'] = dollar_rate['data']['RUB']['value']
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        new_dollar_rate['Время обновления'] = current_time
        last_10_values.append([i, new_dollar_rate])
        context = {
            'dollar_rate': last_10_values
        }
        time.sleep(10)

    return render(request, 'dollar_rate/index.html', context)
