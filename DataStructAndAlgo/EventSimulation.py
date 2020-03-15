# -*- coding: UTF-8 -*-
# 离散事件模拟
from random import randint
from PrioQueueByHeap import PrioQueue
from SQueue import SQueue

class Simulation():
	def __init__(self, duration):
		self._eventq = PrioQueue()
		self._time = 0   #记录当前时间
		self._duration = duration    #记录模拟总时间

	def run(self):
		while not self._eventq.is_empty():
			event = self._eventq.dequeue()
			self._time = event.time()  
			if self._time > self._duration:  #事件时间超过了预设的模拟时间，则停止模拟
				break;
			event.run() #处理事件，这个事件可能会生成新的事件

	def add_event(self, event):
		self._eventq.enqueue(event)

	def cur_time(self):
		return self._time


class Event:
	def __init__(self,event_time,eventHost):
		self._ctime = event_time
		self._host = eventHost

	def __lt__(self, other_event):
		return self._ctime < other_event._ctime

	def __le__(self, other_event):
		return self._ctime <= other_event._ctime

	def host(self):
		return self._host

	def time(self):
		return self._ctime

	def run(self):
		pass   #具体事件类需要做的事情

#事件驱动的具体应用程序
class CustomsApplication:
	def __init__(self, gate_num, duration,arrive_interval, check_interval):
		self.simulation = Simulation(duration)     #模拟事件的驱动程序
		self.waitline = SQueue()    #等待的车辆队列
		self.duration = duration
		self.gates = [0]*gate_num   #收费口，使用中为1，空闲为0
		self.total_wait_time = 0
		self.total_used_time = 0
		self.car_num = 0.0
		self.arrive_interval = arrive_interval  #车辆到达间隔，模拟的使用其范围内的随机数
		self.check_interval = check_interval   #也是随机数的范围

	def wait_time_acc(self, n):
		self.total_wait_time += n

	def total_time_acc(self, n):
		self.total_used_time += n

	def car_count_1(self):
		self.car_num+=1

	def add_event(self,event):
		self.simulation.add_event(event)

	def cur_time(self):
		self.simulation.cur_time()

	def enqueue(self,car):
		self.waitline.enqueue(car)

	def has_queued_car(self):
		return not self.waitline.is_empty()

	def next_car(self):
		return self.waitline.dequeue()

	def find_gate(self):
		for i in range(len(self.gates)):
			if self.gates[i] == 0:
				self.gates[i] =1
				return i
		return None

	def free_gate(self,i):
		if self.gates[i] == 1:
			self.gates[i] = 0
		else:
			raise ValueError("Clear gate error")

	def simulateRun(self):
		Arrive(0,self)   #Arrive是可以自己产生产生事件的事件类，模拟车辆到达
		self.simulation.run()   #模拟事件驱动程序启动
		self.statistics()   #模拟程序运行完毕后，输出统计数据

	def statistics(self):
		print("Simulate " + str(self.duration) + " minute , for "+str(len(self.gates)) + " gates")
		print(self.car_num, " cars pass the customs")
		print("Average waiting time:", self.total_wait_time/self.car_num)
		print("Average passing time:",self.total_used_time/self.car_num)
		i = 0
		while not self.waitline.is_empty():
			self.waitline.dequeue()
			i += 1
		print(i," cars are in waiting line.")

class Car:
	def __init__(self, arraive_time):
		self.time = arraive_time;

	def arrive_time(self):
		return self.time


def event_log(time,name):
	print("Event:"+name+",happens at "+ str(time))
	pass

#事件类，包含了事件处理逻辑
class Arrive(Event):
	def __init__(self, arrive_time, customs):
		Event.__init__(self, arrive_time, customs)
		customs.add_event(self)  #事件创建的时候，自动加入到事件驱动中去。

	def run(self):
		time,customs = self.time(), self.host()
		event_log(time,"car arrive")
		#创建一个新的到底事件，模拟后续到达的车辆哦
		Arrive(time + randint(*customs.arrive_interval),customs)   # *运算符，此处可以理解为解引tuple为一个个元素
		car = Car(time)  #根据到达事件，生成车辆，进行排队或者进入海关
		if customs.has_queued_car():  #前面有排队的，则直接排队
			customs.enqueue(car)
			return
		else:  # 没有排队的，则直接去空闲的关口，若关口都不空闲，则还是排队
			i = customs.find_gate()  
			if i is not None:
				event_log(time, "car checking")
				Leave(time + randint(*customs.check_interval),i,car,customs)  #不用排队直接进入关口的，可以直接生成离开事件
			else:
				customs.enqueue(car)  

class Leave(Event):
	def __init__(self, leave_time, gate_num, car, customs):
		Event.__init__(self, leave_time,customs)
		self.car = car
		self.gate_num = gate_num
		customs.add_event(self)

	def run(self):
		time, customs = self.time(), self.host()
		event_log(time, "car leave")
		customs.free_gate(self.gate_num)
		customs.car_count_1()
		customs.total_time_acc(time-self.car.arrive_time())
		if customs.has_queued_car():
			car = customs.next_car()
			i = customs.find_gate()
			event_log(time,"car check")
			customs.wait_time_acc(time-car.arrive_time())  #从进入等待队列排队，到进入关口的耗时，只有排队的车才需要这个时间。
			Leave(time + randint(*customs.check_interval),
				self.gate_num,car,customs)







if __name__ == '__main__':
	car_arrive_interval = (1,2)
	car_check_time = (3,5)
	cus = CustomsApplication(3,480,car_arrive_interval,car_check_time)
	cus.simulateRun()
else:
	print("Load module "+__file__)