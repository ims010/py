import modules
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']
index = modules.find_index(courses, 'Math')
print(index)

# import modules as alias
import modules as mm

courses = ['History', 'Math', 'Physics', 'CompSci']
index = mm.find_index(courses, 'Math')
print(index)

# only find_index function
from modules import find_index

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(index)

# importing mutiple functions
from modules import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(index)
print(test)

# can be done in this way also
from modules import *

courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(index)
print(test)
print(sys.path)

# the module function is first checked in the same directory, path variable dir, standard lib dir, sites packages dir
# if the module is in different dir, then we can import it by sys.path.append('/Whateverpaththemoduleis') or add it to the path variable

import random
random_course = random.choice(courses)
print(random_course)

import math
import datetime
import calendar

today = datetime.date.today()
print(today)

import os
print(os.getcwd())
