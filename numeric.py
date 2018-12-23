# integer - whole number
# float - decimal
# addition -> a + b
# subtraction -> a - b
# multiplication -> a * b
# division -> a / b
# floor division -> a // b (ignores decimal value)
# exponent -> a ** b
# modulus -> a % b

# incrementing:
num = num + 1
num += 1

# abs - absolute
print(abs(-3))
print(round(3.75))
print(round(3.75, 1)) => round to first digit

# comparsion(returns boolean value):
# equal -> a == b
# not equal -> a != b
# greater than -> a > b
# lesser than -> a < b
# greater or equal -> a >= b
# less or equal -> a <= b

# casting:
# before casting
num_1 = "100"
num_2 = "200"
print(num_1 + num_2)

# after casting
num_1 = int("100")
num_2 = int("200")
print(num_1 + num_2)