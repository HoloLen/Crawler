import json
import requests
data={
    'name':'wangdi',
    'shares':100,
    'price':54.3
}
#python 数据结构转化为json 格式 json.dumps()方法
json_str=json.dumps(data)
#json编码的字符串 转回 python 数据结构
data=json.loads(json_str)

