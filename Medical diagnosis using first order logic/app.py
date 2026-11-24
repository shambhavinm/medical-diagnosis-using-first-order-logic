import streamlit as st

st.set_page_config(page_title="Medical Diagnosis System")

st.title("🏥 Medical Diagnosis Using First-Order Rule Learning")

disease = st.selectbox(
    "Choose Disease",
    ["Diabetes", "Heart Disease"]
)

# Diabetes Section
if disease == "Diabetes":

    st.subheader("Diabetes Prediction")

    glucose = st.number_input("Glucose Level", 0, 300, 120)
    bmi = st.number_input("BMI", 0.0, 50.0, 25.0)
    age = st.number_input("Age", 1, 100, 30)

    if st.button("Predict Diabetes"):

        if glucose > 140 and bmi > 30:
            st.error("⚠ Diabetes Positive")
            st.write("Rule Applied:")
            st.write("IF Glucose > 140 AND BMI > 30 THEN Diabetes")
        else:
            st.success("✅ No Diabetes Detected")

# Heart Disease Section
if disease == "Heart Disease":

    st.subheader("Heart Disease Prediction")

    age = st.number_input("Age", 1, 100, 50)
    chol = st.number_input("Cholesterol", 100, 400, 200)
    bp = st.number_input("Blood Pressure", 80, 250, 120)

    if st.button("Predict Heart Disease"):

        if chol > 240 and bp > 140:
            st.error("⚠ Heart Disease Risk High")
            st.write("Rule Applied:")
            st.write("IF Cholesterol > 240 AND BP > 140 THEN Heart Disease")
        else:
            st.success("✅ Low Heart Disease Risk")