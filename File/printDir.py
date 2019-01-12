import os

#主要目地是遍历目录，输出目录与文件名


def printDirName(path,level):
	'''输出目录与文件名'''
	if not os.path.exists(path):
		return false

	if level == 0:
		print(path)

	separator = '-'	
	while level > 0:
		separator = separator+"--"
		level = level -1

	currentDirData = os.listdir(path)
	for _file in currentDirData:
		_dir = os.path.join(path,_file)
		print(separator+_file)
		if os.path.isdir(_dir):
			printDirName(_dir,level+1)


if __name__ == '__main__':
	_dir = "D:\\xampp\\htdocs\\Ysm\\www.ysmerp.test\\public\\api\\AliOpenApi\\Conf"
	printDirName(_dir,0)