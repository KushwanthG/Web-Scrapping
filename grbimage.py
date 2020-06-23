import bs4,requests
res =requests.get("https://www.imdb.com/name/nm8257146/")
soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup.select(".image")[0].img['src'])
res1=requests.get("https://m.media-amazon.com/images/M/MV5BYmQ1NWFkYmQtMjgwMS00NTNmLTkwNWEtNWY3ZmJkY2NlZTdlXkEyXkFqcGdeQXVyNDc2NzU1MTA@._V1_UX214_CR0,0,214,317_AL__QL50.jpg")
print(res1)
f=open("c:\Users\Kushwanth Gondi\Desktop\New folder","wb")
f.write(res1.content)
f.close()