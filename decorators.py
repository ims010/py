# # Decorators

# def outer_function():
#     message = 'Hi'

#     def inner_function():
#         print(message)
#     return inner_function()


# outer_function()

# # Executing the outer_function without (), by doing so the inner_function() is waiting to be executed.

# def outer_function():
#     message = 'Hi'

#     def inner_function():
#         print(message)
#     return inner_function()


# outer_function


# # Executing the outer_function without (), by doing so the inner_function() is waiting to be executed. Now assigning outer_function to a variable and executing the variable

# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print(message)
#     return inner_function


# my_func = outer_function()
# my_func()


# # Reducing code
# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function()


# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')
# hi_func()
# bye_func()

# # Decorators - a function that takes another function as an argument adds some kind of functionality and then returns another function, all of this without altering the source code of the original function that was passed in

# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function


# def display():
#     print('Display function ran')


# decorated_display = decorator_function(display)
# decorated_display()


# # Using '@' symbol to call the decorators but its similar to assigning the function to a variable and calling the variable. We can add more functionality to wrapper function() without changing the code of outer function

# def decorator_function(original_function):
#     def wrapper_function():
#         print('Wrapper executed before {}'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function


# @decorator_function
# def display():
#     print('Display function ran')


# display()

# # Adding more functionality
# def decorator_function(original_function):
#     def wrapper_function():
#         print('Wrapper executed before {}'.format(original_function.__name__))
#         return original_function()
#     return wrapper_function


# @decorator_function
# def display():
#     print('Display function ran')


# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))


# display_info('John', 25)

# # adding *args, **kwargs to accept the arbitrary number of arguments
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('Wrapper executed before {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function


# @decorator_function
# def display():
#     print('Display function ran')


# @decorator_function
# def display_info(name, age):
#     print('display_info ran with arguments ({}, {})'.format(name, age))


# display_info('John', 25)

# # Classes as decorators

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print('Display function ran')


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
