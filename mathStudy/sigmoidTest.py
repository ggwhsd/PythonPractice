# -*- coding: UTF-8 -*-
import math 
import numpy as np
import matplotlib.pyplot as plot

def sigmoid(x):
    return 1/(1+math.exp(-x))

xArr = np.arange(-10,10,0.1)
yArr = []
for i in range(xArr.size):
    yArr.append(sigmoid(xArr[i]))


c = 1
b = 0
wArr = [0.5,1,2,3]
for w in wArr:
    yArr=[]
    for i in range(xArr.size):
        yArr.append(c*sigmoid(b+w*xArr[i]))
    #plot.plot(xArr,yArr,label=w)
    

c = 1
bArr = [-3,0,3]
w = 1
for b in bArr:
    yArr=[]
    for i in range(xArr.size):
        yArr.append(c*sigmoid(b+w*xArr[i]))
    #plot.plot(xArr,yArr,label=b)

cArr = [-3,-1,1,3]
b = 0
w = 1
for c in cArr:
    yArr=[]
    for i in range(xArr.size):
        yArr.append(c*sigmoid(b+w*xArr[i]))
    plot.plot(xArr,yArr,label=c)
     
plot.legend()



plot.show()


