# streamlit_app.py
import streamlit as st
import requests
import json

# Load API URL and key securely
api_url = st.secrets["api_url"]
api_key = st.secrets["api_key"]

st.set_page_config(page_title="🕵️ Fraud Detection Bot", layout="centered")
st.title("🕵️ Fraud Detection Chatbot")
st.markdown("Paste a transaction and select your preferred language.")

# User inputs
transaction_input = st.text_area("Enter transaction (in JSON)", height=250)
language = st.selectbox("Language", ["English", "Swahili", "Sheng"])

if st.button("Analyze Transaction"):
    try:
        parsed_txn = json.loads(transaction_input)
        res = requests.post(api_url, json={
            "transaction": parsed_txn,
            "language": language
        }, headers={"Authorization": f"Bearer {api_key}"})

        st.success(res.json()["response"])
    except Exception as e:
        st.error(f"Error: {e}")
