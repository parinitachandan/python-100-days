import requests
import smtplib



my_email = "pcparinita@gmail.com"
password = ('')

MY_LAT = 12.971599
MY_LONG = 77.594566


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Checking if the  latitude is inbetween MY_LAT-5 and MY_LAT+5
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()

            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="me@parinita.me",
                                msg="Subject:ISS Track\n\nThe ISS is above you.")
    else:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="me@parinita.me",
                                msg="Subject:ISS Track\n\n"
                                    "You will receive an email when the ISS is above you.")


iss_overhead()