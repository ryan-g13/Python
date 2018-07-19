# Guess a number game
# import the random module for random number generation
import random

print('Hello, what is your name user?')
userName = input()

print('I am thinking of a number between 1 and 20, ' + userName + ', can you guess it in 6 guesses?')
targetNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Please take a guess.')
    currentGuess = int(input())

    if currentGuess < targetNumber:
        print('Your guess is too low.')
    elif currentGuess > targetNumber:
        print('Your guess is too dang high')
    else:
        break

if currentGuess == targetNumber:
    print('You have guessed correctly in ' + str(guessesTaken) + ' guesses, ' + userName +'!')
else:
    print('You ran out of guesses ' + userName + '. The number that I was thinking of was ' + str(targetNumber))