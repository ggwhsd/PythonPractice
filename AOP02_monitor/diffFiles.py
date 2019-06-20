# -*- coding: utf-8 -*-

import difflib
import sys

tips = "Usage: diffFiles filename1 filename2"

try:
	#获取命令行的参数
	textfile1 = sys.argv[1]
	textfile2 = sys.argv[2]
except Exception,e:
	print "Error:"+str(e)
	print tips
	sys.exit()

def readfile(filename):
	try:
		#文件二进制读取
		fileHandler = open(filename, 'rb')
		text=fileHandler.read().splitlines();
		fileHandler.close()
		return text
	except IOError as error:
		print('Read file error : '+str(error))
		sys.exit()
#判断参数是否有效
if textfile1 == "" or textfile2 == "":
	print tips
	sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)
#比较两个文件中的内容，并且输出为html格式。
d = difflib.HtmlDiff()
print d.make_file(text1_lines,text2_lines)