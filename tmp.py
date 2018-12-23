# Random number guessing game
import random

# generate a random number between 1 and 10
secret_num = random.randint(1, 10)
for i in range(1, 6):
    # get a number guess from the user
    guess = int(input("Guess a number between 1 and 10: "))
    # compare guess to secret number
    if guess == secret_num:
        print("You got it!!!, My number was {}.".format(secret_num))
        break
    else:
        # print hit/miss
        print("Thatz not it, sorry. Try again: ")
print("Sorry, you have exceeded the maximum number for tries for the day")
