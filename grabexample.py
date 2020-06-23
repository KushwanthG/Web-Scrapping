import requests,bs4
res=requests.get("https://www.google.co.in/")
soup=bs4.BeautifulSoup(res.text,'lxml')
print(soup.select(".gbh")[0]['style'][0])
