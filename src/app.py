import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("Running from:", BASE_DIR)
print("Files in this folder:", os.listdir(BASE_DIR))

model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))
