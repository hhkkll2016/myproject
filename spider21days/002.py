#encoding: utf-8

import requests
from lxml import etree

#爬取电影天堂数据
BASE_DOMIN = "http://dytt8.net"
URL = 'http://dytt8.net/html/gndy/dyzz/list_23_1.html'
HEADERS = {
    "Referer":"http://dytt8.net/js1/zxj.htm",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
}

def get_detail_urls(url):
    resp = requests.get(url,headers=HEADERS)
    #text = resp.content.decode("gbk")
    #此处采用gbk的方式对有的网页有问题，因为只需要获取url，所以可以不解码或者采用默认方式.text解码
    text = resp.content
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = list(map(lambda url:BASE_DOMIN+url,detail_urls))
    return detail_urls

#1拿到总页数
def get_page_max():
    html = requests.get(URL,headers=HEADERS)
    html = etree.HTML(html.content.decode('gbk'))
    num = int(html.xpath("//select[@name='sldd']/option[last()]/text()")[0])
    return num

def parse_detail_url(url):
    moive ={}
    resp = requests.get(url,headers = HEADERS)
    text = resp.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath('//h1/font/text()')[0]
    moive['title'] = title
    zoomE = html.xpath("//div[@id='Zoom']")[0]
    pic = zoomE.xpath('.//img/@src')
    if pic:
        poster = pic[0]
        screenshot =pic[1]
        moive['poster'] = poster
        moive['screenshot'] = screenshot
    else:
        moive['poster'] = ''
        moive['screenshot'] = ''

    infos = zoomE.xpath('.//text()')
    #清理数据
    def parse_infos(info,rule):
        # strip()去掉两边的空格
        return info.replace(rule,'').strip()
    for index,info in enumerate(infos):
        if info.startswith('◎年　　代'):
            info = parse_infos(info,'◎年　　代')
            moive['year'] = info
        elif info.startswith('◎产　　地'):
            info = parse_infos(info, '◎产　　地')
            moive['country'] = info
        elif info.startswith('◎类　　别'):
            info = parse_infos(info, '◎类　　别')
            moive['type'] = info
        elif info.startswith('◎语　　言'):
            info = parse_infos(info, '◎语　　言')
            moive['language'] = info
        elif info.startswith('◎上映日期'):
            info = parse_infos(info, '◎上映日期')
            moive['date'] = info
        elif info.startswith('◎豆瓣评分'):
            info = parse_infos(info, '◎豆瓣评分')
            moive['douban rating'] = info
        elif info.startswith('◎导　　演'):
            info = parse_infos(info, '◎导　　演')
            moive['director'] = info
        elif info.startswith('◎主　　演'):
            info = parse_infos(info, '◎主　　演')
            actors = [info]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            moive['actors'] = actors
        elif info.startswith('◎简　　介'):
            info = parse_infos(info, '◎简　　介')
            moive['introduction'] = infos[index+1].strip()
    download = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")
    if download:
        download_url = download[0]
        moive['download_url'] = download_url
    else:
        moive['download_url'] = ''
    return moive



def spider():
    url_1 = 'http://dytt8.net/html/gndy/dyzz/list_23_{}.html'
    num = get_page_max()
    moives = []
    for i in range(1,num-180):
        url = url_1.format(i)
        detail_urls = get_detail_urls(url)
        print("*"*30)
        print(i)
        for detail_url in detail_urls:
            moive = parse_detail_url(detail_url)
            moives.append(moive)
    print(moives)


spider()

