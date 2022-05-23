# -*- coding: UTF-8 -*-
from __future__ import division 
import sympy as sy, math
import numpy as np
from sympy import *

print("hello");

print("普通的数学开平方再2次方，会有很多小数[%s]"% (str(math.sqrt(2) ** 2)))

print("sympy开平方再2次方，是没有小数的[%s]"% (str(sy.sqrt(2) ** 2)))

print("sympy是符号数学库，可以简单理解为跟人的计算方式一样，看见开根号和平方会直接处理得到原来的值，而不是先计算开根号的值再计算平方");



x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
f = (2/3)*x**2 + (1/3)*x**2 + x + x + 1
f.simplify()
print("输出表示的代数表达式[%s]"%f)

f=(x+1)*(y+2)
print("展开代数表达式[%s]"%expand(f))

print("还可以解方程")
print("2 * x-3 * y + z = 1")
print("x + y = 0")
print("3*x + y +5 = 0")
y1= 2*x-3*y+z -1
y2= x+y
y3= 3*x + y +5
value = solve([y1,y2,y3])
print(value)

print("求极限")
print(limit((x+10)**3 +100,x,a-10))
print(limit(sin(x)/x,x,0))

n = Symbol('n')
print(limit(((n+3)/(n+2))**n, n, oo))

print("对x求导1次")
print(diff(x**2, x,1) )
print("对x求导2次")
print(diff(x**2, x,2) )

print(diff(x**2+x*y**2, x,1,y,1) )

print("定积分")
f = x**2
print(integrate(f,(x,0,1)))

f=1/x
print(integrate(f,(x,2,3)))

print("不定积分")
print(integrate(f,x))

print("双重定积分")
f=2*x+3*y
print(integrate(f,(x,0,1),(y,1,2)))

print("双重不定积分")
f=2*x+3*y
print(integrate(f,(x,0,1),(y,-x,x)))

print("===================矩阵")
a,b,c,d,e,f,g,h=sy.symbols(['a','b','c','d','e','f','g','h'])
A = sy.Matrix([[a,b],[c,d]])
B = sy.Matrix([[e,f],[g,h]])
print(A+B)

λ,μ=sy.symbols(['λ','μ'])
print(λ*μ*A)

i,j,k,l,m,n=sy.symbols(['i','j','k','l','m','n'])
C=sy.Matrix([[i,j,k],[l,m,n]])
print(A*C)

A1 = sy.Matrix([[1,1],[-1,-1]])
A2 = sy.Matrix([[1,-1],[-1,1]])
print(A1*A2)

A1 = sy.Matrix([[2,-3],[-4,6]])
A2 = sy.Matrix([[8,4],[5,5]])
A3 = sy.Matrix([[5,-2],[3,1]])
print(A1*A2)
print(A1*A3)

A = sy.Matrix(np.zeros((2,2)))

print("行向量")
α=np.array(np.arange(5)).reshape(1,5)
α=sy.Matrix(α)
print(α)
print("列向量")
α=np.array(np.arange(5)).reshape(5,1)
α=sy.Matrix(α)
α
print("单位阵Identity matrix")
I=sy.eye(2)
print(I)

A = np.diag([3,3,3,3])
print(sy.Matrix(A))

A = np.diag([1,2,3,4])
print(sy.Matrix(A))

A1 = sy.Matrix([[a,0,0],[0,b,0],[0,0,c]])
B1 = sy.Matrix([[d,0,0],[0,e,0],[0,0,f]])
print(A1*B1)