import requests
import json
#help(requests.get)

#（一）get请求
url='http://www.baidu.com'
response = requests.get(url)
print(response.text) #打印源代码


#（二）post 请求 请求时候构造一个参数
# 1.用字典构造
data={
    "name":"haha",
    "school":"sysu"
}
response2 = requests.post("http://www.baidu.com",data=data)
print(response2.text)

#  2.json格式构造
data2={
    'name':'desmon',
    'school':'sysu'
}

'''
data2 转化为json 编码
json_str=json.dumps(data2)
json 编码的字符串转化成python 数据结构
data2=json.loads(json_str)
'''

response2 = requests.post("http://www.baidu.com",data=data2)
print(response2.text)

#（三）添加请求头
headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}
r=requests.post("http://baike.baidu.com/item/摩尔斯电码",headers=headers,allow_redirects=False)
r.encoding='UTF-8'
print(r.url)
print(r.headers) #响应头
print(r.request.headers) #请求头

# 公众号上的资料
r = requests.get("https://www.baidu.com") #GET请求
r = requests.post("https://www.baidu.com/post") #POST请求
r = requests.put("https://www.baidu.com/put") #PUT请求
r = requests.delete("https://www.baidu.com/delete") #DELETE请求
r = requests.head("https://www.baidu.com/get") #HEAD请求
r = requests.options("https://www.baidu.com/get") #OPTIONS请求

print(r.status_code)  # 打印状态码
print(r.url)          # 打印请求url
print(r.headers)      # 打印头信息
print(r.cookies)      # 打印cookie信息
print(r.text)         #以文本形式打印网页源码
print(r.content)      #以字节流形式打印


