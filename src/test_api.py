import requests

url = 'http://127.0.0.1:5000/predict'

data = {
    'cylinders': 5.1,
    'displacement': 3.5,
    'horsepower': 1.4,
    'weight': 0.2,
    'acceleration' : 12.0,
    'model_year' : 70,
    'origin' : 1
}

response = requests.post(url, data=data)

if response.status_code == 200:
    prediction = response.json()['prediction']
    print('Predicted Car MPG:', prediction)
else:
    print('Error:', response.status_code)