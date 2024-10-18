def welcome():

    username = ' '
    are_you_sure = None
    while not username or username.isspace() or not are_you_sure == 'Y':
        username = input('Please enter your username: ')
        if not username:
            print('\nUsername can not be empty.')
        elif username.isspace():
            print('\nUsername can not be only spaces.')
        else:
            are_you_sure = input(f'\nAre you sure you want to choose {username} as your username? \n[Y/N]: ').upper()
    return print(f'Hi ' + username + ' and welcome to the World of Games: The Epic Journey')


def start_play():

    global game
    game = None
    while game not in range(1,4):
        game = input("""\n Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS.
    Your choose: """)
        if game.isdigit():
            game = int(game)
            if game not in range(1,4):
                print('\nInput digit within provided range only.')
        else:
            print('\nDigits only accepted.')

    global difficult
    difficult = None
    while not difficult in range(1,6):
        difficult = input("""\n Please choose the difficulty level between 1 and 5,
    where 1 is easiest and 5 is hardest: """)
        if difficult.isdigit():
            difficult = int(difficult)
            if difficult not in range(1,6):
                print('\nInput digit within provided range only.')
        else:
            print('\nDigits only accepted.')

    result = [[' ','Memory Game','Guess Game','Currency Roulette'],[' ','first','second','third','fourth','fifth']]
    print(f"""\n You have chosen {str(result[0][game])}, 
    with {str(result[1][difficult])} level of difficulty.
    \n Let the Game begin!""")
    if game == 1:
        import memory_game
        memory_game.play(difficult)
    elif game == 2:
        import guess_game
        guess_game.play(difficult)
    elif game == 3:
        import currency_roulette_game
        currency_roulette_game.play(difficult)
    return difficult