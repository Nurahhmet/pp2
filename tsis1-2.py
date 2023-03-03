import requests
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D0%B2%D0%B8_(%D0%BF%D1%82%D0%B8%D1%86%D1%8B)"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html')

print(soup)