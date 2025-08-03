import requests

# API endpoint
url = 'http://127.0.0.1:5000/predict'

# Input values in the expected format
data = {
    "Age": 52,
    "Sex": 1,
    "ChestPainType": 2,
    "RestingBP": 130,
    "Cholesterol": 250,
    "FastingBS": 0,
    "RestingECG": 1,
    "MaxHR": 160,
    "ExerciseAngina": 0,
    "Oldpeak": 1.2,
    "ST_Slope": 2
}

# Send POST request
response = requests.post(url, json=data)

# Print the response from the API
print("✅ Response from API:", response.json())
