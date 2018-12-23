# Lists are bag which holds any data types and are mutable(we can change the content on the fly), in python lists are kind of arrays(as in other language).
my_list = [1, 2, 3]
print(my_list)

# can't do my_list + 5 but can do with other things to list like
print(my_list + [4, 5])
print(my_list)

# this can be printed but won't add [4, 5] to my_list as we are not doing any assignment
my_list = my_list + [4, 5]
print(my_list)
my_list += [6, 7]
print(my_list)

# can't do subtraction and division on lists but we can multiply and add
print(my_list * 2)

# we can also use append method to add elements to list
my_list.append(8)
print(my_list)

# we can only one element at a time, for adding more than one element, we use extend and extend() adds the new element to the end of list
my_list.extend([9, 10, 11])
print(my_list)

# we can also have a list within a list
my_list.append([12, 13])
print(my_list)

# to remove elements or list inside the list
my_list.remove([12, 13])
print(my_list)
# removing a element which is not in list results in ValueError

# Converting lists, can't have list(5), give TypeError however we can have list('Hello!!!') which breaks each character as an element in the list
print(list('Hello!!!'))

# split breaks the string on whitespaces
print('hello there students'.split())

# can also tell split on what to break on
print('red:blue:green'.split(':'))

# we can also do based on certain number of splits, more info required

# Lists to strings
flavors = ['Chocolate', 'mint', 'Choco']
print(', '.join(flavors))
print("My favorite flavors are: " + ', '.join(flavors))
print("My favorite flavors are: {}".format(", ".join(flavors)))
# join works on only strings, can't do it on lists without string, like on numbers - TypeError
# '+ '.join([1, 2, 3])

# Indexing on lists and strings
alpha = 'abcde'
print(alpha)
print(alpha.index('a'))

# if multiple occurrence of same elements results in returning the index of first occurrence value
print('abcabdabc'.index('a'))

# index on lists
alpha_list = list(alpha)
print(alpha_list.index('b'))

# index on group of elements
# print(alpha_list.index('cd'))

# calling something isn't in list gives ValueError: substring not found
# print(alpha_list.index("ce"))

# Using indexes
print(alpha[0])
print(alpha[-1])
print(alpha[1])
print(alpha[-2])

# del keyword to deletion
trash = 99
del trash
# printing trash after removing gives a NameError

print(alpha_list)
del alpha_list[2]
print(alpha_list)

# can't delete more than one item from the list, gives TypeError: list indices must be integers, not tuple
# del alpha_list[1, 2]
# We can't delete elements from string, strings are immutable
# alpha = 'abcdef'
# del alpha[0]
# Throws TypeError: 'str' object doesn't support item deletion

# favorite_things += [" warm woolen mittens"]
# lists are mutable, so when we use +=, a new list is not created, however the existing list is modified.
# for using +, both of them have to be lists

# favorite_things.append() can append an element to list or add a list inside a list

# favorite_things.extend() will take a list of elements and insert to the list end of existing list as elements
# extend() can take an types which are iterable
# a = [1, 2, 3]
# a.extend('abc')
# print(a)
# del favorite_things[index]
# favorite_things.insert(index, "whatever element you want to add")




# From Corey's
# lists are defined in []
print('-------------------------------------------------------')
print("FROM COREY'S")
print('--------------------------------------------------------')


courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

# always good to keep a copy of original list
sorted_courses = sorted(courses)
print(sorted_courses)

# length of the list
print(len(courses))

# indexing starts with 0
print(courses[0])
print(courses[3])

# negative indexing works in reverse order
print(courses[-1])

# 0 is inclusive but not 2, so only 0 and 1 will be considered
# 2 is exclusive
print(courses[0:2])

# print(courses[0:2]) same as print(courses[:2])
print(courses[:2])

# print(courses[2:3]) same as print(courses[2:])
print(courses[2:4])
print(courses[2:])

# calling something out of index gives SyntaxError(invalid syntax)
# print(courses(2:5))

# methods with lists
courses.append('Art')
print(courses)

# append at specific location
courses.insert(0, 'Education')
print(courses)

courses_2 = ['Art_Hist', 'Education_Academy']

# adding lists within lists
courses.insert(0, courses_2)
print(courses)

# printing first item course[0]
print(courses[0])

# popping out first element
courses.remove(['Art_Hist', 'Education_Academy'])

# instead of appending the entire lists, we can extend lists too. insert will insert the second list inside the first list but extend will insert the data to existing list
courses.extend(courses_2)
print(courses)

# removing things from lists - last element
# pop() remove last element, popped will store the removed items and can be displayed to check the last time removed from the list
popped = courses.pop()
print(popped)
print(courses)

# sorting in alphabetical order
num = [1, 5, 2, 4, 3]
courses.sort()
print(courses)
num.sort()
print(num)

# reversing the list
courses.reverse()
print(courses)
courses.sort(reverse=True)
num.sort(reverse=True)
print(courses)
print(num)

print(min(num))
print(max(num))
print(sum(num))

# find index of list
print(courses.index('CompSci'))

# print if true / false if the element is found in the list
print('Math' in courses)
print('Arts' in courses)

# print each item in the courses, can use any keyword instead of item
print(courses)
for item in courses:
    print(item)

for course in courses:
    print(course)

# to also have index to each element
for index, course in enumerate(courses):
    print(index, course)

# if don't want to have index 0, we can start with 1
for index, course in enumerate(courses, start=1):
    print(index, course)

# converting list to string
print(courses)
course_str = ', '.join(courses)
print(course_str)

# converting string to list, here ', ' is identifying each element to be added to the list
new_list = course_str.split(', ')
print(new_list)
