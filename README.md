# NutriPredict

## Overview

NutriPredict is a Machine Learning-based web application that predicts an individual's Body Mass Index (BMI) and Obesity Level based on health and lifestyle attributes. The project demonstrates an end-to-end machine learning pipeline, including data preprocessing, model training, model evaluation, comparison of multiple algorithms, and deployment using Streamlit.

---

## Problem Statement

Maintaining a healthy lifestyle requires continuous monitoring of health indicators such as BMI and obesity level. Manual calculation and interpretation can be time-consuming and may not consider multiple influencing factors. NutriPredict provides an automated prediction system that assists users by estimating BMI and obesity category based on user-provided health information.

---

## Objectives

- Predict BMI as a regression task.
- Predict obesity level as a classification task.
- Compare multiple machine learning algorithms.
- Evaluate model performance using appropriate metrics.
- Deploy the trained models as an interactive web application.

---

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

---

## Machine Learning Pipeline

### 1. Data Collection

Health and lifestyle dataset containing demographic, physical, and behavioral features.

### 2. Data Preprocessing

- Missing value handling
- Categorical feature encoding
- Feature selection
- Data splitting (Train-Test Split)

### 3. Regression Models

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

Target:
- BMI Prediction

Evaluation Metrics:
- Mean Absolute Error (MAE)
- R² Score

---

### 4. Classification Models

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

Target:
- Obesity Level Prediction

Evaluation Metrics:
- Accuracy
- F1 Score

---

### 5. Model Selection

Multiple algorithms were evaluated to identify the best-performing model based on evaluation metrics. Random Forest achieved the highest overall performance for both regression and classification tasks.

---

### 6. Model Deployment

The selected models were serialized using Joblib and integrated into a Streamlit application that accepts user inputs and generates real-time predictions.

---

## Features

- BMI Prediction
- Obesity Level Classification
- Interactive User Interface
- Real-time Predictions
- Machine Learning Model Comparison

---

## Project Workflow

User Input

↓

Data Preprocessing

↓

Model Prediction

↓

BMI Prediction

↓

Obesity Classification

↓

Display Results

---

## Learning Outcomes

- End-to-end Machine Learning workflow
- Data preprocessing techniques
- Regression and classification algorithms
- Model evaluation and comparison
- Streamlit application development
- Model deployment using Joblib

---

## Future Enhancements

- Integration with cloud deployment platforms
- User authentication
- Personalized health recommendations
- Real-time health analytics dashboard
- Expanded dataset for improved generalization
