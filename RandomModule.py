# Using Random Module to generate random number, this module shouldn't be used for the random number generation in security purposes or cryptography but Python suggest to use the Secrets Module

import random

print(dir(random))

# Random and Uniform methods
# Random generates a random number between 0 and 1, 0 is inclusive and 1 is non-inclusive, a floating-point value and it won't any arguments/range.
value = random.random()
print(value)
value = random.uniform(1, 10)  # Random valuse between a specific range, a floating-point random number is generated
print(value)
value = random.randint(1, 6)  # Genrates a whole number between a specific range
print(value)
value = random.randint(0, 1)
print(value)

greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)  # choice() picks a random value from a list of values
print(value + ', Nick!')

colors = ['Red', 'Black', 'Green']
results = random.choices(colors, k=10)  # choices() picks multiple random values from a list, k is just like how many time we want to pick, can be any value.
print(results)

colors = ['Red', 'Black', 'Green']
results = random.choices(colors, weights=[18, 18, 2], k=10)  # Limiting a certain color in random generating, also providing a weightage/probability, total adds up, like 18+18+2. So Red has 18 out of 38 changes.
print(results)

# Randomly shuffle a list of values
deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)

hand = random.sample(deck, k=5)  # Sample is different from choices and shuffle, choices will pick multiple same value but sample will always picks a unique value from the list
print(hand)
