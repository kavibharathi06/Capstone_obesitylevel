import streamlit as st
import numpy as np
import joblib

# Load saved models
reg_model = joblib.load("best_reg_model.pkl")
class_model = joblib.load("best_class_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Obesity Level & BMI Prediction")
st.write("Enter lifestyle details to get predictions")

# -------- USER INPUTS --------
Gender = st.selectbox("Gender", ["Male", "Female"])
Age = st.number_input("Age", 10, 100)
Height = st.number_input("Height (meters)", 1.0, 2.5)
Weight = st.number_input("Weight (kg)", 30.0, 200.0)

family_history = st.selectbox("Family history with overweight", ["yes", "no"])
FAVC = st.selectbox("High caloric food consumption", ["yes", "no"])
FCVC = st.slider("Vegetable intake (1–3)(/1-low/2-medium/3-high/)", 1.0, 3.0)
NCP = st.slider("Number of meals per day", 1.0, 4.0)
CAEC = st.selectbox("Food consumption between meals",["no", "Sometimes", "Frequently"])
SMOKE = st.selectbox("Do you smoke?", ["yes", "no"])
CH2O = st.slider("Water intake (1–3)(1 → low, 3 → high)", 1.0, 3.0)
SCC = st.selectbox("Calorie monitoring", ["yes", "no"])
FAF = st.slider("Physical activity (0–3)(0 → none, 1 → low, 2 → medium, 3 → high)", 0.0, 3.0)
TUE = st.slider("Technology usage (0–2)(0 → low, 2 → high)", 0.0, 2.0)
CALC = st.selectbox("Alcohol consumption", ["no", "Sometimes", "Frequently"])
MTRANS = st.selectbox(
    "Mode of transport",
    ["Bike", "Motorbike", "Public_Transportation", "Walking"]
)

# -------- ENCODING --------
Gender = 1 if Gender == "Male" else 0
family_history = 1 if family_history == "yes" else 0
FAVC = 1 if FAVC == "yes" else 0
SMOKE = 1 if SMOKE == "yes" else 0
SCC = 1 if SCC == "yes" else 0

CAEC_map = {
    "no": [1, 0, 0],
    "Sometimes": [0, 1, 0],
    "Frequently": [0, 0, 1]
}
CAEC_vals = CAEC_map[CAEC]


CALC_map = {"no": 0, "Sometimes": 1, "Frequently": 2}
CALC = CALC_map[CALC]

MTRANS_map = {
    "Bike": [1,0,0,0],
    "Motorbike": [0,1,0,0],
    "Public_Transportation": [0,0,1,0],
    "Walking": [0,0,0,1]
}
MTRANS_vals = MTRANS_map[MTRANS]

# -------- FEATURE VECTOR (MUST MATCH TRAINING ORDER) --------
input_data = np.array([
    Gender, Age, Height, Weight,
    family_history, FAVC, FCVC, NCP,
    SMOKE, CH2O, SCC, FAF, TUE, CALC,
    *CAEC_vals,
    *MTRANS_vals
]).reshape(1, -1)

# Scale input
input_scaled = scaler.transform(input_data)

# -------- PREDICTION --------
if st.button("Predict"):
    bmi = reg_model.predict(input_scaled)[0]
    obesity = class_model.predict(input_scaled)[0]

    st.success(f"Predicted BMI: {bmi:.2f}")
    st.success(f"Predicted Obesity Level: {obesity}")
print("Number of features:", input_data.shape[1])

