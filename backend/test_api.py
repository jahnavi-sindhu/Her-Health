import requests
import json

# URL of your running Flask API
url = "http://127.0.0.1:5000/predict"

# Sample input data (make sure keys match what your API expects)
data = {
    "follicle_r": 10,
    "follicle_l": 8,
    "cycle_length": 28,
    "amh": 2.5,
    "bmi": 23.4
}

# Send POST request with JSON data
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    prediction = response.json()
    print("Prediction from API:", prediction)
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response content:", response.text)
