# -*- coding: UTF-8 -*-
import re


#re.match和re.group的用法,
#match是从第一个开始匹配，才算是匹配，如果是中间开始，则不算匹配
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if(matchObj): 
    print(matchObj.group())
    print(matchObj.group(1))
    print(matchObj.group(2))

matchObj = re.match(r'n(.*) to (.*) you','nice to me you, nice to meet you',re.IGNORECASE)
if(matchObj):
    print(matchObj.group(1))
    print(matchObj.group(2))


#re.sub的用法,用于替换，然后返回值
phone = "2004-959-'5'59 # 这是'一个'外电话号码"
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)
num = re.sub(r'\D',"",num)
print("电话号码是: ", num)

context="""
<div class="j-fontContent 
newscontnet minh300"><span 
'style'="font-family: 

方正小标宋简体; color: rgb(0, 0, 0); font-size: 22pt;"



   >


"""
print(context)
cont = re.sub('\"',"\\\"",context)
cont = re.sub('\'',"\\\'",cont)
cont = re.sub('\s+'," ",cont)
print("转义之后,cont",cont)

#re.sub的高级用法，替换字符串，可以用替换函数
#group分组除了用数字索引，也能直接用名字
def replFunc(matchObj):
    value = int(matchObj.group('value'))
    return str(value*2)

oldString = 'asdf123dd588'
#可以看到(?P<pattern>)可以用来标记一些模糊的模式，
# 然后在同一个正则表达式中，我们可以通过(?P=pattern)来复用之前的内容
newString = re.sub('(?P<value>\d+)',replFunc,oldString)
print(newString)

