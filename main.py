import requests
from datetime import datetime
import os

APP_ID = os.environ.get("NX_APP_ID")
API_KEY = os.environ.get("NX_API_KEY")
SHEETY_USER = os.environ.get("SHEETY_USERNAME")
SHEETY_PASS = os.environ.get("SHEETY_PASSWORD")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_END = os.environ.get("SHEETY_ENDPOINT")

exercise_params = {
    "query": input("What exercise did you do today? "),
    "gender": "male",
    "weight_kg": 74.2,
    "height_cm": 178,
    "age": 31
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=exercise_params, headers=headers)
response_json = nutritionix_response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in response_json["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_response = requests.post(url=SHEETY_END, json=sheet_inputs, auth=(SHEETY_USER, SHEETY_PASS))
print(sheety_response.text)
