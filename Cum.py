import requests
from lxml import html

url = input('Ссылочка на источник: ')

page = requests.get(url)
tree = html.fromstring(page.content)

a = [x.attrib['src'] for x in tree.cssselect('img') if 'JPG' or 'PNG' in x.attrib['src']]
for pic_link in a:
    dickpic = requests.get(pic_link).content
    with open('CUM'+pic_link[-1]+'.png', 'wb') as f:
        f.write(dickpic)