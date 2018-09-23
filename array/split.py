numbers = [1,2,3,4,5,6,7,8,9,0]
num = numbers
num[9] = 10
print(numbers)

numbers.insert(3,"four")
i = numbers.index("four")
print(i)