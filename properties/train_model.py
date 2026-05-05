import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data
data = pd.read_csv("properties/data.csv")

X = data[["area", "latitude", "longitude"]]
y = data["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "properties/model.pkl")

print("Model trained and saved!")