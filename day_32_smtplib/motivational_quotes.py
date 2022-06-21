import datetime as dt
import random
import smtplib

my_email = "pcparinita@gmail.com"
password = ""
now = dt.datetime.now()

day = now.weekday()
if day == now.weekday():
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # securing connection and TLS - Transport Layout Security

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="me@parinita.me",
                            msg=f"Subject:Motivation\n\n{quote}")



