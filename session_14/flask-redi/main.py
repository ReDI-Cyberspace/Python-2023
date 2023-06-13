from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to my World!</p>"

@app.route("/grades")
def hello_world_():
    return "<p>You did pass you exam</p>"