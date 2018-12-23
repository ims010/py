# Python Objct Oriented Programming
# Creating classes and instances
# Inheritance
# Class and instance variables
# Static method and classs method

# Creating classes and instances -

# Class - logically group data and functions in a way to reuse and also easy to build upon
# Data - Attributes
# Functions - Methods(a function that is associated with a class)


class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

# Class and a instance of a class: A class is basically a blueprint for creating instances
# Instance Variables cantain data that is unique to each instance, we can manually create instance variable for each employee like

emp_1.first = 'Nick'
emp_1.last = 'Jones'
emp_1.email = 'Nick.Jones@company.com'
emp_1.pay = 50000

emp_2.first = 'Sarah'
emp_2.last = 'Jones'
emp_2.email = 'Sarah.Jones@company.com'
emp_2.pay = 45000

print(emp_1.email)
print(emp_2.email)

# Instead of manually adding all these values, we can use a __init__ method


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # When we create methods within a class, they recieve the instance as the first argument automatically. By convension, self is used but anything can be used.
        # After self we can specify what all the argument we want to accept
        # self.first = first is same as emp_1.first = 'Nick'
        # When we create an object outside the __init__ method, instance is passed automatically, so we can leave off the self
        # __init__ method will be called automatically and instead of self the instance is called

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * 1.04)
        # self.pay = int(self.pay * raise_amount) -> will thrown an error when the instance tries to access this variable. so we can call it as Employee.raise_amount or self.raise_amount
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Nick', 'Mat', 60000)
emp_2 = Employee('Adia', 'Zora', 700000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

# Methods in class
# To print full name without using method
print('{} {}'.format(emp_1.first, emp_1.last))
# Else we can define a method within our class

print(emp_1.fullname())
print(emp_2.fullname())

# If self is not included in the method def, we gwt TypeError: <Method_Name> takes 0 positional arguments but 1 was given

# Running methods using class name iteself
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
# While calling a method from class name, we need to provide the instance but if call using the just the method, we don't need instance as the self is called as first instance of the method by default.


# Class variable and Instance variables
# Class variable are the variables that are shared among all instances of the class
# Instance variable can be unique to each instance(first, last, email).
# Class varaible should be the same for each instance(apply_raise)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)



# Regular, Class and Static methods
# Regular methods and class automatically take instance as the first argument, by convension, its self.

# Class methods called using decorators - @<decorator_name>
