import urllib.request
import os
import time
import hashlib
import base64
from bs4 import BeautifulSoup
import re

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

def url_open(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'\
               ,'Referer':'http://jandan.net/'}
    req = urllib.request.Request(url=url, headers=headers)
    # proxies = ['1.195.250.108:61234','111.170.105.54:61234','60.177.226.252:18118','211.147.67.150:80']
    # proxy = random.choice(proxies)
    # print(proxy)
    # proxy_support = urllib.request.ProxyHandler({'http':proxy})
    # opener = urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(opener)
    response = urllib.request.urlopen(req)
    html = response.read()
    response.close()
    time.sleep(1)
    return html

def get_pages(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    c = html[a:b]
    model = re.findall(r'.*<script\ssrc=\"\/\/(cdn.jandan.net\/static\/min.*?)\"><\/script>.*', html)
    jsFileUrl = "http://" + model[len(model) - 1]
    jsFile = url_open(jsFileUrl).decode('utf-8')
    a = jsFile.find('(e,"')
    constant = jsFile[a + 4:a + 36]
    print(constant)
    return c, constant

def find_imgs(url, constant):
    html = url_open(url).decode('utf-8')
    page = BeautifulSoup(html, "lxml")
    img_addrs = []
    for item in page.select('.img-hash'):
        # print(item.text)
        imgUrl = 'http:' + parse(item.text, constant)
        img_addrs.append(imgUrl)
    return img_addrs

def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]

        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder='xxoo',pages=8):
    # os.mkdir(folder)
    os.chdir(folder)
    url = 'http://jandan.net/ooxx/'
    page_str, constant = get_pages(url)
    page_num = int(page_str)

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url, constant)
        save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()




