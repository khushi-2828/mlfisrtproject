import streamlit as st
import os
import pickle

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered"
)

# -----------------------
# Custom CSS Styling
# -----------------------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #1f4037, #99f2c8);
    }
    .stTextArea textarea {
        border-radius: 10px;
        font-size: 16px;
    }
    .stButton button {
        background-color: #1f4037;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 8px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------
# Header Section
# -----------------------
st.title("📩 SMS Spam Detection System")
st.write("A Machine Learning based Web App to detect Spam Messages.")

# -----------------------
# Load Model
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

# -----------------------
# Input Section
# -----------------------
user_input = st.text_area("Enter your message here:")

if st.button("Analyze Message"):

    if user_input.strip() == "":
        st.warning("⚠ Please enter a message first.")
    else:
        transformed = vectorizer.transform([user_input])
        prediction = model.predict(transformed)[0]
        probability = model.predict_proba(transformed)[0]

        if prediction == 1:
            st.error("🚨 This is a Spam Message")
            st.write(f"Confidence: {round(probability[1]*100,2)}%")
        else:
            st.success("✅ This is Not Spam")
            st.write(f"Confidence: {round(probability[0]*100,2)}%")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit & Machine Learning")
