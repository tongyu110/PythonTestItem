import numpy;

// 数组、元组、字典
dt = numpy.dtype([('id','i1'),('name','S20')]);

a = numpy.array([(1,'xue'),(2,'peng')],dtype=dt);
print(a['name']);