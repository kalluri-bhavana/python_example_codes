#this is a guess the number game

import random

secretnumber=random.randint(1,20)

print('I am thinking of a number between 1 and 20')

#ask the player to guess 6 times
for guessestaken in range(1,7):
    print('take a guess')
    guess=int(input())

    if guess<secretnumber:
        print('your guess is too low')
    elif guess>secretnumber:
        print('your guess is too high')
    else:
        break #this condition is correct guess

if guess==secretnumber:
    print('good job! you guessed my number in '+str(guessestaken) +' guesses!')
else:
    print('nope. the number i was thinking of was'+str(secretnumber))

