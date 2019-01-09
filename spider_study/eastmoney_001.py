# encoding = utf-8

import requests
import json,csv
import re
import string

#根据股票代码获取财报三表信息

def parse_pases(url,foldername):
    if foldername == "xjll.csv":
        with open("C:\\proj_stock\\eastmoney\\headers_xjll.json",'r') as fp:
            headers_table = json.load(fp)
    elif foldername == "zcfz.csv":
        with open("C:\\proj_stock\\eastmoney\\headers_zcfz.json",'r') as fp:
            headers_table = json.load(fp)
    elif foldername == "lr.csv":
        with open("C:\\proj_stock\\eastmoney\\headers_lr.json",'r') as fp:
            headers_table = json.load(fp)

    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
        "Referer" : "http://data.eastmoney.com/yjfp/"
    }

    resp = requests.get(url,headers=headers)
    datas = json.loads(resp.json())
    for data in datas:
        with open("C:\\proj_stock\\eastmoney\\" + foldername, "a", encoding='gbk', newline='') as fp:
            writer = csv.DictWriter(fp, headers_table)
            writer.writerow(data)

"""
    text_html = resp.text
    text_html = text_html.strip(string.punctuation)

    text_html = re.sub('[\]\[\\\\]', '', text_html)
    # text = re.sub("\[",'(',text)
    # text = re.sub("\]", ')', text)
    # text = re.sub("\\\\", "", text)
    texts = text_html.split("},{")
    for index,text in enumerate(texts):
        if index == 0:
            text = '{"' + text + "}"
        elif index==len(texts)-1:
            text = '{' + text + '"}'
        else:
            text = "{" + text + "}"
        text = json.loads(text)
        with open("C:\\proj_stock\\eastmoney\\" +foldername,"a",encoding='gbk',newline='') as fp:
            writer = csv.DictWriter(fp,headers_table)
            writer.writerow(text)
"""

def set_headers():
    with open("C:\\proj_stock\\eastmoney\\headers_lr.json", 'r') as fp:
        headers_lr = json.load(fp)
    with open("C:\\proj_stock\\eastmoney\\headers_zcfz.json", 'r') as fp:
        headers_zcfz = json.load(fp)
    with open("C:\\proj_stock\\eastmoney\\headers_xjll.json",'r') as fp:
        headers_xjll = json.load(fp)
    with open("C:\\proj_stock\\eastmoney\\refer.json",'r',encoding="utf-8") as fp:
        headers_refer = json.load(fp)

    for index,header in enumerate(headers_lr):
        if header in headers_refer.keys():
            headers_lr[index] = headers_refer.get(header)
    for index,header in enumerate(headers_zcfz):
        if header in headers_refer.keys():
            headers_zcfz[index] = headers_refer.get(header)
    for index,header in enumerate(headers_xjll):
        if header in headers_refer.keys():
            headers_xjll[index] = headers_refer.get(header)

    with open("C:\\proj_stock\\eastmoney\\lr.csv", "w", encoding='gbk', newline='') as fp:
        writer = csv.DictWriter(fp, headers_lr)
        writer.writeheader()
    with open("C:\\proj_stock\\eastmoney\\zcfz.csv", "w", encoding='gbk', newline='') as fp:
        writer = csv.DictWriter(fp, headers_zcfz)
        writer.writeheader()
    with open("C:\\proj_stock\\eastmoney\\xjll.csv", "w", encoding='gbk', newline='') as fp:
        writer = csv.DictWriter(fp, headers_xjll)
        writer.writeheader()


# def main():
    url_zcfz_base = 'http://emweb.securities.eastmoney.com/NewFinanceAnalysis/zcfzbAjax?companyType=4&reportDateType=1&reportType=1&endDate=&code='
    url_lr_base = 'http://emweb.securities.eastmoney.com/NewFinanceAnalysis/lrbAjax?companyType=4&reportDateType=1&reportType=1&endDate=&code='
    url_xjll_base = 'http://emweb.securities.eastmoney.com/NewFinanceAnalysis/xjllbAjax?companyType=4&reportDateType=1&reportType=1&endDate=&code='
    foldernames = ['zcfz.csv','lr.csv','xjll.csv']
    set_headers()
    with open("C:\\proj_stock\\eastmoney\\1spec.txt","r",encoding='utf-8') as fp:
        lines = fp.readlines()
        lines = [line.strip() for line in lines]
        for index,x in enumerate(lines):
            url_zcfz = url_zcfz_base + lines[index]
            url_lr = url_lr_base + lines[index]
            url_xjll = url_xjll_base + lines[index]

            parse_pases(url_zcfz, foldernames[0])
            parse_pases(url_lr, foldernames[1])
            parse_pases(url_xjll,foldernames[2])

            print('股票代码{0}正在写入.........'.format(x))
            print('第{0}个完成写入'.format(index))




if __name__ == '__main__':
    main()
