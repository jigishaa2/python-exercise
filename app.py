
#created APIs based on REST(protocol that tells API how to behave) using Flask

from flask import Flask

# app = Flask(__name__) # __name__ will take the file name
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# @app.route("/jigi")
# def print_jigi():
#     return "Jigii"





from random import randint

app = Flask(__name__)

@app.route("/random")
def random():
    return(str(randint(1,20)))





