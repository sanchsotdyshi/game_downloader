"""
Скрипт для скачивания игр с сайта online-fix.me
без регистрации и ожидания
"""

import bs4
import requests
from bs4 import BeautifulSoup

#Запрашиваем название игры и создаем url
game = input('Название игры: ')
game_name = game.replace(' ', '%20')
url = 'https://onlinefixuploads.ru/torrents/' + game_name + '/'

#Создаем сессию и по url запрашиваем страницу
s = requests.Session()
headers = {
	'Referer': 'https://online-fix.me/',	
}
page = s.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'lxml')

#В полученной странице ищем название файла
links = soup.find_all('a')
for link in links:
		if '.torrent' in link.text:
			file_name = link.get('href')


#Создаем url для файла игры, запрашиваем его и сохраняем в папке
file_url = 'https://onlinefixuploads.ru/torrents/' + game_name + '/' + file_name
headers_2 = {
	'Referer': 'https://onlinefixuploads.ru/torrents/Inertial%20Drift/',
}
game_file = s.get(file_url, headers=headers_2)
open(file_name, 'wb').write(game_file.content)



