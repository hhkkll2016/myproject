#!/user/bin/env python3
# - * - coding: UTF-8 - * -

import io
import sys
import urllib
from urllib import request
from urllib import parse

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

"""
def getHtml(url, keys):
    url_values = urllib.parse.urlencode(keys)
    full_url = url + url_values
    page = request.urlopen(url)
    html = page.read()
    #html = html.decode('UTF-8')
    return html

data = {}
data['word'] = '22'

html = getHtml("http://www.baidu.com",data)
"""

data={}
data['word']='Jecvay Notes'

 
url_values=parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data1=request.urlopen(full_url).read()
data1=data1.decode('UTF-8')
data1=data1.encode('gb18030')

#print(data1)

file_object = open('c:/PythonProject/text.txt','wb+')
file_object.write(data1)
file_object.close()

