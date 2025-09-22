from flask import Flask, request, jsonify
from predict import predict_mpg
import os

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get data as JSON
    cylinders = int(data['cylinders'])
    displacement = float(data['displacement'])
    horsepower = float(data['horsepower'])
    weight = float(data['weight'])
    acceleration = float(data['acceleration'])
    model_year = int(data['model_year'])
    origin = int(data['origin'])

    print(cylinders, displacement, horsepower, weight, acceleration, model_year, origin)

    prediction = predict_mpg(cylinders, displacement, horsepower, weight, acceleration, model_year, origin)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
