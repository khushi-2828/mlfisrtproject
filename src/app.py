import streamlit as st
import pickle
import os
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords once (safe if already downloaded)
nltk.download('stopwords')

# ---------------------------
# Text Preprocessing Function
# ---------------------------
def transform_text(text):
    text = text.lower()
    words = text.split()

    stop_words = stopwords.words('english')
    
    cleaned_words = []
    for word in words:
        if word not in stop_words and word not in string.punctuation:
            cleaned_words.append(word)

    return " ".join(cleaned_words)


# ---------------------------
# Load Model & Vectorizer
# ---------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(current_dir, "model.pkl")
vectorizer_path = os.path.join(current_dir, "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))


# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Spam Detector", page_icon="📩")

st.title("📩 SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

if st.button("Predict"):
    
    if input_sms.strip() == "":
        st.warning("Please enter a message")
    else:
        # 1. Preprocess
        transformed_sms = transform_text(input_sms)

        # 2. Vectorize
        vector_input = vectorizer.transform([transformed_sms])

        # 3. Predict
        result = model.predict(vector_input)[0]

        # 4. Show Result
        if result == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")

        # 5. Optional: Show Probability (if NB or LR)
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(vector_input)[0]
            st.write("Spam Probability:", round(prob[1]*100, 2), "%")