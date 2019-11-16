import os
os.mkdir("./testMkdir")

content=''' i am a programer and lucky dog
do you love me?
'''
file=open(r"./text.txt",'w')
file.write(content)
file.close()

fr=open(r"./text.txt")
while True:
	line=fr.readline()
	if len(line)==0:
		break
	print line
fr.close()
