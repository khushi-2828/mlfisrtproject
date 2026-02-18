import streamlit as st
import pickle

# Load model and vectorizer (same folder)
model = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

if st.button("Predict"):

    transformed_sms = cv.transform([input_sms])
    prediction = model.predict(transformed_sms)[0]

    if prediction == 1:
        st.header("Spam 🚨")
    else:
        st.header("Not Spam ✅")
