import requests
from datetime import datetime
import os

GENDER = input("What is your gender? (Key in Male/Female)").capitalize()
WEIGHT_KG = str(input("What is your weight in kg?"))
HEIGHT_CM = str(input("What is your height in cm?"))
AGE = str(input("What is your age?"))

APP_ID = "YOUR_APP_ID"
# APP_ID = os.environ.get("API_ID")
# print(APP_ID)

API_KEY = "YOUR_API_KEY"
# API_KEY = os.environ.get("API_KEY")
# print(API_KEY)

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)
# print(result["exercises"][0])
# print(result["exercises"][0]["nf_calories"])


# _____________________________________________________________

sheety_endpoint = "YOUR_SHEET_ENDPOINT"
today = datetime.now()

for exercise in result["exercises"]:
    sheety_parameters = {
        "sheet1": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": result["exercises"][0]["name"],
            "duration": f'{result["exercises"][0]["duration_min"]}min',
            "calories": result["exercises"][0]["nf_calories"]
        }
    }

    headers = {
        "Authorization": "TOKEN"
    }
    response_sheety = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=headers)
    print(response_sheety.text)
