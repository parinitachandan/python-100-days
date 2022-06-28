from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
import os
from twilio.rest import Client

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUM = os.getenv("TWILIO_NUM")
MY_NUM = os.getenv("MY_NUM")

ORIGIN_CITY_IATA = "LON"

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
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
        body=f"Low alert price!Only{flight.price} to fly from {flight.origin_city} to {flight.destination_city}"
             f"from {flight.out_date} to {flight.return_date}",
        from_=TWILIO_NUM,
        to=MY_NUM
    )

else:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
        body=f"Sorry couldn't find flight in your mentioned budget.",
        from_=TWILIO_NUM,
        to=MY_NUM
    )
