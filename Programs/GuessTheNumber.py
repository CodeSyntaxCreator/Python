import random;

def guess(para1,para2):
    random_number = random.randint(para1, para2)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between {para1} and {para2}:  '))
        print(guess)
        if guess < random_number:
            print('Guess again. Too low.')
        elif guess > random_number:  
              print('Guess again. Too high.')
    print(f'Congratsm you guessed it, it was {random_number}')          
guess(1,10)
