from flask import Flask

app = Flask(__name__)


@app.route("/")   # home page when there is a forward slash
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def bye():
    return "Bye"


app.run()
