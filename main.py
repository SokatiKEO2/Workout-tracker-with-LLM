import os
from dotenv import load_dotenv, find_dotenv
load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

print(APP_ID)