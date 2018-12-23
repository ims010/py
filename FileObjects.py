# File Objects

# Opening a file in the same dir but not a good idea to open in this way, if the file is in other dir, need to provide the complete path
# Reading, Writing, Appending, Reading & Writing. If nothing specified, it defaults to Reading
# r - reading
# w - writing
# a - appeding
# r+ - reading & writing
f = open('text.txt', 'r')
print(f.name)
print(f.mode)  # to know in what mode we have opened the file
f.close()  # After opening, we need to explicitly close the file

# Opening a file using context manager, recommended way. f.close() are not required in here and we work with the file within the block of code, as we exit the code block, the file is closed automatically. It also catches all exceptions

# Calling the file outside the contect manager will throw ValueError, we have to be in the code block to access the file
with open('text.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

# Reads each line of the file side by side
with open('text.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

# Gets the first line of the file but executing multiple time will gets the next line in the file.
with open('text.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)

    f_contents = f.readline()
    print(f_contents)

    f_contents = f.readline()
    print(f_contents)

    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')

# Rather than open in this wau we can iterate over them, this also uses less memory and more efficient, getting one line at a time
with open('text.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Reading only required number of lines(characters):
with open('text.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents)

    # calling again will start from the last left position and reads next 100 characters
    f_contents = f.read(100)
    print(f_contents)
    # As we reach end of the file, the read just reads the empty string, nothing is displayed

# Using loops to read the small chunks of the file
with open('text.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='*')  # adding * to identify the 100 characters, optional
        f_contents = f.read(size_to_read)

# Using seek() to read contents
with open('text.txt', 'r') as f:
    size_to_read = 20
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents, end='')


# Writing into files
# Opening file in read mode and try to write

# with open('text.txt', 'r') as f:
#     f.write('Test') # Throws - io.UnsupportedOperation: not writable error

# Writing to a new file, if the file already exists, Python will over-write the file, using 'a' will append to the existing file if it already exists
with open('text2.txt', 'w') as f:
    f.write('Test')
    f.write('Test2')  # Executing 2 times will write to the last left position

with open('text3.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('Test2')  # Seek over-write the first position and starts from begining everytime.

# Writing a file content to a new file
with open('text.txt', 'r') as rf:
    with open('text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('text.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

# # Copying a picture file
# with open('bronx.jpg', 'r') as rf:
#     with open('bronx_copy.jpg', 'w') as wf:
#         for line in rf:
#             wf.write(line) # This will throw and error as writing a text file is not similar to picture file. Picture file required to open the file in binary format.


# # Copying a picture file in binary format
# with open('bronx.jpg', 'rb') as rf:
#     with open('bronx_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# # Writing to a binary file in small chunks
# with open('bronx.jpg', 'rb') as rf:
#     with open('bronx_copy.jpg', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)
