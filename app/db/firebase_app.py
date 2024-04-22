import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("certificate-validation-f9f21.appspot.com"),
    "messagingSenderId": os.getenv("742385511256"),
    "appId": os.getenv("1:742385511256:web:dde5ded2da815a1627932d"),
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def register(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"

def login(email, password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"