import requests
from bs4 import BeautifulSoup
import pandas as pd

page =1
max_page=5
url = 'https://kokos.com.ua/oneplus-phones/' 
r = requests.get(url)
soup = BeautifulSoup(r.text)
tables=soup.find_all ('li',{'class': 'catalog-list catalogGrid __solid __3to5'})

with open('test.html', 'w') as output_file:
  output_file.write(r.text)