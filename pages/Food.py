import streamlit as st
from dotenv import dotenv_values
import requests
import datetime as dt
import Homepage
import pandas as pd

st.set_page_config(
    page_title="Food",
    page_icon="🍚")
st.title("Food")

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
}