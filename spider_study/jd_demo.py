# encoding = "utf-8"

import requests
import re,json,csv

def parse_page(page):
    url = "https://list.jd.com/list.html"
    baseurl_price = "http://p.3.cn/prices/mgets?skuIds=J_{}"
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
    }

    params = {
        "cat":"9987, 653, 655",
        "page":2,
        "sort":"sort_rank_asc",
        "trans": 1,
        "JL": "6_0_0",
         "ms":"4",
        "page":page
    }

    try:
        html = requests.get(url,headers=headers,params=params)
    except:
        pass

    text = html.text
    phones = re.findall('\{"\d*":\{"aos":\[.*?\}\}',text)

    i = 0

    for phone in phones:
        phone = json.loads(phone)
        skuId = list(phone.keys())[0]
        name = phone[skuId]["name"]
        price_url = baseurl_price.format(skuId)
        try:
            price_html = requests.get(price_url,headers=headers)
        except:
            pass
        price = price_html.json()[0]['op']
        with open("C:\\proj_stock\\jd\\jd.csv","a",encoding="gbk",newline="") as fp:
            myWriter = csv.writer(fp)
            myWriter.writerow([name, price])
        i = i+1
        print("第{0}页第{1}个商品正在写入....".format(page,i))

#京东价格API：http://p.3.cn/prices/mgets?skuIds=J_2510388，
#该api返回的是json数据，易于解释获取，其中skulds是每个商品地址栏内的数字ID，即可获取到json数据。
#在json数据中，p是目前价格，M是最高价，op是指导价。

def main():
    for page in range(1,149):
        parse_page(page)


if __name__ == "__main__":
    main()