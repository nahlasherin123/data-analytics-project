import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("project_Medical_Insurance_model.pkl")

st.title("Medical Insurance Cost Prediction")

age = st.number_input("Age", min_value=18, max_value=100, value=25)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox(
    "Region",
    ["southwest", "southeast", "northwest", "northeast"]
)

# Create input dataframe
input_data = pd.DataFrame({
    "age": [age],
    "sex": [sex],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker],
    "region": [region]
})

if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")
