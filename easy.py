import os
def go_to_folder():
	folder = input('Введите имя директории: ')
	if os.path.isdir(folder):
			print('Успешно перешел')
	else:
		print('Невозможно перейти')
def look_at_folder():
	try:
		folder = input('Введите имя директории: ')
		menu = os.listdir(folder)
		if len(menu) > 0:
			print('Содержимое папки: ')
			for i in menu:
				print(i)
		else:
			print('Эта папка пустая')
	except:
		print('Невозможно вывести')
def delete_folder():
	folder = input('Введите имя директории: ')
	try:
		if os.path.isdir(folder):
			os.rmdir(folder)
		else:
			print('Невозможно удалить')
	except:
		print('Невозможно удалить')
def create_folder():
	folder = input('Введите имя директории: ')
	try:
		os.mkdir(folder)
	except:
		print('Невозможно создать')