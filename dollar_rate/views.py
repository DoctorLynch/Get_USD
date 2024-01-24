import os
import time
from datetime import datetime
from django.shortcuts import render
import requests

Api_key = os.getenv('API_KEY')

new_dollar_rate = {}
last_10_values = []
USD_RUB_API_URL = f'https://api.currencyapi.com/v3/latest?apikey={Api_key}&currencies=RUB'


def index(request):
    response = requests.get(USD_RUB_API_URL)
    dollar_rate = response.json()
    new_dollar_rate['Последнее обновление'] = dollar_rate['meta']
    new_dollar_rate['Курс доллара на сегодня'] = dollar_rate['data']['RUB']['value']
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    new_dollar_rate['Время обновления'] = current_time
    last_10_values.append(new_dollar_rate)
    if len(last_10_values) > 10:
        last_10_values.pop(0)
    context = {
        'dollar_rate': last_10_values
    }
    time.sleep(10)

    return render(request, 'dollar_rate/index.html', context)
