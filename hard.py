name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = int(input("Введите ваш возраст: "))
weight = float(input("Введите ваш вес: "))
if age >= 12 and age < 15:
    if weight > 40 and weight < 58:
    	print(name, " ", surname, ", ", age, " год, " , " вы в хорошем состоянии")
    elif weight > 58:
    	print(name, " ", surname, ", ", age, " год, " , "вам следует чаще заниматься спортом")    
    else:
    	print(name, " ", surname, ", ", age, " год, " , " следует набрать вес!")
elif age >= 9 and age < 12:
	if weight > 31 and weight < 40:
		print(name, " ", surname, ", ", age, " год, " , " вы в хорошем состоянии")
	elif weight < 31:
		print(name, " ", surname, ", ", age, " год, " , " следует набрать вес!")
	else:
		print("Вы слегка упитанный ребенок")
elif age >= 7 and age < 9: 
	if weight > 22 and weight < 28:
		print(name, " ", surname, ", ", age, " год, " , " вы в хорошем состоянии")
	elif weight < 22:
		print(name, " ", surname, ", ", age, " год, " , " следует набрать вес!")
	else:
		print(name, " ", surname, ", ", age, " год, " , "вы слегка упитанный ребенок")
elif age >= 5 and age < 7:
	if weight >= 15.5 and weight <= 21:
	    print(name, " ", surname, ", ", age, " год, " , " вы в хорошем состоянии")
	elif weight < 15.5:
		print(name, " ", surname, ", ", age, " год, " , " следует набрать вес!")
	else: 
		print(name, " ", surname, ", ", age, " год, " , "вы слегка упитанный ребенок")
elif age >= 15 and age <= 17:
	if weight >= 50 and weight <=67:
		print(name, " ", surname, ", ", age, " год, " , " вы в хорошем состоянии")
	elif weight < 58:
		print(name, " ", surname, ", ", age, " год, " , " следует набрать вес!")
	else:
		print(name, " ", surname, ", ", age, " год, " , "вам следует заняться собой")
elif age > 17 and age < 25:
	if weight > 55 and weight < 80:
		print(name, " ", surname, ", ", age, " год, " , " вы в хорошем состоянии")
	elif weight < 55:
		print(name, " ", surname, ", ", age, " год, " , " следует набрать вес!")
	else:
		print(name, " ", surname, ", ", age, " год, " , "вам следует заняться собой")
elif age >= 25:
	if weight > 55 and weight < 100:
		print(name, " ", surname, ", ", age, " год, " , " вы в хорошем состоянии")
	elif weight > 100:
		print(name, " ", surname, ", ", age, " год, " , "вам следует чаще заниматься спортом")
	else:
		print(name, " ", surname, ", ", age, " год, " , " следует набрать вес!")
else:
	print("Таких данных в нашей программе еще нет, но они скоро появятся!")
