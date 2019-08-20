a = [9, 3, 45, 2, 44, 24, 98]
b = a
i = 0
while i < len(b):
        if b[i] % 2 == 0:
                b[i] = b[i] / 2
        else:
                b[i] = b[i] * 2
        i = i + 1
print(b)
