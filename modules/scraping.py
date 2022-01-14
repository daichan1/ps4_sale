import time
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary

SCRAPING_COUNT = 1

def run():
  game_data = []
  driver = webdriver.Chrome()

  for i in range(SCRAPING_COUNT):
    url = 'https://store.playstation.com/ja-jp/category/1b6c3e7d-4445-4cef-a046-efd94a1085b7/' + str(i + 1)
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    game_list = soup.find_all('span', class_='psw-t-body')
    price_list = soup.find_all('span', class_='psw-m-r-3')
    for i, game in enumerate(game_list):
      price = int(price_list[i].get_text().replace('￥', '').replace(',', ''))
      game_data.append({ 'title': game.get_text(), 'price': price })
    time.sleep(2)
  
  driver.quit()
  
  return game_data