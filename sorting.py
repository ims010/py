li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
# sorting different dataytypes, objects by custom citeria
print(li)

# print in ascending order
s_li = sorted(li)
print('Sorted list', s_li)
print('Original list', li)

# sort() method sorts the original list permanently(operates on original list) but the sorted() function returns a new sorted list and returns(none)(doesn't operate on original list).
# sorted() function returns none and creates new list
# sot() method returns the sorted original list
print('Sorted list', s_li)
li.sort()
print('Original list', li)

# sorting in descending order
s_li = sorted(li, reverse=True)
print(s_li)
li.sort(reverse=True)
print(li)

# Why sorted function over sort method
# sort method works only on list, so tuples doesn't have inbuilt sort method
# sorted function gives more felexibilty

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
print(tup)
# tup.sort() -> gives error -> AttributeError: 'tuple' object has no attribute 'sort'
s_tup = sorted(tup)
print(s_tup)

# on dictionary
di = {'name': 'Corey', 'job': 'Programming', 'age': 'None', 'os': 'Mac'}
s_di = sorted(di)
print(s_di)

# working on absolute values
li2 = [-6, -5 - 4, 1, 2, 3]
s_li2 = sorted(li2)
print(s_li2)

#  key=abs, sorted negative first but if we need positive first, key attribute is very important while working with the named attributes
s_li2 = sorted(s_li2, key=abs)
print(s_li2)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # function to print the data as required
    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


emp1 = Employee('Carl', '36', '70000')
emp2 = Employee('Mat', '35', '65000')
emp3 = Employee('John', '30', '60000')

employees = [emp1, emp2, emp3]

# key=abd is builtin function, e_sort is a custom function to sort based on a specific paramater else python will throw error -> unorderable types: Employee() < Employee
# s_employees = sorted(employees) - can't be used

# based on name


def e_sort(emp):
    return(emp.name)


s_employees = sorted(employees, key=e_sort)
print(s_employees)

# based on age


def e_sort(emp):
    return(emp.age)


s_employees = sorted(employees, key=e_sort)
print(s_employees)

# based on salary


def e_sort(emp):
    return(emp.salary)


s_employees = sorted(employees, key=e_sort)
print(s_employees)

# reverse= True can reverse the order
# using lambda function
s_employees = sorted(employees, key=lambda e: e.name)
print(s_employees)


# also can use attrgetter from builtin operator() module
from operator import attrgetter
s_employees = sorted(employees, key=attrgetter('name'))
print(s_employees)
s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)
s_employees = sorted(employees, key=attrgetter('salary'))
print(s_employees)
