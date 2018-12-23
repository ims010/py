# lists are defined in []
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

# 0 is inclusive but not 2
# 2 is exclusive
print(courses[0:2])

# print(courses[0:2]) same as print(courses[:2])
print(courses[:2])

# print(courses[2:3]) same as print(courses[2:])
print(courses[2:4])
print(courses[2:])

# calling something out of index gives syntax error(invalid syntax)
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

# print if true / flase if the element is found in the list
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

# Tuples are similar to list but we can't modify the tuples
# mutable = can be modified(lists) and immutable = can't be modified(tuples)

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

# cahnging a value in the list_1, also changed list_2
list_1[0] = 'Art'
print(list_1)
print(list_2)

# if we don't need a list to be modified then we use tuples, tuples uses -> () brackets
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# chaning a value in tuple gives errpr as tuple object doesnot support
# need to modify => use lists
# if just need to loop through and access => use tuples

# Sets - unorders and no duplicates, don't care about order, everytimes chanhes the order while printing
# sets uses -> {} brackets

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)


# adding a duplicate value, CompSci
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'CompSci'}
print(cs_courses)

# to find common elements in 2 different sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Arts', 'Design'}
print(cs_courses.intersection(art_courses))

# to find different elements in sets
print(cs_courses.difference(art_courses))

# combines both the sets
print(cs_courses.union(art_courses))

# creating empty lists, tuples and sets
empty_list = []
empty_list = list()  # method to call empty list

empty_tuple = ()
empty_tuple = tuple()  # method to call empty tuple

empty_set = {}  # this is dictinoary
empty_set = set()  # method to call empty set
