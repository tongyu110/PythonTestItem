def find_last(string,str):
	last_position = -1;
	while True:
		position = string.find(str,last_position+1)
		if position == -1:
			return last_position
		last_position = position
		

string = "Hellow World"
str = "o"
print(find_last(string,str))
				