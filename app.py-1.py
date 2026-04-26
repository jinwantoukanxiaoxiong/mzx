import os 
from flask import   Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello World!</h1>"


@app.route("/<name>")
def hello():
    return "Hello,how are you doing?"


if __name__ == "__main__":
    app.run
            
