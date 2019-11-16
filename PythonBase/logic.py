# -*- coding: UTF-8 -*-
import sys
a=7
if a>0:
    print "hello"
a=0
while a<7:
	print a
	a+=1
a=100

a=7+8
print a
b="GOD"+"JOB"
print b*2
a=7/3
print a
a=7.0/3
print a


for i in range(5):
	if i%2==0:
		print str(i)+" odd"
	else:
		print str(i)+" even"

char=u"一二三四"  #U代表unicode
tem=("yuan 1","yuan 2","yuan 3","yuan 4")
list_=["list1","list2","list3","list4"]
dict_={"first":"dict1","second":"dict2","third":"dict3"}

for i in char:
	print i
for i in tem:
	print i
for i in list_:
	print i
for i in dict_:
	print i+":"+dict_[i]


def function1():
	a=9
	a+=8
	print a

function1()

def function2(a,b):
	if a>b:
		print a
	else:
		print b

function2(3,9)

def testTimeConsume():
	for i in xrange(10000000):
		i+=1

def multiReturnValue():
	return 1,2,3

a,b,c = multiReturnValue()
print (a,b,c)

def helpDoc():
	'''这个函数展示文档作用
	'''
	return k

help(helpDoc)

import sys
print sys.argv[0]
print sys.platform

print("hello")

from pandas import DataFrame
df1 = DataFrame({'Key':['b','b','a','c','a','a','b'],'data':range(7)})
df1.head(2)


if __name__ == "__main__":
	print "it is a main"
else:
	print "it is not a min"

import module1 as mo
print mo.addModule(1,3)



