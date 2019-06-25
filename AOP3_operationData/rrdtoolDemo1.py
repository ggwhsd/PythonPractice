# -*- coding: utf-8 -*-
import rrdtool
import time
cur_time = str(int(time.time()))
rrd=rrdtool.create('Flow.rrd','--step','300',cur_time,)