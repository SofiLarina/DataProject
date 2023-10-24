"""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options)
driver.get("https://store.steampowered.com/")
sleep(5)

search = driver.find_element(by="id", value="store_nav_search_term")
search.send_keys("Стратегии")
search.send_keys(Keys.ENTER)

sleep(1)
for i in range(50):
    sleep(0.5)
    driver.execute_script("window.scrollBy(0, 1070)")

page = driver.page_source

soup = BeautifulSoup(page, "lxml")
container = soup.find("div", id="search_resultsRows")


list_of_games = container.find_all("div", class_="responsive_search_name_combined")
result = []
for game in list_of_games:
    name = game.find("span", class_="title").text
    result.append(name)
print("Собрали", len(result), "игр")
print("Список собранных игр:", result)
