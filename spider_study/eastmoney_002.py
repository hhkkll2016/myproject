
#encoding= "utf-8"

import requests
from bs4 import BeautifulSoup
import json
#获取东方财富网板块信息的链接

url = 'http://data.eastmoney.com/bkzj/BK0448.html'
url_base ='http://data.eastmoney.com'
headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
        "Referer" : "http://data.eastmoney.com/yjfp/"
    }
links_for_allbk = {}

html = requests.get(url,headers=headers)
soup = BeautifulSoup(html.content.decode("gbk"),"lxml")

links_for_hy = {}
div_hy = soup.find("div", id="pop-cont1")
a_hys = div_hy.find_all("a")
for a_hy in a_hys:
    links_for_hy[a_hy.get_text()] = url_base + a_hy['href']
links_for_allbk.update(links_for_hy)

links_for_gl = {}
div_gl = soup.find("div", id="pop-cont2")
a_gls = div_gl.find_all("a")
for a_gl in a_gls:
    links_for_gl[a_gl.get_text()] = url_base + a_gl['href']
links_for_allbk.update(links_for_gl)

links_for_dq = {}
div_dq = soup.find("div", id="pop-cont3")
a_qds = div_dq.find_all("a")
for a_dq in a_qds:
    links_for_dq[a_dq.get_text()] = url_base + a_dq['href']
links_for_allbk.update(links_for_dq)


with open("C:\\proj_stock\\eastmoney\\links_for_allbk.json","w",encoding="utf-8") as fp:
    json.dump(links_for_allbk,fp,ensure_ascii=False)