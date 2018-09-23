def my_abs(x):
	if x>=0:
		return x;
	else:
		return -x;

def power(x, n=2):
    s = 1;
    while n > 0:
        n = n - 1;
        s = s * x;
    return s;

def fact(n):
	return fact_iter(n,1);

def fact_iter(num,product):
	if num == 1:
		return product;
	return fact_iter(num-1,num*product);	

def listRange(start,end):
	return list(range(start,end));

def generatorTest(datas):
	g = (x * x for x in datas);
	return g;	

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Python Hello, web!</h1>']
