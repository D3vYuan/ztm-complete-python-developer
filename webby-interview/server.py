from flask import Flask, render_template, url_for, request, redirect
import json
from datetime import datetime

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/success.html")
def my_success():
    return render_template("success.html")

def save_to_db(data):
    print(f"Saving to db: {data}")
    return True

@app.route("/submit_form", methods=["POST"])
def submit_form():
    data_dict = request.form.to_dict()
    print(f"Received: {data_dict}")
    
    name = data_dict["name"]

    dob = data_dict["dob"]
    current_year = int(datetime.now().strftime("%Y"))
    dob_year = int(dob.split("-")[0])
    age = current_year - dob_year

    # Address: City State Country
    address = data_dict["address"]
    address_parts = address.split(" ")
    city = address_parts[0]
    state = address_parts[1]
    country = address_parts[2]
    location = f"{city},{state},{country}"

    save_data = {
        "name": name,
        "age": age,
        "location": location
    }

    saved = save_to_db(save_data)
    if saved:
       return redirect("success.html")
    
