# -*- coding: UTF-8 -*-
#pip install psutil

import psutil
print 'file path ',psutil.__file__
mem = psutil.virtual_memory()
swap_mem = psutil.swap_memory()
cpu_times=psutil.cpu_times()
cpu_count = psutil.cpu_count()
cpu_total_time = cpu_times.user + cpu_times.system + cpu_times.idle
disk_info=psutil.disk_partitions()
disk_usage = psutil.disk_usage('/').percent
disk_io_count = psutil.disk_io_counters(perdisk=True)

print disk_io_count
print disk_usage
print disk_info
print 'swap_memory',swap_mem
print ('memory_used[%.2f%%]' %(float(mem.used)/float(mem.total)*100))

print 'cpu_count',cpu_count
print 'cpi_count,physic',psutil.cpu_count(logical=False)
print 'cpu_time_user[%.2f%%]'%(cpu_times.user/float(cpu_total_time)*100)

print psutil.net_io_counters()
print psutil.net_io_counters(pernic=True)['en0']
print psutil.users()[0]
import datetime
print 'bootTime ',datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y %m %d %H:%M:%S')

print psutil.pids()
for proc in psutil.process_iter(attrs=['pid', 'name']):
	print proc.info

