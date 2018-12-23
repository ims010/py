import os

print(dir(os))

# current working directory
print(os.getcwd())

# Changing directories
os.chdir('C:/Users/sgaviyappa/Documents/python/')
print(os.getcwd())
# To see files and folders, by default picks current working directory
print(os.listdir())

