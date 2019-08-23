a = ['Vasya', 'Lena', 'Max', 'Jane', 'Nastya', 'Boris', 'Kostya']
b = [2000, 3000, 4000, 5000, 4500, 2900, 3100]
dictionary = dict(zip(a,b))
file = open('salary.txt', 'w+')
i = 0
n = ' ' 
while i < len(a):
        n = str(a[i]) + '  -  ' +  str(b[i])
        file.write(n)
        file.write('\n')
        i = i + 1
file.seek(0)
for line in file:
        a = line.split()
        print(a[0].upper(), a[1], a[2]) 
file.close()
