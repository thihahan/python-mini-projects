from random import *

def game():
    player = input("What's your choice? 'r' for rock, 'p' for 'paper', 's' for scissors: ")
    computer = choice(['r', 'p', 's'])
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        print("You won!")
    # elif player == 's' and computer == 'p':
    #     print("You won!")
    # elif player == 'p' and computer == 'r':
    #     print("You won!")
    elif player == computer:
        print("Draw")
    else:
        print('You lose!')
    print(f"player: {player} and computer: {computer}")

if __name__ == '__main__':
    again = True
    while again:
        game()
        again = input("do you try again? 'y' for Yes, 'n' for No: ")
        if again == 'y':
            again = True
        elif again == 'n':
            again = False