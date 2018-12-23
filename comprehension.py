nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# n for each n in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# list comparhension
my_list = [n for n in nums]
print(my_list)

# n*n for each n in nums
my_list = []
for n in nums:
    my_list.append(n * n)
print(my_list)

# list comparhension
my_list = [n * n for n in nums]
print(my_list)

# doing the same in map + lambda
my_list = map(lambda n: n * n, nums)
print(my_list)

# n for each n in nums if n is even
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

# list comprahension
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# using a filter + lambda
my_list = filter(lambda n: n % 2 == 0, nums)
print(my_list)

# letter+num pair for each in abcd and eachnumber in 0123
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

# list comprahension
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# dictionary comprehension
# print(zip(names, heros)) - builtin function zip
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

# dictionary comprehension
my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

# adding some restrictions, don't want Peter
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)

# set comprehension, set is like lists but all unique values
nums = [1, 1, 2, 1, 3, 4, 5, 4, 5, 5, 6, 7, 8, 9, 7, 8, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}
print(my_set)

# Generator expressions
# yeild n*n for each n in nums

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen = gen_func(nums)
for i in my_gen:
    print(i)

# comprehension
my_gen = (n * n for n in nums)
for i in my_gen:
    print(i)
