import requests
import random
import utils


def get_money_interval():

    url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_f4bn008eyEzrOa5IE1gD5pOe6Gi3tGrZFP0152go'
    response = requests.get(url, params={'base_currency': 'USD', 'currencies': 'ILS'})

    data = response.json()
    usd_to_ils = data['data']['ILS']

    return usd_to_ils

def get_guess_from_user(amount, usd_to_ils):

    user_input = None

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

def play(difficult):

    utils.screen_cleaner()
    usd_to_ils = get_money_interval()
    amount = random.randint(1, 100)
    amount_in_ils = amount * usd_to_ils
    acceptable_range = 10 - difficult
    max_good = amount_in_ils + acceptable_range
    min_good = amount_in_ils - acceptable_range

    if max_good > get_guess_from_user(amount, usd_to_ils) > min_good:
        print('You good you!')
        return True
    else:
        print('Calculate better next time')
        return False
