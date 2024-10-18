import random
import utils
import time


def generate_sequence(difficult):

    genlist = list()
    while len(genlist) < difficult:
        genlist.append(random.randint(1, 101))
    print(genlist)
    time.sleep(difficult)
    utils.screen_cleaner()
    return genlist


def get_list_from_user(difficult):

    userlist = list()
    while len(userlist) <= difficult-1:
        checkk = (input('Please enter a number from 1 to 101: '))
        if checkk.isdigit():
            checkk = int(checkk)
            userlist.append(checkk)
            if checkk not in range(1, 101):
                print('\nInput number within provided range only.')
        else:
            print('\nNumbers only accepted.')

    return userlist


def is_list_equal(genlist, userlist):

    genlist.sort()
    userlist.sort()
    return True if genlist == userlist  else False


def play(difficult):

    return True if is_list_equal(generate_sequence(difficult), get_list_from_user(difficult)) == True else False
