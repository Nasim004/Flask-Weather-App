import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
load_dotenv()
app = Flask(__name__)
app.config["DEBUG"] = True
api_key = os.getenv("openweather_key")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get('city')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        response = requests.get(url).json()

        weather = {
            "city": city,
            "temperature": response["main"]["temp"],
            "description": response["weather"][0]["description"],
            "icon": response["weather"][0]["icon"],
        }
        return render_template("weather.html", weather=weather)
    return render_template("weather.html",weather=None)
