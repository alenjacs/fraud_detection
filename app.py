import streamlit as st
import pandas as pd
import joblib


@st.cache_resource
def load_model():
    return joblib.load("notebooks/fraud_model.pkl")

model = load_model()

st.title("Credit Card Fraud Detection")
st.write("Upload a CSV of transactions (columns V1…V28, Amount).")
uploaded_file = st.file_uploader("Choose CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # 1) Drop label column if present
    df = df.drop(columns=["Class"], errors="ignore")
    # 2) Reorder to match training features exactly
    df = df[model.feature_names_in_]
    # 3) Predict
    preds = model.predict(df)
    df["Prediction"] = ["Fraud" if p == 1 else "Not Fraud" for p in preds]
    st.dataframe(df)
    counts = df["Prediction"].value_counts()
    st.bar_chart(counts)
    st.markdown("###  Prediction Summary")
    st.success(f" Not Fraud: **{counts.get('Not Fraud', 0):,}**")
    st.error(f" Fraud: **{counts.get('Fraud', 0):,}**")


