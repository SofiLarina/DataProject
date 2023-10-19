"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""

import requests

response = requests.get('https://randomuser.me/api/')
data = response.json()['results'][0]

name = data['name']['first']
country = data['location']['country']
phone = data['phone']

print(f"Hi, I'm {name}, I'm from {country}, my phone number is {phone}")