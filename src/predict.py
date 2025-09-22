import numpy as np
import joblib
import os
from train import run_training

# Load the trained model
model = joblib.load("model/model.pkl")

def predict_mpg(cylinders, displacement, horsepower, weight, acceleration, model_year, origin):
    input_data = np.array([[cylinders, displacement, horsepower, weight, acceleration, model_year, origin]])
    prediction = model.predict(input_data)
    return prediction[0]

if __name__ == "__main__":
    if os.path.exists("model/model.pkl"):
        print("Model loaded successfully")
    else:
        os.makedirs("model", exist_ok=True)
        run_training()
