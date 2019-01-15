import os

s = "dfd\python.py"
str = os.path.splitext(s)
print(str[1][1:])



print(os.path.split(__file__))

print(os.curdir)