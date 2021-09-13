import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-volkswagen/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'accept': '*/*'
}
HOST = 'https://auto.ria.com'

def get_html(url, params=None):  # Передаем в функцию ссылку и номер страницы
    r = requests.get(url, headers=HEADERS, params=params)
    return r

'''def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1'''

def get_content(html,):  # Передаем html конструктору
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_='proposition')  # Указываем в каких тэгах нужная информация

    cars = []   # Почему не соварь списков, а список словарей, потому что нужно \
                # получить key 'items' и values 'название тачек'
    for item in items:
        uah_price = item.find('span', class_='size16')
        a_tag = item.find('a', class_="proposition_link")
        if a_tag:
            a_tag = HOST + a_tag['href']
        else:
            a_tag = 'Link not found'
        if uah_price:
            uah_price = uah_price.get_text()
        else:
            uah_price = 'Цену уточняйте'
        cars.append({
            'title': item.find('div', class_="proposition_title").get_text(strip=True),
            'link': a_tag,
            #'usd': item.find('span', class_='green').get_text(strip=True),
            'uah_price': uah_price,
        })
    print(cars)
    print(len(cars))

    '''for item in items:
        uah_price = item.find('span', class_='size16')
        a_tag = item.find('a', class_="proposition_link")
        if a_tag:
            a_tag=HOST+a_tag.get_text()['href']
            if uah_price:
                uah_price = uah_price.get_text()
            else:
                uah_price = 'Цену уточняйте'
            cars.append({
                'title': item.find('div', class_="proposition_title").get_text(strip=True),
                'link': HOST + a_tag['href'],
                'usd': item.find('span', class_='green').get_text(strip=True),
                'uah_price': uah_price,
                'city': item.find('span', class_='region').get_text(strip=True)
            })

    print(cars)
    print(len(cars))'''

def parse():
    html = get_html(URL)
    print(html.status_code)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()


