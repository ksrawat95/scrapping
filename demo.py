from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.w3schools.com/html/")
bsobj=BeautifulSoup(html.read(), 'lxml')
print(bsobj)
# nameList=bsobj.find_all("span" ,{"class" : "left_h2"});
# for name in nameList:
#     print(name.get_text())
#     print(name)
