# key is a unique identifier, like how we actual look into the dictinoary
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['courses'])
print(student['age'])

# accessing a invalid key, we get KeyError
# print(student['phone'])

# instead of calling the key, use get method to avoid KeyError
print(student.get('name'))

# display 'None' instead of the KeyError
print(student.get('phone'))

# display a custom message for an invalid key
print(student.get('phone', 'Not Found'))

# adding a new entry to dict
student['phone'] = '555-555'
print(student.get('phone'))

# if a key already exists, it updates the value
student['name'] = 'Jane'
print(student)

# UPdating multiple keys
student.update({'name': 'John', 'age': '30', 'phone': '666-6666'})
print(student)

# to delete a specific key and value
del student['age']
print(student)
popped = student.pop('phone')
print(popped)
print(student)

# number of keys
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# loop through the key will only print key
for key in student:
    print(key)

# for looping through key and value
for key, value in student.items():
    print(key, value)
