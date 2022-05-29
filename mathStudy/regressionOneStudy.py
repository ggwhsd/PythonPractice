# -*- coding: UTF-8 -*-

import math
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

'''
线性回归的算法，算法由数学推导而来。
'''

def linerRegression(xArr,yArr):
    xAvg = np.mean(xArr)
    yAvg = np.mean(yArr)
    n = len(xArr)
    sumXiYi=0
    sumXiXi=0
    for i in range(n):
        sumXiYi+=(xArr[i]*yArr[i])
        sumXiXi+=(xArr[i]*xArr[i])
    a = (sumXiYi - n*xAvg*yAvg)/(sumXiXi - n*xAvg*xAvg)
    b = yAvg - a * xAvg
    #print(" y = %0.2f * x + %0.2f"%(a,b))
    def linerPredict(xInput):
        y = a * xInput + b
        return y
    return linerPredict


xArr = [1970,1975,1980,1985,1990,1995,2000,2005]
yArr = [325.68,331.15,338.69,345.90,354.19,360.88,369.48,379.67]
predict=linerRegression(xArr,yArr)
print(predict(2010))
print(predict(2015))
xArr.append(2010)
yArr.append(predict(2010))

xArr.append(2015)
yArr.append(predict(2015))
plot.plot(xArr,yArr,'ro-')
plot.show()

#print(pd.Series(np.array(yArr)).rolling(5).mean())



