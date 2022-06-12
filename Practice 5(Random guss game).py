#from ntpath import join
import random

random_numbers = random.randint(0, 9)

guess_number =  0
guess_limit = 3
while guess_number < guess_limit:
    int_convert = ' % s'%(random_numbers)
    secret_number = int(int_convert)
    guess = int(input(f'Guess a number between 1 to 10  >> '))
    guess_number += 1
#    print (guess == secret_number)
    if guess == secret_number:
        
        print('You win!')
        break
else:
    print(f'You Fail {secret_number}')
#    break

