# -*- coding: UTF-8 -*-

#list 实现 二叉树
def BinTree(data, left=None, right=None):
	return [data,left,right]

def is_empty_BinTree(btree):
	return btree is None

def root(btree):
	return btree[0]

def left(btree):
	return btree[1]

def right(btree):
	return btree[2]

def set_root(btree, data):
	btree[0] = data

def set_left(btree, left1):
	btree[1] = left1

def set_right(btree, right2):
	btree[2] = right2


if __name__ == '__main__':
	t1 = BinTree(2, BinTree(4), BinTree(8))

	set_left(left(t1),BinTree(5))
	


else:
	print("Load module "+__file__)

