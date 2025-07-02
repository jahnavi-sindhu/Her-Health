from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model and scaler
model = joblib.load("random_forest_pcos_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = [
        data["follicle_r"],
        data["follicle_l"],
        data["cycle_length"],
        data["amh"],
        data["bmi"]
    ]
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render provides this PORT
    app.run(debug=True, host="0.0.0.0", port=port)
