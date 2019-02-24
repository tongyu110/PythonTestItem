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



if __name__ == '__main__':
	re = calc(10)
	print(re)