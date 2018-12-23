# Functions
# can't keep a function with any body but we use 'pass' keyword for later enhancements


def hello_func():
    pass


hello_func()
print(hello_func())

# adding some body


def hello_func():
    print('Hello Function')


hello_func()

# DRY - Don't Repeat Yourself, keep your code DRY.
# returns in functions - machine that takes input and produces result


def hello_func():
    return 'Hello Function'


print(hello_func())
print(hello_func().upper())

# pass arguments


def hello_func(greeting):
    return '{} Function'.format(greeting)


print(hello_func('Hi'))

# scope of the function is local to the function and doesn't affect the other function
# also good have a default argument


def hello_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(hello_func('Hi', name='Corey'))

# advanced func: args, kwargs are convension, * -> random number of arguments


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']

info = {'name': 'John', 'age': 22}
student_info(courses, info)

# adding * and ** to unpack the values from our list and dicts
student_info(*courses, **info)
