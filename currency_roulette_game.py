import requests
import random

import utils


def get_money_interval(difficult):

    global amount
    global max_good
    global min_good
    global usd_to_ils

    url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_f4bn008eyEzrOa5IE1gD5pOe6Gi3tGrZFP0152go'
    response = requests.get(url, params={'base_currency': 'USD', 'currencies': 'ILS'})

    data = response.json()
    usd_to_ils = data['data']['ILS']


    amount = random.randint(1, 100)
    amount_in_ils = amount * usd_to_ils
    acceptable_range = 10 - difficult
    max_good = amount_in_ils + acceptable_range
    min_good = amount_in_ils - acceptable_range

    return amount, max_good, min_good, usd_to_ils

def get_guess_from_user(amount, usd_to_ils):

    global user_input
    user_input = True
    while type(user_input) != int and type(user_input) != float:
        user_input = input(f'Please enter amount of {amount} USD in ILS, if rates are {usd_to_ils} ILS to 1 USD: ')
        if user_input.isdigit():
            user_input = int(user_input)
        elif "." in user_input:
            user_input_dot = user_input
            user_input_dot_remove = user_input_dot.replace(".", "")
            if user_input_dot_remove.isdigit():
                user_input = float(user_input)
        elif "." in user_input:
            user_input_dot = user_input
            user_input_dot_remove = user_input_dot.replace(",", "")
            if user_input_dot_remove.isdigit():
                user_input = float(user_input)
        else:
            print('\nDigits only accepted.')
    return user_input

def compare_results(max_good, min_good, user_input):
    if min_good < user_input < max_good:
        return True
    else:
        return False

def play(difficult):

    utils.screen_cleaner()
    get_money_interval(difficult)
    get_guess_from_user(amount, usd_to_ils)
    return True if compare_results(max_good, min_good, user_input) == True else False
