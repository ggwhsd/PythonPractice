# -*- coding: UTF-8 -*-
#利用树的方式，堆的形式，来进行组织优先队列
#插入和弹出的时间复杂度都是O(logN)，建立堆的复杂度时O(n)
class PrioQueueError(ValueError):
	pass
class PrioQueue:
	def __init__(self,elist=[]):
		self._elems = list(elist)  #创建一个elist的副本，而不是使用引用，避免出现问题
		if elist:
			self.buildheap()  #通过一个list对象初始化优先级队列，在正常使用时，我觉得不会这一步，因为初始时队列就是空的。

	def is_empty(self):
		return not self._elems

	def peek(self):
		if self.is_empty():
			raise PrioQueueError
		return self._elems[0]

	def enqueue(self,e):
		self._elems.append(None)
		self.siftup(e,len(self._elems)-1)

	def siftup(self, e, last):
		elems, i, j = self._elems, last, (last-1)//2
		while i>0 and e< elems[j]:
			elems[i] = elems[j]
			i , j = j, (j-1)//2
		elems[i] = e

	def dequeue(self):
		if self.is_empty():
			raise PrioQueueError("in dequeue")
		elems = self._elems
		e0 = elems[0]
		e = elems.pop()
		if len(elems)>0:
			self.siftdown(e, 0 , len(elems))
		return e0

	def siftdown(self, e, begin, end):
		elems , i, j = self._elems, begin, begin*2+1
		while j<end:
			if j+1 < end and elems[j+1] < elems[j]:
				j +=1
			if e < elems[j]:
				break
			elems[i] = elems[j]
			i,j = j, 2*j + 1
		elems[i] = e

	def buildheap(self):
		end = len(self._elems)
		for i in range(end//2, -1, -1):
			self.siftdown(self._elems[i],i,end)

if __name__ == '__main__':
	pass
else:
	print("Load module "+__file__)

