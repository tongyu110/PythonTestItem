try:
	r = open('t.txt','r');
	print(r.read());
except Exception as e:
	print(e);
finally:
	if r:
		r.close();
