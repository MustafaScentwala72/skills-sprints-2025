import streamlit as st
import joblib
import pandas as pd

st.title("Fraud Risk — Demo App")
st.write("This is a minimal demo. Replace with your trained model.")

uploaded = st.file_uploader("Upload CSV with input rows")
if uploaded:
    df = pd.read_csv(uploaded)
    st.write("Preview:", df.head())
    st.write("Pretend predictions go here…")
