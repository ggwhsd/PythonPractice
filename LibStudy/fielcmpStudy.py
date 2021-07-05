#fielcmpStudy.py
import filecmp
import os,sys
import re
import shutil

holderlist=[]

def compareme(dir1,dir2):
	dircmp=filecmp.dircmp(dir1,dir2)
	only_in_one=dircmp.left_only
	diff_in_one=dircmp.diff_files
	dirpath=os.path.abspath(dir1)
	[holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_one]
	[holderlist.append(os.path.abspath(os.paht.join(dir1,x))) for x in diff_in_one]
	if len(dircmp.common_dirs>0):#判断是否存在相同子目录
		for item in dircmp.common_dirs:
			compareme(os.path.abspath(os.path.join(dir1,item)),os.path.abspath(os.path.join(dir2,item)))
	return holderlist

def main():
	if len(sys.argv)>2:
		dir1 = sys.argv[1]
		dir2 = sys.argv[2]
	else:
		print "Usage:",sys.argv[0]," datadir backupdir"
		sys.exit()
	source_files=compareme(dir1,dir2)
	dir1=os.path.abspath(dir1)

	if not dir2.endwith('/'):dir2 = dir2+'/'
	dir2=os.path.abspath(dir2)
	destination_files=[]
	createdir_bool=False

	for item in source_files:
		destination_dir=re.sub(dir1,dir2,item)  #正则表达式 替换，将item中匹配dir1的部分替换为dir2.
		destination_files.append(destination_dir)
		if os.path.isdir(item):
			if not os.path.exists(destination_dir):
				os.makedirs(destination_dir)
				createdir_bool=True


	if createdir_bool:
		destination_files=[]
		source_file=[]
		source_files=compareme(dir1,dir2)
		for item in source_files:
			destination_dir=re.sub(dir1,dir2,item)
			destination_files.append(destination_dir)

	print "update item:"
	print source_files
	copy_pair=zip(source_files,destination_files)
	for item in copy_pair:
		if os.path.isfile(item[0]):
			shutil.copyfile(item[0],item[1])

if __name__ == '__main__':
	main()


