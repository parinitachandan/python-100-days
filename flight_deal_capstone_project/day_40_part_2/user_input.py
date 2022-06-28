import requests
import os

SHEETY_USER_ENDPOINT = "https://api.sheety.co/0bf16380c49a0a78078f51a43e59a088/flightDeals/users"
SHEETY_AUTH_KEY = os.getenv("SHEETY_AUTH_KEY")


class UserInput:
    print("Welcome to Great Flight Deals Club.\n"
          "We find the best flight deals and email you.")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email?\n")
    email_recheck = input("Tell me your email again\n")

    while email != email_recheck:
        print("The email you entered first doesn't match with the second one.Please re-enter.")
        email = input("What is your email?\n")
        email_recheck = input("Tell me your email again\n")
    if email == email_recheck:
        print("You're in the club!")

    user_params = {
        'user': {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }}

    response = requests.post(url=SHEETY_USER_ENDPOINT, json=user_params,
                             headers={"Authorization": "Basic " + SHEETY_AUTH_KEY})
    data = response.json()
    print(data)
