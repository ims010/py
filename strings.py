message = "Hello World!"

# to print length len()
print(len(message))

# to access the variable with the index
# index starts from 0, always
print(message[0])

# to access the substring, here 0 is inclusive and 5 is exclusive
print(message[0:5])

# if nothing specified, defaulty taken as 0
print(message[:9])

# Upper case to lower case
print(message.upper())
print(message.lower())

# Count the number for time the characters is there
print(message.count("Hello"))

# prints start index if character/word is found
print(message.find("World"))

# if nothing found, returns -1
print(message.find("World"))

# replacing a word
message = message.replace('world', 'Universe')
print(message)

greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name
print(message)

# instead of messy code, as above
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# fstrings - string formatting as simple as possible
greeting = 'Hello'
name = 'Michael'
message = f'{greeting}, {name}. Welcome!'
print(message)

greeting = 'Hello'
name = 'Michael'
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# more information on any method
# different than print(help(str))
# print(dir(name))
