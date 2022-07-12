from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def website():
    return render_template("parinita.html")


@app.route("/index")
def index():
    return render_template("index.html")

app.run(debug=True)

