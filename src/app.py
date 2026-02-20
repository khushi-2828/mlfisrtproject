import streamlit as st
import os
import pickle

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="SMS Spam Classifier", page_icon="📩")

st.title("📩 SMS Spam Classifier")
st.write("Enter a message below to check whether it is Spam or Not Spam.")

# -------------------------------
# Load Model Safely
# -------------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    model_path = os.path.join(BASE_DIR, "model.pkl")
    vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

    model = pickle.load(open(model_path, "rb"))
    vectorizer = pickle.load(open(vectorizer_path, "rb"))

except Exception as e:
    st.error("Error loading model files.")
    st.write(e)
    st.stop()

# -------------------------------
# User Input
# -------------------------------
input_sms = st.text_area("Enter the message")

if st.button("Predict"):

    if input_sms.strip() == "":
        st.warning("Please enter a message.")
    else:
        try:
            # Vectorize
            transformed_sms = vectorizer.transform([input_sms])

            # Predict
            prediction = model.predict(transformed_sms)[0]

            # Show Result
            if prediction == 1:
                st.error("🚨 Spam Message")
            else:
                st.success("✅ Not Spam Message")

        except Exception as e:
            st.error("Prediction failed.")
            st.write(e)