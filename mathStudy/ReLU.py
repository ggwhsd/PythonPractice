# -*- coding: UTF-8 -*-
from cProfile import label
import math 
import numpy as np
import matplotlib.pyplot as plot


xArr = np.linspace(-10,10,100)
print(xArr)
c=1
b=1
w=1
y= []
for i in range(xArr.size):
    y.append(c* max(0,b+w*xArr[i]))
plot.plot(xArr,y,label="1")

y= []
for i in range(xArr.size):
    y.append(1* max(0,20+w*xArr[i]))

#plot.plot(xArr,y,label="2")


y= []
for i in range(xArr.size):
    y.append(1* max(0,1+2*xArr[i]))

#plot.plot(xArr,y,label="3")

y= []
for i in range(xArr.size):
    y.append(-1* max(10,1+2*xArr[i]))
plot.plot(xArr,y,label="4")

y= []
for i in range(xArr.size):
    y.append(c* max(0,b+w*xArr[i]) + -1* max(10,1+2*xArr[i]))


plot.plot(xArr,y,label="5")
plot.legend()
plot.show()