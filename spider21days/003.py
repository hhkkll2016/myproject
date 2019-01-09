#encoding = utf-8
from bs4 import BeautifulSoup
import requests

#爬取中国天气网数据

def parse_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
    }
    resp = requests.get(url,headers = headers)
    html = resp.content.decode('utf-8')
    soup = BeautifulSoup(html,'html5lib')
    #soup = BeautifulSoup(html, 'lxml')
    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    infos =[]
    for table in tables:
        trs = table.find_all('tr')[2:]
        for tr in trs:
            tds = tr.find_all('td')
            info = {}
            info['city'] = tds[-8].text.strip()
            info['temp'] = int(tds[-2].text.strip())
            infos.append(info)
    return infos



def get_urls():
    url_base = 'http://www.weather.com.cn/textFC/{}.shtml'
    #regions = ['hb','db','hd','hz','hn','xb','xn','gat']
    regions = ['hb','db','hd','hz','hn','xb','xn','gat']
    urls = list(map(lambda x:url_base.format(x),regions))
    return urls

def main():
    urls = get_urls()
    print(urls)
    all_infos = []
    for url in urls:
        infos = parse_url(url)
        all_infos.extend(infos)
        #break
    print(all_infos)


if __name__ == "__main__":
    main()

