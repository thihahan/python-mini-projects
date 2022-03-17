from random import *

def guess(x):
    random_number = randint(1, x)
    guess_number = 0
    while guess_number != random_number:
        guess_number = input(f'Guess a number between 1 and {x}: ')
        while not guess_number.isnumeric():
            guess_number = input('enter only number')
        guess_number = int(guess_number)
        if guess_number > random_number:
            print("try again. Too high")
        elif guess_number < random_number:
            print("try again. Too low")

    print("success. congratulations...")

def computer_guess(y):
    computer_guess_number = randint(1, y)
    check = input(f'is {computer_guess_number} low(l), high(h), correct(c): ')
    while check != 'c':
        if check == 'l':
            computer_guess_number += randint(10, 40)
        elif check == 'h':
            computer_guess_number -= randint(10, 40)
        check = input(f'is {computer_guess_number} is low(l), high(h), correct(c): ')
    print("Congrats")


x = input('how many do you want to guess: ')
while not x.isnumeric():
    x = input('enter only number: ')
x = int(x)


if __name__ == '__main__':
    #guess(x)
    computer_guess(20)

