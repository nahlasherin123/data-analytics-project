import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("project_Medical_Insurance_model.pkl")

st.title("Medical Insurance Cost Prediction")

age = st.number_input("Age", min_value=18, max_value=100, value=25)

sex = st.selectbox(
    "Sex",
    ["male", "female"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

children = st.number_input(
    "Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.selectbox(
    "Smoker",
    ["yes", "no"]
)

region = st.selectbox(
    "Region",
    ["southwest", "southeast", "northwest", "northeast"]
)

input_data = pd.DataFrame({
    "age": [float(age)],
    "sex": [str(sex)],
    "bmi": [float(bmi)],
    "children": [int(children)],
    "smoker": [str(smoker)],
    "region": [str(region)]
})

if st.button("Predict Insurance Cost"):
    try:
        prediction = model.predict(input_data)
        st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
        st.write("Input Data:")
        st.write(input_data)
        st.write("Data Types:")
        st.write(input_data.dtypes)
