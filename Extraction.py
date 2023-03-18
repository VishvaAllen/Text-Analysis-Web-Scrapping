import requests
from bs4 import BeautifulSoup as bs

url="enter your url here"
page=requests.get(url)
soup=bs(page.content,'html.parser')
title=soup.find('h1',class_='entry-title')
article=soup.find('div', class_='td-post-content')
delete=soup.find('pre',class_='wp-block-preformatted')
delete.decompose()
print(title.text)
print(article.text)