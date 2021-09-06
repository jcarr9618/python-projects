import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/A/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36' }

r = requests.get (url)

soup = BeautifulSoup (r.text, 'html.parser')

price = soup.find ('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[0].text
change = soup.find ('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[1].text


print (price, change)
