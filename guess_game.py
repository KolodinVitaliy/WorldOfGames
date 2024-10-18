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


def compare_results(secret_number, user_input):

    return True if secret_number == user_input else False


def play(difficult):

    utils.screen_cleaner()
    return print(True) if compare_results(generate_number(difficult), get_guess_from_user(difficult)) == True else print(False)
