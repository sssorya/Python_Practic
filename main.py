#© Copyright 2023#
# sssorya #


import urllib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests_toolbelt import user_agent, MultipartEncoder
from requests_toolbelt.cookies.forgetful import ForgetfulCookieJar

# Заголовки для имитации браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'}

# URL сайта
url = ''

# Отправляем GET-запрос и получаем HTML-страницу
page = requests.get(url, headers=headers)

# Инициализация BeautifulSoup и парсинг HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Поиск всех контейнеров товаров на странице
containers = soup.find_all('div', class_='n-catalog-item relative grid-item n-catalog-item__product')

# Создание списка для хранения данных
data = []

# Обход контейнеров и получение данных
for c in containers:
    # Получение наименования товара
    name = c.find('span', class_='string bold nowrap n-catalog-item__click-copy').text.strip()
    # Получение цены товара
    price = c.find('div', class_='n-catalog-item__price-box col-12 col-md pr-0 mb-2').text.strip()

    # Запись данных в список
    data.append([name, price])

# Создание pandas DataFrame и сохранение в CSV
df = pd.DataFrame(data, columns=['Name', 'Price'])
df.to_excel('./test.xlsx')


# Показать парсинг таблицу
# print(df)
