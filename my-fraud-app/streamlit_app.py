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

# User input
user_input = st.text_input("Paste transaction JSON below:")

st.write("Raw Input:", user_input)  # Debug line to see what’s coming in

if st.button("Analyze Transaction"):
    if not user_input:
        st.warning("No input detected! Please paste JSON above.")
    else:
        try:
            transaction_data = json.loads(user_input)
            st.success("Transaction loaded successfully!")
            st.json(transaction_data)
        except json.JSONDecodeError as e:
            st.error(f"Invalid JSON format: {e}")


