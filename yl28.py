import urllib3
from bs4 import BeautifulSoup
url = "https://www.delfi.ee/"
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")
print(soup.find('title').text)

htmlEle = soup.find('h5', attrs={'class': 'C-headline-title'})

print(htmlEle.text)
