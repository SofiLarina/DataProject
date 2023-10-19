"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""

import requests
def random_cats():
    for i in range(2):
        response = requests.get("https://cataas.com/cat")
        with open(f"cat{i}.jpg", "wb") as f:
            f.write(response.content)

def original():
    images = ["https://cataas.com/cat/cute", "https://cataas.com/cat/cool"]
    for i, image_url in enumerate(images):
        response = requests.get(image_url)
        with open(f"cat{i}.jpg", "wb") as f:
            f.write(response.content)

def pixelated():
    images = ["https://cataas.com/cat", "https://cataas.com/cat"]
    for i, image_url in enumerate(images):
        response = requests.get(f"{image_url}?filter=pixel")
        with open(f"pixelated{i}.jpg", "wb") as f:
            f.write(response.content)

random_cats()
original()
pixelated()