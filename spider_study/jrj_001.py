import urllib.request
from bs4 import BeautifulSoup

url = 'http://stock.jrj.com.cn/share,600715,zcfzb.shtml'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
#html = response.read().decode('utf-8',errors='ignore')

soup = BeautifulSoup(html, 'lxml')

print(soup.title, soup.head, soup.a, soup.p)