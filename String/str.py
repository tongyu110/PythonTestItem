#repr可以观察转义字符，不会翻译转义字符
s = "Hello world \n"
print(s)
print(str(s))		#人可以可以看懂
print(repr(s))		#计算机看懂

num = 0.0000001
print(num)
print(str(num))
print(repr(num))

# 输出结果
#Hello world

#Hello world

#'Hello world \n'
#1e-07
#1e-07
#1e-07