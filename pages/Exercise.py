import streamlit as st
from dotenv import dotenv_values
import requests
import datetime as dt
import Homepage
import pandas as pd

st.set_page_config(
    page_title="Exercise",
    page_icon="🤸")
st.title("Exercise")

SECRET_API = dotenv_values(".env")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
weight = Homepage.weight
height = Homepage.height
age = Homepage.age
exercise_text = st.text_input("Tell me what exercise you did: ")

headers = {
    "x-app-id": SECRET_API["APP_ID"],
    "x-app-key": SECRET_API["API_KEY"]
}

parameters = {
    "query": exercise_text,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
}

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['date', 'time', 'exercise', 'duration', 'calories'])

if exercise_text:
    response = requests.post(url=exercise_endpoint, headers=headers, json=parameters)
    result = response.json()

    date = dt.datetime.now().strftime("%d/%m/%Y")
    time = dt.datetime.now().strftime("%X")
    exercises_to_append = []

    for exercise in result["exercises"]:
        data_to_append = {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
        exercises_to_append.append(data_to_append)

    st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame(exercises_to_append)], ignore_index=True)

st.write(st.session_state.df)
