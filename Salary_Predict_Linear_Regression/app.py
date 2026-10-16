import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("11AM_ML_MODEL.sav","rb"))
st.set_page_config()

st.title("Salary Prediction App")
st.write("Predict an employee's salary based on their Exp")
st.divider()
years_exp = st.number_input(
    "Enter the exp",
    min_value = 0.0,
    max_value = 50.0,
    value = 1.0,
    step = 0.1
)
if st.button("Predict Salary"):
    input_data = np.array([[years_exp]])
    prediction = model.predict(input_data)
    predict_salary = prediction[0][0]
    st.success(
        f"Predicted Salary: {predict_salary:,.2f}"
    )