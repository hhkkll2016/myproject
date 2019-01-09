#encoding: utf-8

import requests
from lxml import etree

#豆瓣电影正在上映的电影

url = 'https://movie.douban.com/cinema/nowplaying/changsha/'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Referer":"https://movie.douban.com/"
}
resp = requests.get(url,headers=headers)
text = resp.text
html = etree.HTML(text)
#print(etree.tostring(html,encoding="utf-8").decode("utf-8"))
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
moives = []
for li in lis:
    title = li.xpath('@data-title')[0]
    score = li.xpath('@data-score')[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath('@data-region')[0]
    director = li.xpath('@data-director')[0]
    actors = li.xpath('@data-actors')[0]
    poster = li.xpath('.//img/@src')[0]
    moive ={
        'title':title,
        'score':score,
        'duration':duration,
        'region':region,
        'director':director,
        'actors':actors,
        'poster':poster
    }
    moives.append(moive)
print(moives)

