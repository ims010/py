# Random number guessing game


# import random

# # generate a arandom number between 1 and 10
# secret_num = random.randint(1, 10)
# while True:
#     # get a number guess from the user
#     guess = int(input("Guess a number between 1 and 10: "))
#     # compare guess to secret number
#     if guess == secret_num:
#         print("You got it!!!, My number was {}.".format(secret_num))
#         break
#     else:
#         # print hit/miss
#         print("Thatz not it, sorry. Try again: ")

# -----------EXTENDED-1--------------------

# import random

# # generate a arandom number between 1 and 10
# secret_num = random.randint(1, 10)
# for i in range(1, 6):
#     # get a number guess from the user
#     guess = int(input("Guess a number between 1 and 10: "))
#     # compare guess to secret number
#     if guess == secret_num:
#         print("You got it!!!, My number was {}.".format(secret_num))
#         break
#     else:
#         # print hit/miss
#         print("Thatz not it, sorry. Try again: ")
# print("Sorry, you have exceeded the maximum number for tries for the day")


# -----------EXTENDED-2-------------------


# Limit the number of guesses
# Catch when someone submits a non-integer
# Print "Too High" or "Too Low" message for bad gusses


# secret_num = random.randint(1, 10)
# for i in range(1, 6):
#     # get a number guess from the user

#     guess = input("Guess a number between 1 and 10: ")
#     if type.(guess) == int:
#         # compare guess to secret number
#         if guess == secret_num:
#             print("You got it!!!, My number was {}.".format(secret_num))
#             break
#         else:
#             # print hit/miss
#             print("Thatz not it, sorry. Try again: ")
#     else:
#         print("Ohh, that's not an integer. Try again: ")
# print("Sorry, you have exceeded the maximum number for tries for the day")


# -------------TRIES-----------------------------------------

# import random
# secret_num = random.randint(1, 10)
# for i in range(1, 6):
#     guess = int(input("Guess a number between 1 and 10: "))
#     if guess == secret_num:
#         print("You got it!!!, My number was {}.".format(secret_num))
#         break
#     else:
#         print("Thatz not it, sorry. Try again: ")
# print("Sorry, you have exceeded the maximum number for tries for the day")


# guess = int(input("Guess a number between 1 and 10: "))
# if guess > secret_num:
#     print("Too HIGH")
# else:
#     print("Too LOW")

#-----------------------FINAL--------------------------------

import random

# safely make an int
# limit guesses
# too high message
# too low message
# play again


def game():
    # generate a arandom number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []
    while len(guesses) < 5:
        try:
            # get a number guess from the user
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print("You got it!!!, My number was {}.".format(secret_num))
                break
            elif guess < secret_num:
                print("My Number is higher than {}".format(guess))
            else:
                # print hit/miss
                print("My Number is lower than {}".format(guess))
            guesses.append(guess)
    else:
        print("You didn't get it! My Number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye")


game()
