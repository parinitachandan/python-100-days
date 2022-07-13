from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(0, 10)
    current_year = datetime.now().strftime("%Y")
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    gender_url = requests.get(f"https://api.genderize.io?name={name}")
    gender_response = gender_url.json()
    gender = gender_response["gender"]

    age_url = requests.get(f"https://api.agify.io?name={name}")
    age_response = age_url.json()
    age = age_response["age"]

    return render_template("guess.html", person_name=name, person_gender=gender, person_age=age)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


app.run(debug=True)



