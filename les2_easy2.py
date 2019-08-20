a = [1, 2, 3, 'str', 'galaxy', 28.9]
b = [2, 38, 56, 45.67, 28.9, 'str', 1]
a = set(a)
b = set(b)
a = a ^ b
print(a)
print(b)
