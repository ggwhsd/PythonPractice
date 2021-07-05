# -*- coding: UTF-8 -*-
import xlsxwriter
workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A',20)
bold = workbook.add_format({'bold':True})
worksheet.write('A1','Hello')
worksheet.write(2,0,32.5)
worksheet.write(4,0,'=sum(A3:A4)')
workbook.close()
