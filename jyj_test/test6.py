#!/usr/bin/pathon
# __*__ coding: UTF-8 __*__

import itchat
from itchat.content import *
import requests
import json

@itchat.msg_register(TEXT)
def reply_text(msg):
    #from_text = msg['Text']
    
    #if from_text[0] == '#':
        #to_text = baidu_trans(from_text[1:])
    itchat.send_msg('nice to meet you',msg['YOUJUN'])
    #else:
        #to_text   = tuling(from_text)
        #itchat.send(to_text,msg['FromUserName'])


def main():
    itchat.auto_login(hotReload=True)
    itchat.run()

if __name__ == '__main__':
    main()



