import os
import requests
from datetime import datetime

NUTRITION_ID = os.getenv("NUTRITION_ID")
NUTRITION_API = os.getenv("NUTRITION_API")

SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")


EXERCISE = input("Tell me which exercises you did: ")
GENDER = "Female"
WEIGHT = 44.15
HEIGHT = 154
AGE = 16

exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/0bf16380c49a0a78078f51a43e59a088/workoutTracker/workouts"

exercise_headers = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_API
}

exercise_params = {
    "query": EXERCISE,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
result = response.json()
print(result)

today = datetime.now().strftime("%d/%m/%y")  # date,month,year
time = datetime.now().strftime("%X")  # time

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_endpoint,
                                    json=sheet_inputs,
                                    auth=(SHEETY_USERNAME,
                                          SHEETY_PASSWORD))
    print(sheety_response.text)

