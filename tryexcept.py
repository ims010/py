# try and except

# try:
#     f = open('testfile.txt')
# except Exception:
#     print("Sorry the file does not exist!")
# else:
#     print(f.read())
#     f.close()
# finally:
#     print('Executing Finally...')


# try:
#     f = open('testfile.txt')
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print('Executing Finally...')


try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
        raise Exception
# except FileNotFoundError as e:
#     print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')
