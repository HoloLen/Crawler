from contextlib import  closing
import requests,json,re,os,sys,random,time
from urllib.request import urlopen
import urllib
from lxml import etree

class getUrl(object):

    def run(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
        }
        url= 'http://www.dxy.cn/bbs/thread/626626'
        req= requests.get(url,headers=headers)
        html=req.text
        tree = etree.HTML(html)
        user=tree.xpath('//div[@class=“auth”]/a/text()')
        content=tree.xpath('//td[@class=“postbody”]')
        #print(content)
        result=[]
        for i in range(0,len(user)):
            print(user[i].strip()+":"+content[i].xpath('string(.)').strip())
            print('*' * 80)
if __name__ == '__main__':
    geturl = getUrl()
    geturl.run()