# -*- coding: UTF-8 -*-
import pandas as pd 

obj = pd.Series([40,12,-3,25])
print obj
print obj.index
print obj.values
print obj>15
print obj[obj>15]
print obj.mean()

dict = obj.to_dict()
print dict.values()

dic={'one':pd.Series([1.,2.,3.,4.],index=['a','b','c','d']),'two':pd.Series([3.,4.,5.,6.],index=['a','b','c','d'])}
df = pd.DataFrame(dic)
print df
df.to_excel('dataframe.xls');

a = pd.read_excel('dataframe.xls')
print a

data=pd.read_csv('closeprice.csv',dtype={'seq':str},encoding='gbk')
print data.describe().T
#print data.info()

'''
通过映射字典方式，新增一列数据
'''
b={'0':"yinhang",'1':"baoxian",'2':"jinglirun"}
data['describe']=data.seq.map(b)
print data
#排序，inplace表示是否覆盖原数据
print data.sort_values(by=['describe'],ascending=[False],inplace=False)

print data.replace(1,'nan')
print data.rename(columns={'seq':'id'})


