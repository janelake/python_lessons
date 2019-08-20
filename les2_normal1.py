import math
a =  [2, -5, 8, 9, -25, 25, 4]
print(a)
b = []
c = []
sqrt = 0
for i in a:
        sqrt = i ** 0.5
        b = str(sqrt).split('.')
        if i > 0 and b[1] == '0':
                c.append(int(b[0]))
        b.pop()
        b.pop()
print(c)

