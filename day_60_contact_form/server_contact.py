from flask import Flask, render_template, request
import os
import smtplib

from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

EMAIL = os.getenv("EMAIL")
PASSWORD = "ekuaowwuijsxttre"


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("index.html", msg_sent=True)
    return render_template("index.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\n" \
                    f"Name: {name}\n" \
                    f"Email: {email}\n" \
                    f"Phone: {phone}\n" \
                    f"Message:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="me@parinita.me",
                            msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)

