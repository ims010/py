# LEGB - Local(function), Enclosing(enclosing function), Global(top-level), Built-in

x = 'global x'


def test():
    y = 'local y'
    # print(y)
    print(x)


test()
# print(y)
print(x)

# local and global variables


def test():
    x = 'local x'
    print(x)


test()

# updating global variable,


def test():
    global x
    x = 'local x'
    print(x)


test()

# keyword global will set the scope of the vailable outside the local function even though a gloable variable isn't declared but this practise isn't good as using the local scope of the varilable will help you understand the scope of that variable and easier to work and mantain code


def test(z):
    x = 'local x'
    print(z)


test('local z')
# print(z) - gives error as the scope is outside the function


# printing smallest value in the iterable, min() is builtin function
m = min([5, 1, 4, 2, 3])
print(m)

# import builtins
# print(dir(builtins))


# when calling a function, python check the global list of function then it will check in builtins folder, so always a custom function name as that it won't conflict with the builtin functions

# Enclosing - has to do with nested functions

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()

# commenting out inner x, so python will check for x varaiable in the inner function, when it doesn't find x, it looks in the enclosing function which outer() in this case


def outer():
    x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)


outer()

# updating the x variable to the main function using nonlocal statement


def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()


# LEGB rule

x = 'global x'


def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
print(x)
