a = ['xue','peng','cheng'];
for i in range(len(a)):
	print(i, a[i])
else:
	print("Over")

a.insert(0,'first')
print(a)


a_count = -(len(a))
print(a_count)
print(a[:-2])

print(a[-3:-1])

print(a[:-4:-1])

print("-------------")
a.remove('xue')
print(a)


val = a.pop(0)
print(val)
print(a)

