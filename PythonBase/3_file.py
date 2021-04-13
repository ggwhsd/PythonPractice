import os

def printFenGeFu(msg:str):
    print("*"*10,msg,"*"*10)

printFenGeFu(" create dir ")
os.mkdir("./testMkdir")

printFenGeFu(" delete dir ")
os.rmdir("./testMkdir")

printFenGeFu(" file text write ")
content=''' i am a programer and lucky dog
do you love me?
'''
file=open(r"./text.txt",'w')
file.write(content)
file.close()

printFenGeFu(" file text read ")
fr=open(r"./text.txt")
while True:
	line=fr.readline()
	if len(line)==0:
		break
	print(line)
fr.close()
