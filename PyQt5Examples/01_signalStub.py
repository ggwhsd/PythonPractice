
# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time

import pandas as pd
#import matplotlib.pyplot as plt
import datetime

class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("表格数据实时刷新显示")  # 设置表格名称
        # self.setWindowIcon(QIcon("ok.png"))  # 设置图标（图片要存在）
        self.resize(600, 400)  # 设置表格尺寸（整体大小）
        self.setColumnCount(20)  # 设置列数
        self.setRowCount(20)  # 设置行数
        self.setColumnWidth(0,10)  # 设置列宽(第几列， 宽度)
        self.setRowHeight(0, 20)  # 设置行高(第几行， 行高)

        column_name = [
            'instrument',
            'ask',
            'bid',
            'time',
            'col4',
        ]
        self.setHorizontalHeaderLabels(column_name)  # 设置列名称
        
        row_name = [
            '1',
            '2',
            '3',
        ]
        self.setVerticalHeaderLabels(row_name)  # 设置行名称

    def update_item_data(self, signalNum):
        """更新内容"""
        if "au9999" in tickMarket:
            self.setItem(0, 0, QTableWidgetItem("au9999"))
            self.setItem(0, 1, QTableWidgetItem(str(tickMarket["au9999"]["bid"])))  # 设置表格内容(行， 列) 文字
            self.setItem(0, 2, QTableWidgetItem(str(tickMarket["au9999"]["ask"])))  # 设置表格内容(行， 列) 文字
            self.setItem(0, 3, QTableWidgetItem(str(tickMarket["au9999"]["time"])) )


tickMarket={}

class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring

    def run(self):
        cnt = 0
        while True:  
            cnt += 1
            self.update_date.emit(str(cnt))  # 发射信号
            #time.sleep(1)
  
class ReceiveMarket(QThread):
    update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring
    
    def run(self):
        while True:
            tick= {}
            tick["time"] = datetime.datetime.now();
            tick["ask"]=112;
            tick["bid"]=110;
            tickMarket["au9999"]=tick
            self.update_date.emit(str(1))  # 发射信号
            time.sleep(0.01)
                      
if __name__ == '__main__':
    # 实例化表格
    app = QApplication(sys.argv)
    myTable = MyTable()
    # 启动更新线程
    #update_data_thread = UpdateData()
    #update_data_thread.update_date.connect(myTable.update_item_data)  # 链接信号
    #update_data_thread.start()
    produceMarket = ReceiveMarket()
    produceMarket.update_date.connect(myTable.update_item_data)  # 链接信号
    produceMarket.start()
    # 显示在屏幕中央
    desktop = QApplication.desktop()  # 获取坐标
    x = (desktop.width() - myTable.width()) // 2
    y = (desktop.height() - myTable.height()) // 2
    print("x,y = %d %d "%(x,y))
    myTable.move(x, y)  # 移动
    # 显示表格
    myTable.show()
    app.exit(app.exec_())


