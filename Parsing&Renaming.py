# Renaming and re-ordering the files in file system.

import os
oc.chdir(<path>)

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) # Split filename and extension
    # os.path.splitext() gives a tuple which includes the filename and extension(along with '.')
    f_title, f_course, f_num = f_name.split('-') # Spiltting filename as certain point like '-' here and reorders based on available characters in filename
    f_title = f_title.strip() # Stripping off whitespace in f_title
    f_course = f_course.strip() # Stripping off whitespace in f_course
    f_num = f_num.strip()[1:].zfill(2) # Stripping off '#' symbol in f_num strating from 1st position and zfill() pads all the f_num with 0 in the begining, 2 indicates the total padding, padding + f_num.

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext) # Renaming the files in desired format, f_ext already had '.' in it, so didn't mention in the string formatting.
    os.rename(f, new_name) # Calling the rename action through os modules.
