# 🎓 Student Dropout Risk Prediction

An end-to-end Machine Learning application that predicts a student's academic status as **Graduate, Enrolled, or Dropout** using a trained **LightGBM classification model**.

The project includes data analysis, feature engineering, model training, MLflow experiment tracking, FastAPI deployment, Docker containerization, and an interactive Streamlit dashboard.

---

## 🚀 Project Overview

Student dropout is an important problem for educational institutions.

This project uses Machine Learning to identify students who may be at risk of dropping out based on factors such as:

- Academic performance
- Admission information
- Previous qualification
- Financial status
- Scholarship status
- Curricular unit performance
- Attendance-related information
- Economic indicators

The system provides both **individual predictions** and **batch predictions using CSV files**.

---

## ✨ Features

### 🤖 Machine Learning

- LightGBM classification model
- Multiple model experiments
- Model evaluation
- Feature engineering
- Feature importance analysis
- Prediction probabilities
- Model persistence using Joblib

### 📊 Data Science

- Exploratory Data Analysis
- Data cleaning
- Feature engineering
- Correlation analysis
- Statistical analysis
- Feature importance visualization

### 📈 MLflow

- Experiment tracking
- Parameter logging
- Metric logging
- Model tracking
- Comparison of different experiments

### ⚡ FastAPI

REST API for real-time predictions.

Example endpoint:

```text
POST /predict