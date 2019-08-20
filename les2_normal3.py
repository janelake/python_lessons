import random
a = []
n = int(input("Введите количество элементов списка: "))
i = 0
while i < n:
	a.append(random.randint(-100, 100))
	i = i + 1
print(a)
