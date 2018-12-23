# Generate don't hold the result in memory, they yeild one result at a time

# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i * i)
#     return result

# my_nums = square_numbers([1, 2, 3, 4, 5])
# # my_nums = [x *x for x in [1, 2, 3, 4, 5]]

# print my_nums

# # for num in my_nums:
# #     print num

# # Instead of storing the result in an empty list, we can use yield method of calculate a result in realtime and display the output, yield don't store any result


def square_numbers(nums):
    for i in nums:
        yield(i * i)


my_nums = square_numbers([1, 2, 3, 4, 5])
# my_nums = (x *x for x in [1, 2, 3, 4, 5])

# print next(my_nums)
# print next(my_nums)
# print next(my_nums)
# print next(my_nums)
# print next(my_nums)
# # print next(my_nums) # Printing out of iteration in will thrown StopIteration error

# print list(my_nums) # to store the values as a list instead of printing out
for num in my_nums:
    print(num)


# import mem_profile
# import random
# import time

# names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
# majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# print 'Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil())


# def people_list(num_people):
#     result = []
#     for i in xrange(num_people):
#         person = {
#             'id': i,
#             'name': random.choice(names),
#             'major': random.choice(majors)
#         }
#         result.append(person)
#     return result


# def people_generator(num_people):
#     for i in xrange(num_people):
#         person = {
#             'id': i,
#             'name': random.choice(names),
#             'major': random.choice(majors)
#         }
#         yield person


# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

# # t1 = time.clock()
# # people = people_generator(1000000)
# # t2 = time.clock()

# print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
# print 'Took {} Seconds'.format(t2 - t1)
