#import random module
import random

#set random number that needs to be guessed
#random number is between 0 and 20
randNum = random.randint(0, 20);

#print game rules
print("Welcome to the random number guessing game!\n")
print("Guess a number between 0 and 20: ")

#get user input, typecast it to int
guess = int(input())

#empty line for spacing
print()

#start a guess count
count = 0

while guess != randNum:
    if guess > randNum:
        print("You guessed too high, guess again: ")
        guess = int(input())
    else:
        print("You guessed too low, guess again: ")
        guess = int(input())

    count += 1

    #empty line for spacing
    print()

#player guessed correctly
print("You guessed right!\n")
print("It took you", count, "guesses!")

