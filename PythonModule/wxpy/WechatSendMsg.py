# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 08:23:08 2018

@author: Gao
"""

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
#windows登录调用 bot = Bot()
#linux登录调用 bot = Bot(console_qr=2,cache_path="botoo.pkl")
bot = Bot(console_qr=2,cache_path="botoo.pkl")

def get_news():
    url='http://open.iciba.com/dsapi/'
    r=requests.get(url)
    content=r.json()['content']
    note=r.json()['note']
    return content,note

def send_news():
    try:
        contents=get_news()
        my_friend=bot.friends().search(u'Future')[0]
        my_friend.send(contents[0])
        my_friend.send(contents[1])
        my_friend.send(u'Have a good one!')
        
        t=Timer(86400,send_news)
        t.start()
    except:
        my_friend=bot.friends().search('Future')[0]
        my_friend.send(u'今天消息发送失败了')
    
if __name__=='__main__':
    send_news()

     