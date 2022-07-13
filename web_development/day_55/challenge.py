from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return '<img src="https://media.giphy.com/media/KiMBUPZUhUg4HRV6PW/giphy.gif">'


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return '<h1>Bye!</h1>'


app.run()