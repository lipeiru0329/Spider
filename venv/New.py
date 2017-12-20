import BeautifulSoup
import urllib2
#import wx
import sys
import urllib
import urllib2
import re
import json
import hashlib
import os
import time


class Datacollect():
    def __init__(self, keyword, startTime, interval='50', flag=True, begin_url_per = "https://www.gebiz.gov.sg/"):
        self.begin_url_per = begin_url_per  # url
        self.setKeyword(keyword)  # Keyword
        self.setStartTimescope(startTime)  # starttime
        # self.setRegion(region)  # region
        self.setInterval(interval)  # interval time
        self.setFlag(flag)
        self.logger = logging.getLogger('main.CollectData')  # log

    def setKeyword(self, keyword):
        self.keyword = keyword.decode('GBK', 'ignore').encode("utf-8")
        print 'twice encode:', self.getKeyWord()

    def getKeyWord(self):
        once = urllib.urlencode({"kw": self.keyword})[3:]
        return urllib.urlencode({"kw": once})[3:]

    def setStartTimescope(self, startTime):
        if not (startTime == '-'):
            self.timescope = startTime + ":" + startTime
        else:
            self.timescope = '-'

    def setRegion(self, region):
        self.region = region

    def setInterval(self, interval):
        self.interval = int(interval)

    def setFlag(self, flag):
        self.flag = flag

    def getURL(self):
        return self.begin_url_per + self.getKeyWord() + self.timescope + "&page="


def main():
    print 1
    response = urllib2.urlopen("http://www.baidu.com")
    print response.read()


if __name__ == '__main__':
    main()