import easy
do = input ('Выберите действие: \n [1] -  Перейти в папку \n [2] - Просмотреть содержимое текущей папки \n [3] - Удалить папку \n [4] - Создать папку \n')
if do == '1':
           easy.go_to_folder()
elif do == '2':
           easy.look_at_folder()
elif do == '3':
           easy.delete_folder()
elif do == '4':
           easy.create_folder()
else:
        print('Вы ввели некоректные данные')



