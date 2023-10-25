from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options)
driver.get("https://www.aviasales.ru/")
sleep(7)

search_city = driver.find_element(by="xpath", value='//*[@id="avia_form_destination-input"]')
search_city.send_keys("Минск")
sleep(5)
button_data = driver.find_element(by="xpath", value='/html/body/div[7]/div[2]/div/div/div/div/form/div[1]/div/button[1]')
button_data.click()
sleep(5)
button_16 = driver.find_element(by="xpath", value='/html/body/div[7]/div[2]/div/div/div/div/form/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[3]/div[4]/div')
button_16.click()
sleep(0.5)
button_16.click()
sleep(5)
button_back = driver.find_element(by="xpath", value='/html/body/div[7]/div[2]/div/div/div/div/form/div[1]/div[2]/div[1]/div/div/div/div/div/header/div[2]')
button_back.click()
sleep(5)
button = driver.find_element(by="xpath", value='/html/body/div[7]/div[2]/div/div/div/div/form/button')
button.click()

sleep(20)
"""
page = driver.page_source

soup = BeautifulSoup(page, "lxml")
container = soup.find("div", id="h__X9to3ExGtvW7f810u9HW product-list")

list_of_games = container.find_all("div", class_="product-list__item fade-appear-done fade-enter-done")
result = []
for game in list_of_games:
    name = game.find("div", class_="product-list__item fade-appear-done fade-enter-done").text
    result.append(name)
print("Собрали", len(result), "игр")
print("Список собранных игр:", result)
"""