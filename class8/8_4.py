import glob
# print(glob.glob('/home/romunuch/univer/python/*.py'))


import os

path=input('Input path to directory(ex:/home/romunuch/univer/python)\n')



print(os.listdir('/home/romunuch/univer/python/'))
print(os.listdir(path))