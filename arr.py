names = ['xue','peng','cheng'];
print('len:',len(names));

names.append('test');
print('append:',names);

names.insert(0,'first');
print('insert:',names);

names.pop();
print('pop:',names);



d = {'name':'xue','age':20,'sex':1};
print(d);
if d.get('name1'):
	print(d['name']);
else:
	print('not find');

for v in d:
	print(v);	


