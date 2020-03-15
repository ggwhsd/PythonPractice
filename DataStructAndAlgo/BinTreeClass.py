# -*- coding: UTF-8 -*-
#二叉树的类结构表示法，这也是实际常用的方法
from SQueue import *
from SStack import *

class BinTNode:
	def __init__(self, dat, left= None, right=None):
		self.data = dat
		self.left = left
		self.right = right

def count_BinTNode(t):
	if t is None:
		return 0
	else:
		return 1 + count_BinTNode(t.left) + count_BinTNode(t.right)

def sum_BinTNode(t):
	if t is None:
		return 0
	else:
		return t.data + sum_BinTNode(t.left) + sum_BinTNode(t.right)

#深度 先序遍历，递归方式
def preorder(t, proc):
	if t is None:
		return
	proc(t.data)
	preorder(t.left,proc)
	preorder(t.right,proc)

def print1(data):
	print(data)

#宽度遍历,比较简单，递归方式
def levelorder(t, proc):
	qu = SQueue()
	qu.enqueue(t)
	while not qu.is_empty():
		t = qu.dequeue()
		if t is None:
			continue;
		qu.enqueue(t.left)
		qu.enqueue(t.right)
		proc(t.data)

#深度访问，先序，采用非递归的方式（用栈）
def preorder_nonrec(t,proc):
	s = SStack()
	while t is not None or not s.is_empty():
		while t is not None:
			proc(t.data)
			s.push(t.right)
			t = t.left
		t = s.pop()

class BinTree:
	def __init__(self):
		self._root = None

	def is_empty(self):
		return self._root is None

	def root(self):
		return self._root

	def leftchild(self):
		return self._root.left

	def rightchild(self):
		return self._root.right

	def set_root(self, rootnode):
		self._root = rootnode

	def set_left(self, leftchild):
		self._root = leftchild

	def set_right(self, rightchild):
		self._root = rightchild

		#元素生成器，类似迭代器
	def preorder_element(self):
		t, s = self._root, SStack()
		while t is not None or not s.is_empty():
			s.push(t.right)
			yield t.data
			t = t.left
		t = s.pop()


if __name__ == '__main__':
	root = BinTNode(1,BinTNode(2),BinTNode(3))
	print(count_BinTNode(root))
	print(sum_BinTNode(root))
	preorder(root,print1)


else:
	print("Load module "+__file__)