# -*- coding: UTF-8 -*-


class Employee:
    '员工基类'
    empCount = 0    #类变量


    '构造函数'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1


    def __del__(self):
        print(self.name + " 销毁")


    def displayCount(self):
        print("Total employee %d" % Employee.empCount)


    def displayEmployee(self):
        print("Name:"+self.name+" Salary:"+self.salary)




print(Employee.__doc__)
print(Employee.__module__)


t = Employee("T1",100)
t.displayCount()








class Parent:
    parentAttr = 100


    def __init__(self):
        print("parent")
        


    def parentMethod(self):
        print("parent method")


    def setAttr(self, attr):
        Parent.parentAttr = attr
        
    
    def getAttr(self):
        print(Parent.parentAttr)


    # to-do : 继承
    def method(self):
        pass


class Child(Parent):
    __privateData = 1 #只能内部使用
    _protectData = 2  #只能子类使用


    def __init__(self):
        print("child")


    def childMethod(self):
        print("child method")


    def method(self):
        super().method()
        print("child overwrite method")


    def __privateMethod(self):
        pass


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(20)
c.getAttr()
c.method()


print(issubclass(Child,Parent))
print(isinstance(c,Child))
print(isinstance(c,Parent))

