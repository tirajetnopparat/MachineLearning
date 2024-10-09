# ml_app/model.py
import pickle

# Load the model from the pickle file
with open(r"C:\Users\ASUS Vivobook\Downloads\model_DT.pkl", 'rb') as f:
    model = pickle.load(f)
