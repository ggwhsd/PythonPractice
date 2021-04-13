#!/usr/bin/python
# -*- coding:UTF-8 -*-

print("*"*10,"类的使用，以及Socket的Server端","*"*10)

class Employee:
	empCount=0
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Employee.empCount+=1

	def displayCount(self):
		print(Employee.empCount)

	def displayEmployee(self):
		print(self.name, self.salary)

	def __del__(self):
		class_name = self.__class__.__name__
		print(class_name, "destroy")


e1 = Employee("tom",123)
e2 = Employee("jack",321)
e1.displayCount()
e2.displayCount()


class Parent:
	parentAttr=100;
	def __init__(self):
		print("parent init")

	def parentMethod(self):
		print("parent method")

	def setAttr(self,attr):
		Parent.parentAttr=attr;

	def getAttr(self):
		print("parent ",Parent.parentAttr)

	def method(self):
		print("parent ")


class Child(Parent):
	def __init__(self):
		print("child init")

	def childMethod(self):
		print("childMethod")

	def method(self):
		print("child ")

c1 = Child()
p1 = Parent()
c1.method()

import socket

class Server:
	s = socket.socket()
	__host = socket.gethostname()
	__port = 12345
	s.bind((__host,__port))

	def start(self):
		self.s.listen(5)
		while True:
			c,addr = self.s.accept()
			print("accept address ",addr)
			c.send('welcome')
			c.close()

server = Server()
#server.start()



