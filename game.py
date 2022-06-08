"""A number-guessing game."""

import random

# greet player
print("Welcome, what's your name?")

# get player name
name = input("Type up your name: ")

# choose random number between 1 and 100
rnum = random.randrange(0, 100, 1)

print(name + ", I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

count = 0
# repeat forever:
while True:
#     get guess
    try:
        guess = int(input("Your guess? "))
        count += 1
    #     if guess is incorrect:
    #         give hint
    #         increase number of guesses
        if guess > 100 or guess < 1:
            print("Number must be between 1 and 100")
        elif guess > rnum:
            print("Your guess is too high, try again.")
        elif guess < rnum:
            print("Your guess is too low, try again.")
#     else:
#         congratulate player
        elif guess == rnum:
            print("Well done, " + name + "! You found my number in " + str(count) + " tries!")
            break
    except:
        print("Input a valid number as a guess and try again.")
