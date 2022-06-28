import os
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0bf16380c49a0a78078f51a43e59a088/flightDeals/prices"
SHEETY_AUTH_KEY = os.getenv("SHEETY_AUTH_KEY")
SHEETY_USER_ENDPOINT = "https://api.sheety.co/0bf16380c49a0a78078f51a43e59a088/flightDeals/users"
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers={"Authorization": "Basic " + SHEETY_AUTH_KEY})
        data = response.json()
        # pprint(data) formatted data
        # print(data)
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers={"Authorization": "Basic " + SHEETY_AUTH_KEY},
                json=new_data
            )
            print(response.text)





