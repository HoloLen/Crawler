import urllib.request
import requests
import urllib3
#get urlopen
f = urllib.request.urlopen('http://www.baidu.com')
firstline = f.readline() #读取html 页面第一行
#print(firstline)

#post Request urlopen
req = urllib.request.Request(url='http://www.baidu.com',data=b'The first day of Crawler')
req_data = urllib.request.urlopen(req)
req = req_data.read()
#print(req)
