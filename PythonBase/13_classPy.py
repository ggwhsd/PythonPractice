# -*- coding: UTF-8 -*-
from packageDerivedClass.Testpackage import getPackageOk

class Employee(object):
	empCount =0 #类属性

	def __init__(self,name,salary):

		self.name = name    #对象属性
		self.salary = salary
		Employee.empCount += 1

	def ShowCount(self):
		print("Totol %d"%(Employee.empCount))

	def Show(self):
		print("Name %s Salary %d"%(self.name,self.salary))

	@classmethod
	def ShowCountForClass(cls):
		print("Totol %d"%(Employee.empCount))

	@staticmethod
	def _isHighSalary(salary):
		if(salary>32000):
			print("highSalary good to work")
		else:
			print("lowSalary bad to work")

def testBaseClass():

	emp1 = Employee("jack1",30000)
	emp2 = Employee("jack2",31000)
	emp3 = Employee("jack3",50000)

	emp1.ShowCount()
	emp2.ShowCount()
	emp3.ShowCount()
	emp3.Show()
	Employee.ShowCountForClass()
	emp1._isHighSalary(33000);


class Manager(Employee):
	mgrCount =0

	def __init__(self,name,salary):
		self.bouns =   salary*10  #对象属性
		
		Employee.__init__(self,name,salary)
		Employee.empCount += 1
		Manager.mgrCount += 1

	def Show(self):
		#super(Manager,self).Show()
		print("Name %s Salary *** bouns %d"%(self.name,self.bouns))

class Worker():
	def __init__(self,name,salary):
		self.name = name    #对象属性
		self.salary = salary
	def Show(self):
		print("I don't know you")

def testDerivedClass():
	emp1 = Employee("jack1",30000)
	mgr1 = Manager("jack",60000)
	Worker1 = Worker("dd",100000000)
	mgr1.Show()
	peop=[]
	peop.append(emp1)
	peop.append(mgr1)
	peop.append(Worker1)
	#由于列表等类型中可以存储不同类型，所以以下方法相当于一种多态形式了。而没有使用类似C++中的虚函数。
	for x in peop:
		x.Show()


if __name__ == '__main__':
    print('作为主程序运行')
    print(__file__)
    #testBaseClass()
    #getPackageOk()
    testDerivedClass()
else:
    print('package_'+__file__+'初始化')


