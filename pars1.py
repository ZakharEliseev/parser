from bs4 import BeautifulSoup
from bs4.element import Tag
def open_file():
    html = open('table.html','r' ,encoding='utf-8')
    html_sorted = open('html_sorted.html', 'w+',encoding='utf-8')
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div', class_='row')
    table = soup.find('table', class_='table')
    table = str(table)
    title = str(title)
    html_sorted.write(title + table)
    html.close()
    html_sorted.close()
open_file()

