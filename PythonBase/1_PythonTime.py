# -*- coding: UTF-8 -*-

import time
ticks = time.time()
print "当前时间戳:",ticks

localtime = time.localtime(time.time())
print "本地时间:",localtime

print "本地时间：",time.asctime(time.localtime(time.time()))

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

a = "Mon Apr 22 19:45:48 2019"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

import calendar
 
cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal