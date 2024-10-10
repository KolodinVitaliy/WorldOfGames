import random


def generate_number():

    global difficult
    secret_number = random.randint(0, difficult)
    return secret_number

def get_guess_from_user():

    global difficult
    global user_input
    user_input = input(f'Please enter number from 0 to {difficult}')
    return user_input

def compare_results():

    global difficult
    global user_input

    if difficult == user_input:
        return 1
    else:
        return 0

def play():