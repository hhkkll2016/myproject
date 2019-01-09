# encoding utf-8

import requests
from lxml import etree

def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    }
    resp = requests.get(url,headers=headers)
    text = resp.text
    print(text)

def main():
    for x in range(1,2):
        url = "http://www.doutula.com/photo/list/?page={}".format(str(x))
        parse_page(url)


if __name__ == '__main__':
    main()

