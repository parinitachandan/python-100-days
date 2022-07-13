from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/MeJgB3yMMwIaHmKD4z/giphy.gif" width="400">'


@app.route("/<name>")
def greet(name):
    return f'<h2>Hello, {name}!</h2>' \
           f'<br>' \
           f'<img src="https://media.giphy.com/media/KiMBUPZUhUg4HRV6PW/giphy.gif" width="400">'


@app.route("/<path:name>/<int:age>")
def info(name, age):
    return f'<p><h2>Name:{name}</h2> </p>' \
           f'<p> <h2>Age:{age}</h2> </p>'


app.run(debug=True)