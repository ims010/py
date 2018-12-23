# Conditionals, if, else

if True:
    print('Conditional was True')

if False:
    print('Conditional was True')

language = 'Python'
if language == 'Python':
    print(True)

# Comparsion:
# Equals: ==
# Not Equals: !=
# Greater than: >
# Less Than: <
# Greate or Equal: >=
# Less or Equal: <=
# Object Identity: is   => checks whether the objects have same id in memory

language = 'Python'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Java')
elif language == 'JavaScript':
    print('JavaScript')
else:
    print('No Match')
# Python doesn't support switch case as is else are clean to handle


# and
# or
# not

user = 'Admin'
logged_in = True

# if two conditions needs to be checked
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# Or
logged_in = False
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# not
if not logged_in:
    print('Please log in')
else:
    print('Welcome')

# Object identity
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)

# printing id(in memory) of a and b
print(id(a))
print(id(b))

# is will check if the id the objects are the same
print(a is b)

# objects will get referenced in memory is assignment is used
b = a
print(id(a))
print(id(b))
print(a is b)


# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence, eg '', (), []
# Any empty mapping, eg {}

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 10
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = ()
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = []
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = ''
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
