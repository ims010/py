course = {'title': 'Python', 'teacher': {'firstname': 'John', 'Lastname': 'Swagger'}}
print(course)
print(course['title'])
print(course['teacher'])
print(course['teacher']['firstname'])

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['courses'])
print(student['age'])

# accessing a invalid key, we get KeyError
# print(student['phone'])

# instead of calling the key, use get() method to avoid KeyError, get() display 'None' instead of the KeyError
print(student.get('phone'))

# display a custom message for an invalid key
print(student.get('phone', 'Custom Message : Key is Invalid/Not Found'))

# # adding a new entry to dict
student['phone'] = '555-555'
print(student.get('phone'))

# if a key already exists, it updates the value
print(student)
student['name'] = 'Jane'
print(student)

# Updating multiple keys
student.update({'name': 'John', 'age': '30', 'phone': '666-6666'})
print(student)

# to delete a specific key and value
del student['age']
print(student)

# using popped variable to get the last variable removed using pop() method
popped = student.pop('phone')
print('Last value removed by pop(): {}'.format(popped))
print(student)

# number of keys
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
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
