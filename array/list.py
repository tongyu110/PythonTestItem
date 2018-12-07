months = ['January','February','March','April','May','June','July','August','September','October','November','December']
print(months[3:4])
print(months[3:8:2])			#步长
print(months[-3:-1])
month = input("Month:")
month_num = int(month)
print(months[month_num])



str = months
print str[0:3] #截取第一位到第三位的字符
print str[:] #截取字符串的全部字符
print str[6:] #截取第七个字符到结尾
print str[:-3] #截取从头开始到倒数第三个字符之前
print str[2] #截取第三个字符
print str[-1] #截取倒数第一个字符
print str[::-1] #创造一个与原字符串顺序相反的字符串
print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
print str[-3:] #截取倒数第三位到结尾
print str[:-5:-3] #逆序截取



#需要注意的是，列表切片产生的是列表的副本，与原列表不是同一份空间。
x=[1,2,3]
y=x[:]
x[0]=-1
print(y) #输出[1,2,3]