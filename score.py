import app
import memory_game



def add_score():
    if memory_game.play() == True:
        with open('scores.txt', 'a+') as f:
            saved_score = f.read()
            f.write(saved_score + difficult * 3 +5)