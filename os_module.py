import os
# access os properties
# to print all supported function in os module
print(dir(os))

# to print current working directory
print(os.getcwd())

# to change directory, need to use forward slash instead of backward
os.chdir('C:/Users/sgaviyappa/Desktop')
print(os.getcwd())

# to list all directories,files in current dir
print(os.listdir())

# To create dir
os.mkdir('os_demo')
os.makedirs('os_demo_2/sub_os_demo')
# makedirs used to create netsted dirs, mkdir gives error as the top level dir won't exist
print(os.listdir())

# Removing dir - rmdir removes the top level and gives error if sub dir exists but the removedirs removes all the dir recurrsively, use with caution
os.rmdir('os_demo')
os.removedirs('os_demo_2/sub_os_demo')
print(os.listdir())

# renaming a file/folder
# os.rename('text.txt', 'demo.txt')
print(os.listdir())

# printing the info about any file
print(os.stat('demo.txt'))
# st_size = size of the file
# st_mtime = modification time

# to print in human readable format
from datetime import datetime
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# traverse all the dir, yeilds a 3 value tuple
for dirpath, dirname, filename in os.walk('C:/Users/sgaviyappa/Desktop'):
    print('Current Path:', dirpath)
    print('Directories:', dirname)
    print('Files:', filename)

# environment variables
print(os.environ.get('C:/'))
# print path without slash
# file_path = os.environ.get('C:/Users/sgaviyappa/Desktop') + 'demo.txt'
# print(file_path)
# print path with slash
# file_path = os.path.join(os.environ.get('C:/Users/sgaviyappa/Desktop') + 'demo.txt')
# print(file_path)

# to check whether file or folder exists
print(os.path.exists('C:/Users/sgaviyappa/Desktop/demo.txt'))

# to check whether its a dir or file
print(os.path.isdir('C:/Users/sgaviyappa/Desktop/demo'))
print(os.path.isfile('C:/Users/sgaviyappa/Desktop/demo.txt'))

# to get the file extension, ext
print(os.path.splitext('C:/Users/sgaviyappa/Desktop/demo.txt'))

print(dir(os.path))
