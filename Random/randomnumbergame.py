# Code for rng_game.py

import random
numbers = [1, 2, 3, 4, 5, 6]
number_correct = 0

print('This is a game where you attempt to guess a random number')
print('You have ten guesses to guess the correct number three times')

for i in range(10):
    rng = random.choice(numbers)
    guess = int(input('Enter a number from 1-6: '))
    if guess == rng:
        print('Correct')
        number_correct = number_correct + 1
    else:
        print('Incorrect')

if int(number_correct) >= 3:
    print(f'\nYou won the game! You guessed correctly {number_correct} times')
else:
    print(f'\nYou lost the game! You guessed correctly {number_correct} times')
