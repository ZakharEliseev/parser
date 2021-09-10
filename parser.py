import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-jeep/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'accept': '*/*'
}


def get_html(url, params=None):  # Передаем в функцию ссылку и номер страницы
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):  # Передаем html конструктору
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('section', class_='proposition')  # Указываем в каких тэгах нужная информация

    cars = []   # Почему не словарь списков, а список словарей, потому что нужно \
                # получить key 'items' и values 'название тачек'
    for item in items:
        cars.append({
            'title': item.find('div', class_="proposition_title").get_text(strip=True),
            'link': item.find('a', class_="proposition_link").get_text('href'),
        })
    print(cars)
    print(len(cars))


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()

'''s = requests.session()
a = s.get(URL)
csrf_token = s.cookies['csrftoken']

data = {
    'Login':'9792-10',
    'password':'zAUuir',
    'csrfmiddlewaretoken':'csrf_token'
}

d = s.post(URL, data=data, headers=dict(Refer=URL))
dd = s.get('https://vashkontrol.ru/')


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def parse():
    html = get_html(URL)
    print(html)

parse()'''
