number = int(input("Введите число, которое больше 0, но меньше 10: "))
while number <= 0 or number >= 10:
    print("Вы ввели неверное число, попробуйте еще раз")
    number = int(input("Введите число, которое больше 0, но меньше 10: "))
else:
    print(number * number)
