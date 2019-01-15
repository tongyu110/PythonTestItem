#返回函数，再调用
def lazy_sum(*numbers):
	def sum():
		ax = 0
		for n in numbers:
			ax = ax + n
		return ax
	return sum


f = lazy_sum(1,2,3,4)
print(f())