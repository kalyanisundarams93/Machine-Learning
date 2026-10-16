import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("startup.sav","rb"))
st.set_page_config()

st.title("Startup Profit detection app")
st.write("Predict an startup profit based on their expense")
st.divider()
rd_spend = st.number_input(
    "Enter R&D Spend",
    min_value = 0.0,
    max_value = 999999.0,
    value = 1.0,
    step = 0.01
)
admin = st.number_input(
    "Enter the Administration",
    min_value = 0.0,
    max_value = 999999.0,
    value = 1.0,
    step = 0.01
)
mark = st.number_input(
    "Enter the Marketing Spend",
    min_value = 0.0,
    max_value = 999999.0,
    value = 1.0,
    step = 0.01
)
if st.button("Predict Profit"):
    input_data = pd.DataFrame([{
        'R&D Spend': rd_spend,
        'Administration': admin,
        'Marketing Spend': mark
    }])
    prediction = model.predict(input_data)
    predict_profit = prediction[0][0]
    st.success(
        f"Predicted Profit: ₹{float(predict_profit):,.2f}"
    )