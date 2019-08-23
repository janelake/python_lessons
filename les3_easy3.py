def strings(*args):
	return(max(args, key=len))
print(strings('Vasya', 'Vera', 'Maxim', 'Irina', 'Lisa', 'Vova', 'Anastasia'))