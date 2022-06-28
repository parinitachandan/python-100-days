import requests
import smtplib
from flight_details import FlightSearch
from flight_data_manager import DataManager
from user_input import UserInput
from datetime import datetime, timedelta
import os


ORIGIN_CITY_IATA = "LON"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/0bf16380c49a0a78078f51a43e59a088/flightDeals/users"
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
SHEETY_AUTH_KEY = os.getenv("SHEETY_AUTH_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_EMAIL_PASSWORD = "iskjxrsmcxdapljo"

UserInput

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

# timedelta() - generally used for calculating differences in dates and also can be used for date manipulations
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination_code in destinations:
    flight_search = FlightSearch()
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today

    )

flight_search = FlightSearch()
if flight is None:
    pass
if flight.price < destinations[destination_code]["price"]:
    response = requests.get(url=SHEETY_USER_ENDPOINT, headers={"Authorization": "Basic " + SHEETY_AUTH_KEY})
    data = response.json()
    users = data['users']
    print(users)
    emails = [row["email"] for row in users]
    names = [row["firstName"] for row in users]
    message = f"Low alert price!Only{flight.price} to fly from {flight.origin_city} to {flight.destination_city}" \
              f"from {flight.out_date} to {flight.return_date}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # securing connection and TLS - Transport Layout Security
        subject = "Great Flight Deals Club"
        connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=emails,
                            msg=f"Subject: {subject}\n\n"
                                f"{message}")
else:
    response = requests.get(url=SHEETY_USER_ENDPOINT, headers={"Authorization": "Basic " + SHEETY_AUTH_KEY})
    data = response.json()
    users = data['users']
    print(users)
    emails = [row["email"] for row in users]
    names = [row["firstName"] for row in users]
    message = f"Sorry couldn't find flight in your mentioned budget."

    subject = "Great Flight Deals Club"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # securing connection and TLS - Transport Layout Security

        connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=emails,
                            msg=f"Subject: {subject}\n\n"
                                f"{message}")




