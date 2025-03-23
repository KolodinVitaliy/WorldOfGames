import random

import utils


def generate_number(difficult):

    secret_number = random.randint(0, difficult)
    return secret_number


def get_guess_from_user(difficult):

    user_input = None
    while user_input not in range(0, difficult+1):
        user_input = input(f'Please enter number from 0 to {difficult}: ')
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input not in range(0, difficult+1):
                print('\nInput digit within provided range only.')
        else:
            print('\nDigits only accepted.')
    return user_input

def play(difficult):
    utils.screen_cleaner()
    print(f'In this game you have to guess number between 0 and {difficult} \nGood Luck!')
    if generate_number(difficult) == get_guess_from_user(difficult):
        print('Right guess. Congratulations!')
        return True
    else:
        print('Bad guess. Try better next time.')
        return False