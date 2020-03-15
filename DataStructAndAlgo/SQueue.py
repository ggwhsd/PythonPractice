# -*- coding: UTF-8 -*-

#SQueue
class QueueUnderflow(ValueError):
	def __init__(self):
		pass
#利用list数组，来作为队列的基础，并且数组采用循环使用方式。
class SQueue:
	def __init__(self,init_len=8):
		self._len = init_len #存储区长度
		self._elems = [0]*init_len
		self._head = 0
		self._num = 0
		self.__hello = "hello"

	def is_empty(self):
		return self._num == 0;

	def peek(self):
		if self._num == 0:
			raise QueueUnderflow
		return self._elems[self._head]

	def dequeue(self):
		if self._num == 0:
			raise QueueUnderflow
		e = self._elems[self._head]
		self._head = (self._head+1)%self._len
		self._num -= 1
		return e

	def enqueue(self, e):
		if self._num == self._len:
			self.__extend()
		self._elems[(self._head+self._num)%self._len] = e
		self._num += 1

	def __extend(self):
		old_len = self._len
		print("__extend old len "+str(old_len))
		self._len *= 2
		new_elems = [0]*self._len
		for i in range(old_len):
			new_elems[i]=self._elems[(self._head+i)%old_len]
		self._elems , self._head = new_elems, 0


if __name__ == '__main__':
	queue = SQueue()
	for i in range(100):
		queue.enqueue(i)
	while(queue.is_empty()==False):
		print(queue.dequeue());
	print(queue._head)


else:
	print("Load module "+__file__)



