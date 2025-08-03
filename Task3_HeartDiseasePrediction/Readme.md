 Task 3: Heart Disease Prediction API

📄 Description

Built and deployed a Logistic Regression model using Flask to predict heart disease from patient medical data.

📁 Files

heart.csv – Dataset

model_training.py – Trains model and saves as model.pkl

app.py – Flask API to serve predictions

test_request.py – Sends POST request to test API

🧪 Steps Performed

Encoded categorical variables

Trained logistic regression model

Created prediction API using Flask

Tested API using Python script

🛠️ Libraries Used

pandas

scikit-learn

flask

requests

🔧 API Endpoint

POST http://127.0.0.1:5000/predict

✅ Output
{"prediction": 0}