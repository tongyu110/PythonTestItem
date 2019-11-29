import os
import copy
def sortpost(lis):
	"""冒泡排序"""
	for i in range(len(lis)-1):
		for j in range(len(lis)-1-i):
			if lis[j] > lis[j+1]:
				lis[j],lis[j+1] = lis[j+1],lis[j]
	return lis

def power(x,n):
	"""计算x的n次方"""
	val = 1
	for i in range(n):
		val = val * x
	return val

def calc(*number):
	"""计算a*a + b*b + c*c + …"""
	total = 0
	for n in number:
		total = total + n*n
	return total

def fac():
	total = 1
	num = int(input("请输入一个数字"))
	if num < 0:
		input("抱歉，负数没有乘阶")
	elif num == 0:
		input("0 的乘阶为 1")
	else:
		for i in range(1,num+1):
			total = total * i
	return total

def printDirFileName(path='.'):
	for d in os.listdir(path):
		print(d)

def strToLower(str):
	return str.lower()

def test1(x,y):
	x = y-x
	y = y-x
	x = y+x
	return {'x':x,'y':y}

def test():
	global Money
	Money = Money + 1

Money = 10

if __name__ == '__main__':
	test()
	print(Money)