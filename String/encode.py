import string

s = "我很好"
print(s)
print(s.encode('gb2312'))


s1 = "I love you"
if s1.lower().islower():
	print(s1.upper())
else:
	print("false")

print(s1.swapcase())

s2 = "I love You"
print(s2.capitalize())

print(string.capwords(s2))