#encoding=utf8
#---------------------------------------
#教程资源下载爬虫
#肖叮
#------------------------------------------------------------------------
#30元套餐链接
#http://ruiyujiaoyu.com/forum.php?mod=viewthread&tid=4&extra=page%3D1
#密码：333123458
#（输入密码不显示资源，刷新下就好了）
#好*评送价值3888元大礼
#欢迎加入我们的q讨论q un: 169511293(申请时候备注上淘宝账号)
#论坛上注册帐号后发给我，我给亲开通会员，更新都在论坛上，基本每天更新
#------------------------------------------------------------------------
#首先在360登录，接着输入密码，再将网页另存到本地重命名为1.html，然后运行此程序即可,现在有241条
#2016-11-11
#---------------------------------------
import urllib
import urllib2
import cookielib
import string
import re
import requests
import sys
import logging

from bs4 import BeautifulSoup
from urllib2 import urlopen
class ResourceSpider:

    def __init__(self):
        pass

    def downloadResource(self, starturls):
        indexhtml = open(starturls[0])
        soup = BeautifulSoup(indexhtml.read(), "html.parser", from_encoding="utf-8")
        soup.prettify()
        table = soup.find("table",{"class":"hovertable"})
        count =0
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            if len(cells)==3:
                count+=1
                name=cells[0].find(text=True)
                href=cells[1].a.get("href")
                code = cells[2].find(text=True)
                print "No: "+str(count)+" "+name+" : "+href+" --------- [提取码：".decode("utf-8") +code+"]"




    def getResource(self):
        pass


    def sotreResource(self):
        pass

if __name__ == '__main__':
    startUrls = ["1.html"]
    spider = ResourceSpider()
    spider.downloadResource(startUrls)
    spider.getResource()
    spider.sotreResource()
