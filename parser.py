import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
URL = 'https://www.akchabar.kg/ru/exchange-rates/'
FILE = 'curs.csv'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101', 'Accept': '*/*'}


def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('table', id="rates_table")
    result = items.find_all('tr')
    global curs
    curs = []
    for item in result:
        data3 = [i.text for i in item.find_all('th')]
        data2 = [i.text for i in item.find_all('td')]
        z = data3 + data2
        curs.append(z)
        print(curs)
    return curs


def save_file(path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        for i in curs:
            writer.writerow(i)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        save_file(FILE)
    else:
        print('ERROR')
parse()