a = [1, 2, 4, 5, 6, 2, 5, 2]
b = set(a)
c = []
print(" Неповторяюиеся элементы списка: ", list(b))
n = 0
i = 0
while i < len(a):
        n = a.count(a[i])
        if n == 1:
                c.append(a[i])
        i = i + 1
print(c)
