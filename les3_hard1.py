def attack(attacker, defender):
    defender['health'] = defender['health'] - attacker['damage']
    print('Игрок ', attacker['name'], ' нанес удар игроку ', defender['name'])
    print(attacker['name'], '- health: ', attacker['health'])
    print(defender['name'], '- health: ', defender['health'])
def armor(attacker, defender):
    return attacker['damage']/defender['armor']
def file_reader(name):
    file = open(name)
    file.seek(0)
    for line in file:
        a = line.split()
        player_1[a[0]] = a[2]
    print(player_1)
    file.close()
player_1 = {'name': '', 'health': 100, 'damage': 20, 'armor': 1.2}
player_2 = {'name': '', 'health': 100, 'damage': 35, 'armor': 1.2}
player_1['name'] = input('Введите имя первого игрока:')
player_2['name'] = input('Введите имя второго игрока:')
n = input("Введите имя игрока, который наносит удар: ")
while n != player_1['name'] or n != player_2['name']:
    if n == player_1['name']:
        attack(player_1, player_2)
        print("Урон по отношению к броне: ", round(armor(player_2, player_1),1))
        break 
    elif n == player_2['name']:
        attack(player_2, player_1)
        print("Урон по отношению к броне: ", round(armor(player_1, player_2), 1))
        break
    else:
        print("Вы ввели неверное имя. Попробуйте еще раз.")
        n = input("Введите имя игрока, который наносит удар: ")
file = open(player_1['name'] + '.txt', 'w+')
for i in player_1:
    l = str(i) + ' - ' + str(player_1[i])
    file.write(l)
    file.write('\n')
file.close()
file = open(player_2['name'] + '.txt', 'w')
for i in player_2:
    l = str(i) + ' - ' + str(player_2[i])
    file.write(l)
    file.write('\n')
file.close()
file_reader('jane.txt')


