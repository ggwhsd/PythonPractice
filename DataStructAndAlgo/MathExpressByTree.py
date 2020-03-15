
# -*- coding: UTF-8 -*-

#表达式求算数运算，使用元组方式的二叉树形式

#  3 *（ 2 + 5 ） =》 ('*',3,( '+' , 2 , 5))

#基本算数表示
def make_sum(a, b):
	return('+',a,b)

def make_prod(a, b):
	return('*', a,b)

def make_diff(a,b):
	return('-',a,b)

def make_div(a,b):
	return ('/',a,b)

#区分基本表达式 和 复合表达式
def is_basic_exp(a):
	return not isinstance (a,tuple)

def is_number(x):
	return (isinstance(x,int) or isinstance(x,float) or isinstance(x,complex))

#表达式求值解析

def eval_exp(e):
	if is_basic_exp(e):
		return e
	op, a, b = e[0], eval_exp(e[1]),eval_exp(e[2])   #递归解析表达式，只有基础数才能计算
	if op == '+':
		return eval_sum(a,b)
	elif op == '-':
		return eval_diff(a,b)
	elif op == '*':
		return eval_prod(a,b)
	elif op == '/':
		return eval_div(a,b)
	else:
		raise ValueError("UnSupport operator:",op)

#具体表达式的计算,(求值器)
def eval_sum(a, b):
	if is_number(a) and is_number(b):
		return a + b;
	if is_number(a) and a == 0:
		return b
	if is_number(b) and b == 0:
		return a
	print("??make_sum")
	return make_sum(a,b)

def eval_diff(a, b):
	if is_number(a) and is_number(b):
		return a - b;
	if is_number(a) and a == 0:
		return -b
	if is_number(b) and b == 0:
		return a
	return make_diff(a,b)

def eval_div(a,b):
	if is_number(a) and is_number(b):
		return a/b
	if is_number(a) and a == 0:
		return 0
	if is_number(b) and b == 1:
		return a
	if is_number(b) and b == 0:
		raise ZeroDivisionError
	return make_div(a,b)

def eval_prod(a,b):
	if is_number(a) and is_number(b):
		return a*b
	if is_number(a) and a == 0:
		return 0
	if is_number(b) and b == 1:
		return a
	if is_number(b) and b == 0:
		return 0
	if is_number(a) and a == 1:
		return b
	return make_prod(a,b)

if __name__ == '__main__':
	e1 = make_sum(make_sum(2,make_prod(2,2)),make_sum(2,make_sum(1,3)))
	print(e1)
	print(is_basic_exp(e1))
	print(eval_exp(e1))


else:
	print("Load module "+__file__)



