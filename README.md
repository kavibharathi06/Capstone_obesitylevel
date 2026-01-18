🏥 Obesity Level & BMI Prediction System
📌 Project Overview

This project is an end-to-end machine learning application designed to predict an individual’s Body Mass Index (BMI) and obesity level based on lifestyle, dietary habits, and physical activity data. The system uses real-world health data and compares multiple machine learning algorithms to automatically select the best-performing models for both regression and classification tasks.

🎯 Problem Statement

Obesity is a major health concern influenced by various lifestyle factors such as diet, physical activity, and daily habits. The goal of this project is to:

Predict BMI values using regression models

Classify individuals into obesity categories using classification models

Provide real-time predictions through an interactive web interface

📊 Dataset

Name: Estimation of Obesity Levels Based on Eating Habits and Physical Condition

Source: UCI Machine Learning Repository (available on Kaggle)

Data Type: Structured tabular data

Features: Age, Gender, Height, Weight, food habits, physical activity, lifestyle indicators

Target Variables:

BMI (Regression target)

NObeyesdad (Classification target)

🛠️ Technologies Used

Programming Language: Python

Libraries: NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn

Model Deployment: Streamlit

Model Persistence: Joblib

🔍 Machine Learning Approach
1️⃣ Data Preprocessing

Handling missing values

Label encoding and one-hot encoding for categorical features

Feature scaling using StandardScaler

Train-test split for model evaluation

2️⃣ Model Training & Evaluation

Regression Models (BMI Prediction):

Linear Regression

Decision Tree Regressor

Random Forest Regressor

K-Nearest Neighbors Regressor

Classification Models (Obesity Level Prediction):

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

K-Nearest Neighbors Classifier

3️⃣ Model Selection

Regression models evaluated using MAE and R² score

Classification models evaluated using Accuracy and F1-score

Best-performing models automatically selected based on evaluation metrics

🚀 Deployment

Developed an interactive Streamlit web application

Allows users to enter lifestyle and physical details in real time

Uses trained models to predict BMI and obesity level instantly

Ensures consistent preprocessing during inference

📈 Key Features

End-to-end machine learning pipeline

Combined regression and classification in a single project

Automated best model selection

Real-time predictions via web interface

Beginner-friendly and scalable design
