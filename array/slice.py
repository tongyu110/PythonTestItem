def between(beg, end, mid):
 # 判断mid是否位于begin和end之间
 return end > mid >= beg or end < mid <= beg
 
 
def get_slice(a, beg, end, delta=1):
 # 数组切片get方式
 if delta == 0: raise ValueError("slice step cannot be 0")
 # 将负数下标转化一下
 if beg < 0: beg += len(a)
 if end < 0: end += len(a)
 # 如果转化完成之后依然不在合法范围内，则返回空列表
 if beg < 0 and end < 0 or beg >= len(a) and end >= len(a): return []
 # 如果方向不同，则返回空列表
 if (end - beg) * delta <= 0: return []
 # 将越界的部分进行裁剪
 beg = max(0, min(beg, len(a) - 1))
 end = max(-1, min(end, len(a)))
 ans = []
 i = beg
 while between(beg, end, i):
  ans.append(a[i])
  i += delta
 return ans
 
 
def set_slice(a, li, beg, end, delta=1):
 if delta == 0: raise ValueError("slice step cannot be 0")
 if delta == 1:
  # 如果delta==1，那么li的长度可以随意
  if beg < 0: beg += len(a)
  if end < 0: end += len(a)
  beg = max(0, min(beg, len(a) - 1))
  end = max(-1, min(end, len(a)))
  for i in range(beg, end):
   del a[beg]
  for i in reversed(li):
   a.insert(beg, i)
 else:
  # delta!=1,相当于替换
  if len(get_slice(a, beg, end, delta)) != len(li): raise ValueError("array don't match")
  if len(li) == 0: return
  if beg < 0: beg += len(a)
  if end < 0: end += len(a)
  beg = max(0, min(beg, len(a) - 1))
  # 用li中的全部元素逐一替换
  for ind, value in enumerate(li):
   a[ind * delta + beg] = value
 
 
def test_getSlice():
 a = list(range(10))
 import random
 for i in range(10):
  beg = random.randint(-15, 15)
  end = random.randint(-15, 15)
  delta = 0
  while delta == 0: delta = random.randint(-15, 15)
  print(len(get_slice(a, beg, end, delta)) == len(a[beg:end:delta]), beg, end, delta)
 
 
def test_setSlice():
 import random
 for i in range(10):
  a = list(range(10))
  beg = random.randint(-15, 15)
  end = random.randint(-15, 15)
  delta = 0
  while delta == 0: delta = random.randint(-5, 5)
  sz = len(a[beg:end:delta])
  if delta == 1: sz = random.randint(0, 4)
  li = [random.randint(0, 100) for i in range(sz)]
  set_slice(a, li, beg, end, delta)
  mine = a
  a = list(range(10))
  a[beg:end:delta] = li
  print(a == mine)
 
 
test_setSlice()