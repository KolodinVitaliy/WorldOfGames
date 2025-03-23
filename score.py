from utils import SCORES_FILE_NAME
import ast

def add_score(difficult,username):
    points = difficult * 3 + 5

    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            content = file.read()
            list_of_lists = ast.literal_eval(content)
            file.close()
    except (FileNotFoundError, SyntaxError):
        list_of_lists = []

    if not isinstance(list_of_lists, list):
        list_of_lists = []

    found = False
    for sublist in list_of_lists:
        if sublist[0] == username:
            sublist[1] += points
            found = True
            break

    if not found:
        list_of_lists.append([username, points])

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(list_of_lists))
        file.close()

    return list_of_lists
