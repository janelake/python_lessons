import re
name = input('Name: ')
surname = input('Surname: ')
email = input('Your email: ')
n_s_check = '[A-Z]{1,1}[a-z]'
mail_check = '[a-z_]+@[a-zA-Z0-9]+\.(ru|org|com)'
if re.match(n_s_check, name) == None:
            print(name, ' - неправильно введено имя')
if re.match(n_s_check, surname) == None:
            print(surname, ' - неправильно введена фамилия')
if re.match(mail_check, email) == None:
            print(email, ' - неправильно введен адрес почты')
