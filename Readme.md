# YouTube Playlist Scraper

Данное приложение автоматизирует процесс сбора информации о плейлисте на YouTube.
Оно использует веб-скрапинг для извлечения как заголовка плейлиста, так и названий
всех видео в этом плейлисте. Собранная информация сохраняется в текстовый файл для последующего использования.
Приложение может быть полезно, например, для анализа содержания плейлиста или для создания текстового описания его содержимого.

Вкратце, вот что делает каждый основной шаг:

Открывает веб-страницу: Сначала код открывает указанный URL плейлиста на YouTube через браузер Chrome.

Скроллинг: Чтобы убедиться, что все видео в плейлисте загружены на странице, код скроллит страницу вниз два раза.

Парсинг HTML: Извлекает HTML-код страницы и использует BeautifulSoup для его парсинга.

Извлечение информации: Находит и сохраняет заголовок плейлиста и названия всех видео.

Сохранение в файл: Все собранные названия и заголовок плейлиста сохраняются в текстовый файл.

Вывод информации: Названия видео и заголовок плейлиста выводятся на экран.

Закрытие браузера: После всех операций браузер закрывается.

Дорогой друг, надеюсь, это описание поможет вам понять, как работает данное приложение! 🌟

## Импорт библиотек

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

- BeautifulSoup: Для парсинга HTML.
- webdriver: Интерфейс для управления браузером.
- Keys: Эмуляция клавиш.
- time: Для задержки.
- By: Для указания типа селектора при поиске элементов.

## Инициализация драйвера Chrome

driver = webdriver.Chrome()

## Открыть URL

url = "<https://www.youtube.com/watch?v=dAfYYhC0RFQ&list=PLq89pZIwXSou6UxWQahrfRUGYpta43md4>"
driver.get(url)

## Скроллинг страницы

elem = driver.find_element(By.TAG_NAME, 'html')
elem.send_keys(Keys.END)
time.sleep(3)
elem.send_keys(Keys.END)
Здесь мы скроллим страницу вниз, чтобы загрузить все видео в плейлисте.

## Получение HTML страницы

innerHTML = driver.execute_script("return document.body.innerHTML")

## Парсинг HTML

page_soup = bs(innerHTML, 'html.parser')

## Получение названия плейлиста

playlist_title_element = page_soup.find('yt-formatted-string', {'class': 'title style-scope ytd-playlist-panel-renderer complex-string'})
playlist_title = playlist_title_element.text if playlist_title_element else "Unknown"

## Получение названий видео

res = page_soup.find_all('span', {'class': 'style-scope ytd-playlist-panel-video-renderer'})
titles = []
for video in res:
    if video.get('title') != None:
        titles.append(video.get('title'))

## Сохранение названий в файл

with open('video_titles.txt', 'w', encoding='utf-8') as f:
    f.write(f"Заголовок плейлиста: {playlist_title}\n")
    f.write('\n')
    for title in titles:
        f.write(f"{title}\n")

## Вывод названий

print(f"Заголовок плейлиста: {playlist_title}")
for title in titles:
    print(title)

## Закрыть браузер

driver.close()
