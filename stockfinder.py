import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/A/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36' }

r = requests.get (url)

soup = BeautifulSoup (r.text, 'html.parser')

price = soup.find ('span',  {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
change = soup.find ('span', {'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor) data-reactid="32">+1.26 (+0.71%)'}).text

print (price, change)
