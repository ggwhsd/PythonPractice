# -*- coding: UTF-8 -*-

from ctypes import *
import time
import _ctypes

# 定义回调函数参数的结构体
class DevMsg(Structure):
    _fields_ = [("type", c_long),
                ("cardID", c_long),
                ("InstrumentID", c_char*30),
                ("bidPrice", c_double),
                ("isTrade", c_bool),
                ("Other", c_char_p)
                ]