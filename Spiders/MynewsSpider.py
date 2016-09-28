#encoding=utf8
#---------------------------------------
#网易新闻爬虫
#肖叮
#2016-09-25
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
class MynewsSpider:

    def __init__(self):
        pass
    def setNewsUrls(self, starturls):
        indexhtml = urlopen(starturls[0])
        soup = BeautifulSoup(indexhtml.read(), "html.parser", from_encoding="gbk")
        soup.prettify()
        for page in soup.find_all(href=re.compile("http://news.163.com/special/00011229/shehuinews")):
            print page.get('href')
            startUrls.append(page.get('href'))
            print startUrls,
        for idx,url in enumerate(startUrls):
            print "page: "+str(idx)
            html = urlopen(url)
            soup = BeautifulSoup(html.read(),"html.parser",from_encoding="gbk")
            soup.prettify()
            for links in soup.find_all("div", class_="list-item clearfix"):
                print links.h2
                pageurl = links.h2.a.get('href')
                pagehtml = urlopen(pageurl)
                pagesoup = BeautifulSoup(pagehtml.read(),"html.parser",from_encoding="gbk")
                print pagesoup.find('span',class_='ep-editor').text

            print "end"




    def getNews(self):
        pass


    def sotreNews(self):
        pass

if __name__ == '__main__':
    startUrls = ["http://news.163.com/shehui/"]
    spider = MynewsSpider()
    spider.setNewsUrls(startUrls)
    spider.getNews()
    spider.sotreNews()
