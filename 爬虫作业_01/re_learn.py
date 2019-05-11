import re
# 参考：learn from https://desmonday.github.io/2019/03/02/python%E7%88%AC%E8%99%AB%E5%AD%A6%E4%B9%A0-day2%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/
# 参考：https://blog.csdn.net/m0_37360684/article/details/84139047

#（一）re.match (pattern,string,flags) span() 返回一个元组包含匹配 (开始,结束) 的位置
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

#group
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# r 表示为非转义原始字符 让编译器忽略转义字符  (.*) 第一个匹配分组，.*代表匹配除换行符之外的所有字符；(.*?)第二个匹配分组，.*?后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符；后面的一个.* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

#（二）re.search

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

line="Cats are smarter than dogs";
searchObj= re.search(r'(.*) are (.*?) .*',line ,re.M|re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

# （三）re.sub(pattern, repl, string, count=0, flags=0) 替换

phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num= re.sub(r'#.*$',"",phone)
print(num)
#删除-
num2=re.sub(r'\D',"",num)
print(num2)

#匹配的数字 乘2
def double(matched):
    value = int(matched.group('value'))
    return  str(value*2)
s='A23G4348D5'
print(re.sub('(?P<value>\d+)',double,s))
#？P<value> 代表的是为 group 分组添加一个分组名


#（四）re.compile(pattern[, flags]) compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。

pattern= re.compile(r'\d+')
m=pattern.match('12345dfsjdf',2,8)
print(m)


#（五）re.findall 在字符串中匹配所有字串 返回一个list  findall(string, pos, endpos)

pattern = re.compile(r'\d+')  # 查找数字
result= pattern.match('runoob 123 google 456')
result0= pattern.search('runoob 123 google 456')
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result)
print(result0)
print(result1)
print(result2)



#（六）身份证匹配
s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())



