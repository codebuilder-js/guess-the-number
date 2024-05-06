import random

randomNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20...')

for guesses in range(1, 7):
    guess = int(input('Take a guess: '))

    if guess < randomNumber:
        print('Your guess is too low...')
    elif guess > randomNumber:
        print('Your guess is too high...')
    else:
        break

if guess == randomNumber:
    print('Good job! You guessed my number in ' + str(guesses) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(randomNumber) + '.')
