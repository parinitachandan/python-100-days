import smtplib

my_email = "pcparinita@gmail.com"
password = ""

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()  # securing connection and TLS - Transport Layout Security

    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="me@parinita.me",
                        msg="Subject:Hello\n\nThis is the body of my email")

