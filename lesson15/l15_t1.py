import requests
from bs4 import BeautifulSoup
import json
from time import sleep

cookies = {
    'PHPSESSID': 'hh1i1jm1o8lqthrcr6fstvoeav',
    '51a55dae53577255b792d39bfe1d40ac': '1',
    '_ga': 'GA1.1.1966699917.1698057434',
    '_ym_uid': '1698057435190062749',
    '_ym_d': '1698057435',
    '_ym_isad': '2',
    '_ga_BB3QC8QLF4': 'GS1.1.1698057434.1.1.1698057547.0.0.0',
}

headers = {
    'authority': 'zaka-zaka.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.888 YaBrowser/23.9.2.888 Yowser/2.5 Safari/537.36',
}

result = {}
for i in range(1, 15):
    print('Cобираю данные страницы '+ str(i))
    sleep(1)

    response = requests.get('https://zaka-zaka.com/game/new/page'+str(i), cookies=cookies, headers=headers)

    with open('page1.html', 'w', encoding='UTF-8') as f:
        f.write(response.text)
    with open('page1.html', 'r', encoding='UTF-8') as file:
        soup = BeautifulSoup(file.read(), "lxml")
        container = soup.find('div', class_='tabs-content tab-1 active')
        cards = container.find_all('a', class_='game-block')
        for card in cards:
            name = card.find('div', class_='game-block-name').text
            price = card.find('div', class_='game-block-price').text
            if price is not None:
                new_price = ''
                for i in price:
                    if i.isdigit():
                        new_price += i
                result[name] = int(new_price)

print(result)

with open('result1.json', 'w', encoding='UTF-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)