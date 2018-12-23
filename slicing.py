my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# positive  0  1  2  3  4  5  6  7  8  9
#negative -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(my_list)

# list[start:end:step]
# end is non inclusive
print(my_list[0:5])

# with step =2
print(my_list[0:5:2])

# printing same with positive and negative
print(my_list[3:8])
print(my_list[-7:-2])

# using both positive and negative
print(my_list[1:-2])

# print all elements in the list
# end and step are optional
print(my_list[0:])

# negative step
print(my_list[2:-1:-1])
print(my_list[-1:2:-1])
print(my_list[-1:2:-2])

# entire list reversed
print(my_list[::-1])

# slicing strings
sample_url = 'http://coreyms.com'
print(sample_url)

# reverse url
print(sample_url[::-1])

# get top level domain
print(sample_url[-4:])

# print the url without the http://
print(sample_url[7:])

# print the url without the http:// and the top level domain
print(sample_url[7:-4])
