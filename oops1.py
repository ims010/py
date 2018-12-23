# Python Object Oriented Programming
# OOPS1


class Employee:

    raise_amount = 1.04

    # Methods
    # self keyword is assigning values to instance as each instance is different here
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


# Instances
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Mat', 'Rat', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

# no need to pass any arguments for instance as self is already declared
print(emp_1.fullname())
print(emp_2.fullname())
# Running from class we need to manually pass the arguments
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))

# displaying full name of the employee
# print('{} {}'.format(emp_1.first, emp_1.last))

# calling from method, fullname
print(emp_1.fullname())


# OOPS2
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amount()
Employee.raise_amount()

# instead of hard coding the raise amount, we can define a raise amount variable and call it in our method.
# calling just the variable will thrown an error as we are defining the raise amount outside the method, we need to call it with the class like Employee.raise_amount or self.raise_amount

# OOPS3 - Regular method, Class method and Static method


# OOPS1 - Repeated
