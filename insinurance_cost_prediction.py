import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("project_Medical_Insurance_model.pkl")

st.set_page_config(page_title="Medical Insurance Cost Prediction")

st.title("🏥 Medical Insurance Cost Prediction")

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
    "Number of Children",
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

# Convert categorical values
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0

region_map = {
    "southwest": 0,
    "southeast": 1,
    "northwest": 2,
    "northeast": 3
}

region = region_map[region]

input_data = pd.DataFrame({
    "age": [float(age)],
    "sex": [int(sex)],
    "bmi": [float(bmi)],
    "children": [int(children)],
    "smoker": [int(smoker)],
    "region": [int(region)]
})

if st.button("Predict Insurance Cost"):
    try:
        st.write("Input Data:")
        st.write(input_data)

        prediction = model.predict(input_data)

        st.success(
            f"Estimated Insurance Cost: ${prediction[0]:,.2f}"
        )

    except Exception as e:
        st.error(f"Error: {e}")
