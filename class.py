import requests,bs4
res =requests.get("https://www.imdb.com/name/nm8257146/")
soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup.select(".year_column")[0].getText())
for item in soup.select(".year_column"):
    print(item.text)