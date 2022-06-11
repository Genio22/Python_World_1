from ntpath import join
import random

random_numbers = random.randint(0, 10)
secret_number = '>> % s'%(random_numbers)
guess_number =  0
guess_limit = 3
while guess_number < guess_limit:
    guess = int(input(f'Guess a number between 1 to 10 >> '))
    guess_number += 1
    if guess == secret_number:
        print('You win!')
    else:
        print(f'You Fail {secret_number}')
        break

