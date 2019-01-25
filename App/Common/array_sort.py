#https://mp.weixin.qq.com/s/nL_1g0FMpz63h6TW0HVdtg
#冒泡排序
def sortport(lis):
	#lis = [56,12,1,8,354,10,100,34,56,7,23,456,234,-58]
	for i in range(len(lis)-1):
		for j in range(len(lis)-1-i):
			if lis[j] > lis[j+1]:
				lis[j],lis[j+1] = lis[j+1],lis[j]
	return lis

if __name__ == '__main__':
	lis = [56,12,1,8,354,10,100,34,56,7,23,456,234,-58]
	new_lis = sortport(lis)
	print(new_lis)