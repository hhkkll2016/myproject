"""
import urllib.request

response = urllib.request.urlopen("http://www.fishc.com")
html = response.read().decode("utf-8")
print(html)

import urllib.request

#实例化一个request对象
req = urllib.request.Request("http://placekitten.com/g/500/600")
response= urllib.request.urlopen(req)
cat_img = response.read()
with open("cat_500_600.jpg","wb") as f:
     f.write(cat_img)

print(response.geturl())
print(response.info())
print(response.getcode())
"""
import urllib.request
import hashlib
import base64
from bs4 import BeautifulSoup
import requests
import re
import random
import shutil
import os
import time
import queue
import threading

def parse(imgHash,constant):
    q = 4
    hashlib.md5()
    constant = md5(constant)
    o = md5(constant[0:16])
    n = md5(constant[16:32])
    l = imgHash[0:q]
    c = o + md5(o + l)
    imgHash = imgHash[q:]
    k = decode_base64(imgHash)
    h = list(range(256))

    b = list(range(256))

    for g in range(0, 256):
        b[g] = ord(c[g % len(c)])

    f = 0
    for g in range(0, 256):
        f = (f + h[g] + b[g]) % 256
        tmp = h[g]
        h[g] = h[f]
        h[f] = tmp

    result = ""
    p = 0
    f = 0
    for g in range(0, len(k)):
        p = (p + 1) % 256
        f = (f + h[p]) % 256
        tmp = h[p]
        h[p] = h[f]
        h[f] = tmp
        result += chr(k[g] ^ (h[(h[p] + h[f]) % 256]))
    result = result[26:]

    return result


def md5(src):
    m = hashlib.md5()
    m.update(src.encode("utf8"))
    return m.hexdigest()


def decode_base64(data):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return base64.b64decode(data)

url = "http://jandan.net/ooxx/page-88#comments"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36' \
    , 'Referer': 'http://jandan.net/'}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
#print(html)
model = re.findall(r'.*<script\ssrc=\"\/\/(cdn.jandan.net\/static\/min.*?)\"><\/script>.*', html)

jsFileUrl = "http://" + model[len(model) - 1]
#print(jsFileUrl)
req2 = urllib.request.Request(url=jsFileUrl,headers=headers)
jsFile = urllib.request.urlopen(req2).read().decode('utf-8')
#print(jsFile)
a = jsFile.find('(e,"')
constant = jsFile[a+4:a+36]
#print(constant)
page = BeautifulSoup(html, "lxml")
for item in page.select('.img-hash'):
    #print(item.text)
    imgUrl = 'http:' + parse(item.text, constant)
    print(imgUrl)
#https://blog.csdn.net/van_brilliant/article/details/78723878
#https://github.com/van1997/JiandanSpider/blob/master/spider.py

#m = 'f4dbd6rKcTZRS76P0m4+7lRHXwlzLRldEWXKRZUVJ4OlsMU0surJiUJbuQrZEy6bFDUoxVMjNta2m5qfTD72DSYgWdEt0WB9fpB2YFDOZC5d0EhiEMmP7A'
#m = 'ece8ozWUT/VGGxW1hlbITPgE0XMZ9Y/yWpCi5Rz5F/h2uSWgxwV6IQl6DAeuFiT9mH2ep3CETLlpwyD+kU0YHpsHPLnY6LMHyIQo6sTu9/UdY5k+Vjt3EQ'
# r = 'qySLoo7dXz8MbtdZwHNtypQueQjFOtne'
# print('http:' + parse(m, r))