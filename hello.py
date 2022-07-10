from flask import Flask

app = Flask(__name__) # __name__ will take the file name

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/jigi")
def print_jigi():
    return "Jigii"
