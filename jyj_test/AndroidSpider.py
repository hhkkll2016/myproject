

#url_manager.py
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.used_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.used_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) > 0

    def get_new_url(self):
        temp_url = self.new_urls.pop()
        self.used_urls.add(temp_url)
        return temp_url

#html_downloader.py
from http import cookiejar
from urllib import request, error
from urllib.parse import urlparse

class HtmlDownLoader(object):
    def download(self, url, retry_count=3, headers=None, proxy=None, data=None):
        if url is None:
            return None
        try:
            req = request.Request(url, headers=headers, data=data)
            cookie = cookiejar.CookieJar()
            cookie_process = request.HTTPCookieProcessor(cookie)
            opener = request.build_opener()
            if proxy:
                proxies = {urlparse(url).scheme: proxy}
                opener.add_handler(request.ProxyHandler(proxies))
            content = opener.open(req).read()
        except error.URLError as e:
            print('HtmlDownLoader download error:', e.reason)
            content = None
            if retry_count > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    #说明是 HTTPError 错误且 HTTP CODE 为 5XX 范围说明是服务器错误，可以尝试再次下载
                    return self.download(url, retry_count-1, headers, proxy, data)
        return content

#html_parser.py
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parse(self, url, content, html_encode="utf-8"):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, "html.parser", from_encoding=html_encode)
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data


    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r"/item/\w+"))
        for link in links:
            url_path = link["href"]
            new_url = urljoin(url, url_path)
            new_urls.add(new_url)
        return new_urls


    def _get_new_data(self, url, soup):
        data = {"url": url}
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        data["title"] = title_node.get_text()
        summary_node = soup.find("div", class_="lemma-summary")
        data["summary"] = summary_node.get_text()
        return data

#html_output.py
import time

class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        file_name = time.strftime("%Y-%m-%d_%H-%M-%S")
        with open("/Users/chenjuan/PycharmProjects/demo/out_%s.html" % file_name, "w", encoding='utf-8') as f_out:
            f_out.write("<html>")
            f_out.write(r'<head>'
                        r'<link rel="stylesheet" '
                        r'href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" '
                        r'integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" '
                        r'crossorigin="anonymous"></head>')
            f_out.write("<body>")
            f_out.write(r'<table class="table table-bordered table-hover">')

            item_css = ['active', 'success', 'warning', 'info']
            for data in self.datas:
                index = self.datas.index(data) % len(item_css)
                f_out.write(r'<tr class="'+item_css[index]+r'">')
                f_out.write('<td>%s</td>' % data["url"])
                f_out.write('<td>%s</td>' % data["title"])
                f_out.write('<td>%s</td>' % data["summary"])
                f_out.write("</tr>")

            f_out.write("</table>")
            f_out.write("</body>")
            f_out.write("</html>")

#spider_main.py
#from AndroidSpider import url_manager, html_downloader, html_parser, html_output

'''
爬取百度百科 Android 关键词相关词及简介并输出为一个HTML tab网页
Extra module:
BeautifulSoup
'''
class SpiderMain(object):
    def __init__(self):
        # self.urls = url_manager.UrlManager()
        # self.downloader = html_downloader.HtmlDownLoader()
        # self.parser = html_parser.HtmlParser()
        # self.out_put = html_output.HtmlOutput()
        self.urls = UrlManager()
        self.downloader = HtmlDownLoader()
        self.parser = HtmlParser()
        self.out_put = HtmlOutput()
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
                }
                html_content = self.downloader.download(new_url, retry_count=2, headers=headers)
                new_urls, new_data = self.parser.parse(new_url, html_content, "utf-8")
                self.urls.add_new_urls(new_urls)
                self.out_put.collect_data(new_data)
                if count >= 30:
                    break
                count = count + 1
            except Exception as e:
                print("craw failed!\n"+str(e))
        self.out_put.output_html()

if __name__ == "__main__":
    rootUrl = "http://baike.baidu.com/item/Android"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)