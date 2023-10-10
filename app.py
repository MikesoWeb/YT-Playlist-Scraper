from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

url = "https://www.youtube.com/watch?v=dAfYYhC0RFQ&list=PLq89pZIwXSou6UxWQahrfRUGYpta43md4"
driver.get(url)

elem = driver.find_element(By.TAG_NAME, 'html')
elem.send_keys(Keys.END)
time.sleep(3)
elem.send_keys(Keys.END)

innerHTML = driver.execute_script("return document.body.innerHTML")

page_soup = bs(innerHTML, 'html.parser')

# Извлечение названия плейлиста
playlist_title_element = page_soup.find(
    'yt-formatted-string', {'class': 'title style-scope ytd-playlist-panel-renderer complex-string'})
playlist_title = playlist_title_element.text if playlist_title_element else "Unknown"

# Извлечение названий видео
res = page_soup.find_all(
    'span', {'class': 'style-scope ytd-playlist-panel-video-renderer'})
titles = []
for video in res:
    if video.get('title') != None:
        titles.append(video.get('title'))

# Сохранение названий в файл
with open('video_titles.txt', 'w', encoding='utf-8') as f:
    f.write(f"Заголовок плейлиста: {playlist_title}\n")
    f.write('\n')
    for title in titles:
        f.write(f"{title}\n")

# Вывод названий построчно
print(f"Заголовок плейлиста: {playlist_title}")
for title in titles:
    print(title)

driver.close()
