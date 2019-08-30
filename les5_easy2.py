import os
folders = []
for filename in os.listdir():
	if os.path.isdir(filename):
		folders.append(filename)
print(folders)
