person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}
 
bank = [person1, person2, person3]
 
 
def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person
 
 
def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    else:
        return False
 
 
def check_account(person):
    return round(person['money'], 2)
 
 
def withdraw_money(person, money):
    if person['money'] >= money:
        person['money'] -= money
        return 'Вы сняли {} рублей. Оставшаяся сумма на карте {} рублей.'.format(money, round(person['money'],2))
    else:
        return 'На вашем счету недостаточно средств!'
 
 
def process_user_choice(choice, person):
    if int(choice) == 1:
        print(check_account(person))
    elif int(choice) == 2:
        count = float(input('Сумма к снятию:'))
        if count > 0:
            print(withdraw_money(person, count))
        else:
            print('Вы не можете снять отрицательное или нулевое значение с вашей карты!')
 
 
def start():
    person = 0
    card_number = -1
    pin_code = -1
    while card_number == -1 and pin_code == -1:
        try:
            card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
        except:
            print('Вы ввели только номер карты или пинкод. Введите оба значение!')
    card_number = int(card_number)
    pin_code = int(pin_code)
    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        while True:
            choice = int(input('Выберите пункт:\n'
                               '1. Проверить баланс\n'
                               '2. Снять деньги\n'
                               '3. Выход\n'
                               '---------------------\n'
                               'Ваш выбор:'))
            if choice == 3:
                break
            process_user_choice(choice, person)
    else:
        print('Номер карты или пин код введены не верно!')
        
start()
