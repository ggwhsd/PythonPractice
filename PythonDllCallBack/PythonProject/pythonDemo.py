# -*- coding: UTF-8 -*-
from data import DevMsg
from ctypes import *
import time
import _ctypes
# 定义功能类与方法
class DemoDll:

    def __init__(self):
        self.dll = cdll.LoadLibrary('PythonDllCallBack.dll')
        return

    def callBackStartWork(self, callback):
        return self.dll.callBackStartWork(callback)

    def getData(self,p):
        self.dll.getData.argtypes = [c_char_p]
        self.dll.getData.restype = c_char_p
        arg1 = c_char_p(bytes(p, 'utf-8'))
        return self.dll.getData(arg1)

# ctypes通过 CFUNCTYPE 支持回调函数，定义返回值与参数，第一个参数表示返回值，void为None，第二参数为回调函数的参数为结构体指针
CALLBACK = CFUNCTYPE(None, POINTER(DevMsg))

# 回调函数距离功能实现    
def _callback(para):
    # print(dir(para))
    obj = para.__getitem__(0)

    print(obj.type, obj.cardID, obj.InstrumentID, obj.bidPrice, obj.isTrade, obj.Other)

class CallBackTest(object):
    def __init__(self):
        self.msg = None

    def call_back(self,para):
        obj = para.__getitem__(0)
        
        print(obj.type, obj.cardID, obj.InstrumentID, obj.bidPrice, obj.isTrade, obj.Other)
        
        

if __name__ == '__main__':
    print("hello")
    # 定义回调函数
    callBackFunc = CALLBACK(_callback)
    #cbt = CallBackTest()
    #callBackFunc = CALLBACK(cbt.call_back)
    # 实例化功能类
    dll = DemoDll()

    type_p_int = POINTER(c_int)
    v = c_int(8)
    p_v = type_p_int(v)
    print(p_v[0])
    # 具体功能调用
    c = dll.callBackStartWork(callBackFunc)
    print(c)

    
    res=dll.getData("helloaa")
    print(res.decode())

