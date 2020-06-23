import requests
import bs4
result=requests.get("https://www.imdb.com/name/nm8257146/")
soup=bs4.BeautifulSoup(result.text,'lxml')
print(type(result))
print(result.text)
print(soup.select('p')[0].getText())