import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

model = joblib.load(MODEL_PATH)

def predict_price(area, lat, lng):
    result = model.predict([[area, lat, lng]])
    return round(result[0], 2)