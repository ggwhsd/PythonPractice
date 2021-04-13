# -*- coding: UTF-8 -*-
import numpy as np
print("*"*10," numpy ","*"*10)
data = [1,2,3,5]
arr = np.array(data)

data1 = [data,data]
arr1 = np.array(data1)

print(arr)
print(arr1)

zero = np.zeros((3,3))
print(zero)

l = np.arange(1,10,2)
print(l)


float_data = arr1.astype(np.float64)
print(float_data)

print(float_data[0,0])
print(float_data[0])


print(float_data*3)

print(float_data.mean())
print(float_data.std())

import numpy.random as npr
import matplotlib.pyplot as plt

print(npr.rand(3,2))
print(npr.rand(3,2)*2+2)


#横坐标
input_values = range(5)
#横坐标对应的纵坐标上的值
squares = [1,4,9,16,25]

plt.plot(input_values,squares,linewidth=1)
plt.title("squares",fontsize = 24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize = 14)
plt.tick_params(axis='both',labelsize=14)
plt.show()

plt1=plt
plt1.scatter(2,4)
plt1.scatter(3,5,s=200)
plt1.show()

plt1.scatter(input_values,squares,s=100)
plt1.show()

x_values=range(1,1001)
y_value=[x**2 for x in x_values]

plt1.scatter(x_values,y_value,edgecolor='none',s=10,c='red')

plt1.axis([0,1100,0,1100000])
plt1.show()



