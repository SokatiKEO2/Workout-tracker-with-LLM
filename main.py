from dotenv import dotenv_values
import requests
import datetime as dt


SECRET_API = dotenv_values(".env")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me what exercise you did: ")
weight = 78
height = None
age = 20

headers = {
    "x-app-id" : SECRET_API["APP_ID"],
    "x-app-key" : SECRET_API["API_KEY"]
}

parameters = {
    "query" : exercise_text,
    "weight_kg" : None,
    "height_cm" : height,
    "age" : age,
}

response = requests.post(url=exercise_endpoint, headers=headers, json=parameters)
result = response.json()
print(result)

date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

SHEET_ENDPOINT = SECRET_API["SHEET_ENDPOINT"]
GOOGLE_SHEET_NAME = "workout"
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs)
print(f"Sheety Response: \n {sheet_response.text}")
    