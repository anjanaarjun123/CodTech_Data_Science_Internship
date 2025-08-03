# app.py

from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Heart Disease Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    # Convert input data to numpy array
    features = np.array([list(data.values())])
    
    # Make prediction
    prediction = model.predict(features)
    
    return jsonify({"prediction": int(prediction[0])})  # 0 = No disease, 1 = Disease

if __name__ == "__main__":
    app.run(debug=True)
