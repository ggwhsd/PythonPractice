
# -*- coding: utf-8 -*-

import xlsxwriter

workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type':'column'})
title = [u'名称',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日',u'平均流量']
buname=['name1','name2','name3','name4','name5','name6','name7']
data = [
[150,152,158,140,155,156,121],
[150,152,158,140,155,156,121],
[110,110,110,110,155,156,121],
[150,152,158,140,155,156,121],
[150,152,158,140,155,156,121]
]
format = workbook.add_format()
format.set_border(1)
format_title = workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')
format_title.set_align('center')
format_title.set_bold()

format_ave = workbook.add_format();
format_ave.set_border(1)
format_ave.set_num_format('0.00')

worksheet.write_row('A1',title,format_title)
worksheet.write_column('A2',buname,format)
worksheet.write_row('B2',data[0],format)
worksheet.write_row('B3',data[1],format)
worksheet.write_row('B4',data[2],format)
worksheet.write_row('B5',data[3],format)
worksheet.write_row('B6',data[4],format)

def chart_series(cur_row):
	worksheet.write_formula('I'+cur_row,\
		'=AVERAGE(B'+cur_row+':H'+cur_row+')',format_ave)
	chart.add_series({
		'categories':'=Sheet1!$B$1:$H$1',
		'values':'=Sheet1!$B$'+cur_row+':$H$'+cur_row,
		'line':{'color':'black'},
		'name':'=Sheet1!$A$'+cur_row
		})

for row in range(2, 7):
	chart_series(str(row))

chart.set_size({'width':577,'height':287})
chart.set_title({'name':'data display'})
chart.set_y_axis({'name':'Mb/s'})

worksheet.insert_chart('A8',chart)
workbook.close()