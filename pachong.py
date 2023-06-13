import requests

from bs4 import BeautifulSoup

url = "https://www.bibooo.cn/"

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")
links = []

for li in soup.find_all('li',{'class':'py-6'}):
    for a in li.find_all('a'):
        links.append(a['href'])


linksarr = []

for i in links:
    linksarr.append( url +i)



with open('links.txt','w') as f:
    for link in linksarr:
        f.write(link)
        f.write('\n')
