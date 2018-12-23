# loops
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# break
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

# continue
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

# loop in loop
for num in nums:
    for letter in 'abc':
        print(num, letter)

# range - for certain number of times
for i in range(10):
    print(i)

# starting at a certian start point
for i in range(1, 10):
    print(i)

# while loops - will go through until the condition is met or hit break
# while loops will go into infinite loops if the value isn't incremented
x = 0
while x < 10:
    print(x)
    x += 1

# breaking a inifinite loop, always use break
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
