"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов всех персонажах начиная с
вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""

import requests
import json

start = 11
end = start * 5

response = requests.get(f'https://rickandmortyapi.com/api/character/{start},{end}')
data = response.json()

characters = []
for result in data:
    name = result['name']
    planet = result['origin']['name']
    episodes = result['episode']
    characters.append({'name': name, 'planet': planet, 'episodes': episodes})

with open('characters.json', 'w') as f:
    json.dump(characters, f)

print('Characters saved to characters.json file')