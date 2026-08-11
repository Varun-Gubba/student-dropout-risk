from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
import pandas as pd
import joblib

# -------------------------------
# Load trained model
# -------------------------------
model = joblib.load("models/final_model.pkl")

# -------------------------------
# Feature order used during training
# -------------------------------
feature_columns = [
    "Marital status",
    "Application mode",
    "Application order",
    "Course",
    "Daytime/evening attendance",
    "Previous qualification",
    "Previous qualification (grade)",
    "Nacionality",
    "Mother's qualification",
    "Father's qualification",
    "Mother's occupation",
    "Father's occupation",
    "Admission grade",
    "Displaced",
    "Educational special needs",
    "Debtor",
    "Tuition fees up to date",
    "Gender",
    "Scholarship holder",
    "Age at enrollment",
    "International",
    "Curricular units 1st sem (credited)",
    "Curricular units 1st sem (enrolled)",
    "Curricular units 1st sem (evaluations)",
    "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)",
    "Curricular units 1st sem (without evaluations)",
    "Curricular units 2nd sem (credited)",
    "Curricular units 2nd sem (enrolled)",
    "Curricular units 2nd sem (evaluations)",
    "Curricular units 2nd sem (approved)",
    "Curricular units 2nd sem (grade)",
    "Curricular units 2nd sem (without evaluations)",
    "Unemployment rate",
    "Inflation rate",
    "GDP",
    "Average_grade",
    "Total_approved",
    "Grade_improvement",
    "Total_enrolled",
    "Approval_rate"
]

# -------------------------------
# Prediction mapping
# -------------------------------
target_map = {
    0: "Dropout",
    1: "Enrolled",
    2: "Graduate"
}

# -------------------------------
# FastAPI App
# -------------------------------
app = FastAPI(
    title="Student Dropout Prediction API",
    description="Predict whether a student will Dropout, Enroll or Graduate",
    version="1.0"
)

# -------------------------------
# Input Model
# -------------------------------
class StudentInput(BaseModel):
    data: Dict[str, Any]

# -------------------------------
# Home Route
# -------------------------------
@app.get("/")
def home():
    return {
        "message": "Student Dropout Prediction API"
    }

# -------------------------------
# Prediction Route
# -------------------------------
@app.post("/predict")
def predict(student: StudentInput):

    df = pd.DataFrame([student.data])

    # Ensure correct feature order
    df = df[feature_columns]

    prediction = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]

    return {
    "prediction": int(prediction),
    "probabilities": probabilities.tolist()
}