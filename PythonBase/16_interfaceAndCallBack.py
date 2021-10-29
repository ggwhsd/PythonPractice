# -*- coding: UTF-8 -*-


#展示回调接口的预留和实现， 继承的使用


class CTPTradeSPI:
    def OnRtnLogin(self):
        pass
    def OnGetCaptial(self, money:int):
        pass
    def OnRtnLogout(self):
        pass
    


LOGIN = 1
LOGOUT = 2
GETCAPTIAL = 3


class CTPTradeApi:
    
    def __init__(self):
        pass


    def RegisterSpi(self,spi):
        self.spi:CTPTradeSPI = spi


    def Login(self):
        self.__OnCall(LOGIN)


    def GetCaptial(self):
        self.__OnCall(GETCAPTIAL)


    def Logout(self):
        self.__OnCall(LOGOUT)


    def __OnCall(self,type:int=0):
        if type == LOGIN:
            self.spi.OnRtnLogin()
        if type == GETCAPTIAL:
            self.spi.OnGetCaptial(1000)
        if type == LOGOUT:
            self.spi.OnRtnLogout()




class MyTradeSpi(CTPTradeSPI):


    def __init__(self):
        pass


    def OnRtnLogin(self):
        print("OnRtnLogin")


    def OnGetCaptial(self, money:int):
        print("GetCaptial%d"%money)


    def OnRtnLogout(self):
        print("OnRtnLogout")


td = CTPTradeApi()
spi = MyTradeSpi()
td.RegisterSpi(spi)
td.Login()
td.GetCaptial()
td.Logout()

