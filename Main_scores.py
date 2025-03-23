from flask import Flask, render_template_string
from utils import SCORES_FILE_NAME
import ast

app = Flask(__name__)

error_template = """
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1><div id="score" style="color:red">ERROR</div></h1>
    </body>
</html>
"""

html_template = """
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>The scores is: </h1>
        {% for score in scores %}
        <p>{{score}}</p>
        {% endfor %}
    </body>
</html>
"""

@app.route('/')
def score_server():
    with open(SCORES_FILE_NAME, "r") as score_file:
        current_score = score_file.read()
        list_of_lists = ast.literal_eval(current_score)
    if current_score is None:
        return render_template_string(error_template)
    return render_template_string(html_template, scores=list_of_lists)

if __name__ == '__main__':
    app.run()

score_server()