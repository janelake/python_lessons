import os
i = 1

for i in range(10):
    os.mkdir('dir_' + str(i))

for i in range(10):
    os.rmdir('dir_' + str(i))
