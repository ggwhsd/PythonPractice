# -*- coding: UTF-8 -*-
# sudo python2 -m pip install pycurl

import os,sys
import time
import pycurl

URL="www.qq.com"
c=pycurl.Curl()
c.setopt(pycurl.URL,URL) 
c.setopt(pycurl.CONNECTTIMEOUT,5)  #连接等待时间
c.setopt(pycurl.TIMEOUT,5) #请求超时时间
#c.setopt(pycurl.NOPROGRESS)
c.setopt(pycurl.FORBID_REUSE,1) #请求之后，断开链接，不重用
c.setopt(pycurl.MAXREDIRS,1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA,indexfile)

try:
	c.perform()
except Exception,e:
	print "connection error:"+str(e)
	indexfile.close()
	c.close()
	sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

print "HTTP_CODE :%s"%(HTTP_CODE)
print "NAMELOOKUP_TIME:%.2f ms"%(NAMELOOKUP_TIME)
print "CONNECT_TIME:%.2f ms" %(CONNECT_TIME)
print "PRETRANSFER_TIME:%.2f ms"%(PRETRANSFER_TIME)
print "STARTTRANSFER_TIME:%.2f ms"%(STARTTRANSFER_TIME)
print "TOTAL_TIME:%.2f ms"%(TOTAL_TIME)
print "SIZE_DOWNLOAD:%d bytes"%(SIZE_DOWNLOAD)
print "HEADER_SIZE:%d bytes"%(HEADER_SIZE)
print "SPEED_DOWNLOAD:%d" %(SPEED_DOWNLOAD)
indexfile.close()
c.close()
