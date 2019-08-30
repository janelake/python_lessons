import sys
import os
import shutil

name = sys.argv[0]
newfile = name.split('.py')
newfile = newfile[0] + '.dupl' + '.py'
shutil.copy(name, newfile)
