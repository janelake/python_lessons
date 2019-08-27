my_list= [9, 4, 10, 23, 24.8, -4]
elements = [i for i in my_list if i % 3 == 0 or i > 0 or i % 4 != 0]
print(elements)
