# -*- coding: UTF-8 -*-

import numpy as np
import math
xArr = [1,3,6,10,15,21]
yArr = [7,11,17,25,35,47]
print("样本协方差矩阵，显示的四个元素， cov(x,x),cov(x,y),cov(y,x),cov(y,y)。 "+ str(np.cov(xArr,yArr)))
print("xArr的协方差:%.2f"%np.cov(xArr))
print("xArr的方差:%.2f"%np.var(xArr))
print("yArr的方差:%.2f"%np.var(yArr))

Ex = np.mean(xArr)
print("xArr的期望:%.2f"%Ex)
Ey = np.mean(yArr)
print("yArr的期望:%.2f"%Ey)
SumExx = 0
for x in (xArr-Ex):
    SumExx+=x*x
Varx =SumExx/len(xArr)
print("xArr的方差:%.2f"%Varx)

print("xArr的sigma标准差:%.2f"%np.std(xArr))
print("yArr的sigma标准差:%.2f"%np.std(yArr))

sumEx_Ey =0
for i in range(len(xArr)):
    sumEx_Ey+=(xArr[i]-Ex)*(yArr[i]-Ey)
#以下两个函数都是协方差
cov_xy_sample =sumEx_Ey*1/ (len(xArr)-1)  #样本协方差
cov_xy=sumEx_Ey*1/ len(xArr)     #当n很大时，协方差=样本的协方差
print("cov(x,y)协方差:%.2f"%cov_xy)
print("cov(x,y)样本的协方差:%.2f 该值应该和np.cov算出来的值一样 %s"%(cov_xy_sample, abs(cov_xy_sample-np.cov(xArr,yArr)[0,1])<=0.0001))

rho = np.cov(xArr,yArr)[0,1] / (np.std(xArr)*np.std(yArr))
print("x和y相关系数corr(x,y):%f"%(rho))
#一般用下面这个来计算相关性，rho绝对值时小于等于1的，等于1表示存在y=ax+b的关系。
#皮尔逊相关系数，表示的线性关系，如果为0不代表没有非线性关系。所以独立一定不相关，但是不相关不一定独立。
rho= cov_xy / (np.std(xArr)*np.std(yArr))
print("x和y的皮尔逊相关系数，corr(x,y):%f"%(rho))
