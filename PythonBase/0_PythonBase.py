
# -*- coding: UTF-8 -*-
print ("你好")

def printFenGeFu(msg:str):
    print("*"*10,msg,"*"*10)

printFenGeFu("if/else")
if True:
	print ("True")
	print ("对")
else:
	print ("False")
	print ("错")

printFenGeFu(" \' and \" ")
singleQuote='i say:"i will be back”'
print(singleQuote)
doubleQuotes="hero's world"
print(doubleQuotes)

printFenGeFu(" list ")
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
print(list) # 输出完整列表
print(list[0]) # 输出列表的第一个元素
print(list[1:3]) # 输出第二个至第三个的元素
print(list[2:]) # 输出从第三个开始至列表末尾的所有元素
print(list[1:4:3])  #3是步长

str ="hello"
print(str)
print(str[0:1])
print(str[1:])

printFenGeFu(" list and tuple ")
#元组是另一个数据类型，类似于List（列表）。元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]

list[2] = 1000 # 列表中是合法应用
print(list)
print(tuple)

printFenGeFu(" dict ")
#列表是有序的对象结合，字典是无序的对象集合。
dict = {} 
dict['one'] ="This is one"
dict[2] = "This is two"
print(dict)

print(dict.keys())
print(dict.values())
if dict.get('one',None) is None:
	print("dict has not key")
else:
    print("dict has key")

printFenGeFu(" int() ")
i = "10"
print(int(i))
print(hex(int(i)))
print(oct(int(i)))

printFenGeFu(" if/elif/else ")
num = 5
if num == 3:# 判断num的值 
	print('boss');
elif num == 5:
	print('staff');
else:
	print('nothing');


printFenGeFu(" while ")
count =1
while count < 5 :
	print(count,"is less than 5")
	count = count +1
else:
	print(count,"is not less than 5")

printFenGeFu(" for ")
for letter in 'Python':
	print('当前字母:',letter)



