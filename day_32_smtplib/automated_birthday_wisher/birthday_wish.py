import datetime as dt
import pandas
import random
import smtplib


my_email = "pcparinita@gmail.com"
password = ""

today = dt.datetime.now()
today_date = (today.month, today.day)


data = pandas.read_csv("birthday.csv")
birthday_dict = {(data_row["month"], data_row["day_42_ intermediate_html"]): data_row for (index, data_row) in data.iterrows()}

if today_date in birthday_dict:
    birthday_person = birthday_dict[today_date]
    file_path = f"wish_letters/letter_{random.randint(1, 2)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # securing connection and TLS - Transport Layout Security

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n"
                                f"{contents}")

