import random
from time import sleep
from utils import screen_cleaner


def generate_sequence(difficult):

    generated_list = list()
    while len(generated_list) < difficult:
        generated_list.append(random.randint(1, 100))
    print(generated_list, end="")
    sleep(difficult/2)
    print(" " * len(generated_list), end="")
    return generated_list


def get_list_from_user(difficult):

    user_list = list()
    while len(user_list) <= difficult-1:
        check = (input('Please enter a number from 1 to 100: '))
        if check.isdigit():
            check = int(check)
            user_list.append(check)
            if check not in range(1, 101):
                print('\nInput number within provided range only.')
        else:
            print('\nNumbers only accepted.')

    return user_list


def play(difficult):
    print(f"Randomly generated sequence per chosen by you difficulty level \n will appear on screen for {difficult} seconds and then disappear. \nYou have to catch the sequence and enter it latter.")
    print('Get prepared!')
    sleep(3)
    print('3..')
    sleep(1)
    print('2..')
    sleep(1)
    print('1..')
    sleep(1)
    if generate_sequence(difficult) == get_list_from_user(difficult):
        print('You god dam right!')
        return True
    else:
        print('Bad memory. Continue to train!')
        return False

