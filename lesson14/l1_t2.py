import requests
from bs4 import BeautifulSoup
import lxml

cookies = {
    'stest201': '1',
    'stest207': 'acc1',
    'stest209': 'ct2',
    'tp_city_id': '38733',
    'PHPSESSID': 'de2afc3241e8c672578296d7a10a8fbb',
    'user_public_id': 'hRzUyi%2BOBeD7L45v4D5D6Zd%2Fp4rs6LeiA0JluAB2%2F8DY3wnX3ywpiFSwyi1WX9DA',
    'expId': 'PRozp8kCSgK4duzzxjym7w',
    'expVar': '0',
    '_slid': '653258f83abf2a36440b3ab8',
    '_gcl_au': '1.1.1359496991.1697798392',
    '_ym_uid': '1697798392754120215',
    '_ym_d': '1697798392',
    '_gid': 'GA1.2.1696711764.1697798393',
    'tmr_lvid': '403eb0433f5fd3ca3f02e6e4d5dbbea6',
    'tmr_lvidTS': '1697798393692',
    '_rc_sess': 'b08c0798-c410-4f81-9eee-b76ce2123413',
    'uxs_uid': '01b56900-6f35-11ee-be24-d1cfa2399bff',
    'tp_campaign_url': 'https%3A%2F%2Fsochi.technopark.ru%2Fsmartfony%2F%3Futm_referrer%3Dhttps%253A%252F%252Fjazz.sber.ru%252F',
    'tp_referrer': 'https%3A%2F%2Fjazz.sber.ru%2F',
    '_slid_server': '653258f83abf2a36440b3ab8',
    '_ym_isad': '2',
    '_rc_uid': 'b069ab4f3584b31cfa4b1867d88b9f62',
    'adrdel': '1',
    'adrcid': 'A8kHABD-bIgZKDjyfw7mfbg',
    'afUserId': '37289de3-7f1e-4107-9db6-38535bb26bdc-p',
    'AF_SYNC': '1697798397714',
    '_userGUID': '0:lnyhby9j:YlP48BUweEp4DbxlhAvouizbHK5RKji1',
    'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22{%5C%22client_id%5C%22:%5C%22[chat]%20340fe561000616168edd%5C%22%2C%5C%22client_token%5C%22:%5C%22f8a322776d4d4750d33cd5b97fdb726c%5C%22}%22}',
    'promo500closed': 'true',
    'pageviewTimerFired15': 'true',
    'pageviewTimerFired30': 'true',
    'pageviewTimerFired60': 'true',
    '_slsession': '6802D26F-FA16-4436-961C-C5C1533AF4E0',
    '_ym_visorc': 'b',
    'dSesn': '0190a0ee-476b-6e47-9437-61d832f0563e',
    '_dvs': '0:lnyl2gsx:to6PlDV4oVpG3uiXwLaqpkijNSWDHqgT',
    'qrator_jsid': '1697804537.884.1HceddhVnxkSxAYM-962o6s1rdpr81qkhiqn917aipnmpcbnq',
    'visitedPagesNumber': '20',
    '_ga': 'GA1.2.283182757.1697798393',
    'mindboxDeviceUUID': '966cf1e3-a3ec-43c5-81cf-0765327c828e',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22966cf1e3-a3ec-43c5-81cf-0765327c828e%22%7D',
    'tmr_detect': '0%7C1697805637621',
    '_ga_RD4H4CBNJ3': 'GS1.1.1697804537.3.1.1697805698.54.0.0',
    'pageviewTimer': '2993.7089999999994',
}

headers = {
    'authority': 'sochi.technopark.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    # 'cookie': 'stest201=1; stest207=acc1; stest209=ct2; tp_city_id=38733; PHPSESSID=de2afc3241e8c672578296d7a10a8fbb; user_public_id=hRzUyi%2BOBeD7L45v4D5D6Zd%2Fp4rs6LeiA0JluAB2%2F8DY3wnX3ywpiFSwyi1WX9DA; expId=PRozp8kCSgK4duzzxjym7w; expVar=0; _slid=653258f83abf2a36440b3ab8; _gcl_au=1.1.1359496991.1697798392; _ym_uid=1697798392754120215; _ym_d=1697798392; _gid=GA1.2.1696711764.1697798393; tmr_lvid=403eb0433f5fd3ca3f02e6e4d5dbbea6; tmr_lvidTS=1697798393692; _rc_sess=b08c0798-c410-4f81-9eee-b76ce2123413; uxs_uid=01b56900-6f35-11ee-be24-d1cfa2399bff; tp_campaign_url=https%3A%2F%2Fsochi.technopark.ru%2Fsmartfony%2F%3Futm_referrer%3Dhttps%253A%252F%252Fjazz.sber.ru%252F; tp_referrer=https%3A%2F%2Fjazz.sber.ru%2F; _slid_server=653258f83abf2a36440b3ab8; _ym_isad=2; _rc_uid=b069ab4f3584b31cfa4b1867d88b9f62; adrdel=1; adrcid=A8kHABD-bIgZKDjyfw7mfbg; afUserId=37289de3-7f1e-4107-9db6-38535bb26bdc-p; AF_SYNC=1697798397714; _userGUID=0:lnyhby9j:YlP48BUweEp4DbxlhAvouizbHK5RKji1; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22{%5C%22client_id%5C%22:%5C%22[chat]%20340fe561000616168edd%5C%22%2C%5C%22client_token%5C%22:%5C%22f8a322776d4d4750d33cd5b97fdb726c%5C%22}%22}; promo500closed=true; pageviewTimerFired15=true; pageviewTimerFired30=true; pageviewTimerFired60=true; _slsession=6802D26F-FA16-4436-961C-C5C1533AF4E0; _ym_visorc=b; dSesn=0190a0ee-476b-6e47-9437-61d832f0563e; _dvs=0:lnyl2gsx:to6PlDV4oVpG3uiXwLaqpkijNSWDHqgT; qrator_jsid=1697804537.884.1HceddhVnxkSxAYM-962o6s1rdpr81qkhiqn917aipnmpcbnq; visitedPagesNumber=20; _ga=GA1.2.283182757.1697798393; mindboxDeviceUUID=966cf1e3-a3ec-43c5-81cf-0765327c828e; directCrm-session=%7B%22deviceGuid%22%3A%22966cf1e3-a3ec-43c5-81cf-0765327c828e%22%7D; tmr_detect=0%7C1697805637621; _ga_RD4H4CBNJ3=GS1.1.1697804537.3.1.1697805698.54.0.0; pageviewTimer=2993.7089999999994',
    'if-none-match': '"118419-JYWpOrKbqfHvpcxt00NDb5Qunzo"',
    'referer': 'https://sochi.technopark.ru/smartfony/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36',
}

response = requests.get('https://sochi.technopark.ru/smartfony/', cookies=cookies, headers=headers)
with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)
with open("page.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file.read(), "lxml")
    print(soup.prettify())
    container = soup.find("div", class_="catalog-listing")
    cards = container.find_all("div", class_="product-card-big__container")
    print(container)