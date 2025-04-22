from flask import Flask, request, jsonify
from flask_cors import CORS
from prediction import PricePredictor
import os

app = Flask(__name__)
CORS(app)

#load the model
prerdictor = PricePredictor('model_params.npz')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        #verify the fields from the request
        required_fields = ['RAM', 'age_years', 'Battery Capacity', 'Condition', 'Launched Price (USA)']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Hay campos faltantes"}), 400
        
        #make sure the data is in the correct format
        input_data = {
            "RAM": float(data['RAM']),
            "age_years": float(data['age_years']),
            "Battery Capacity": float(data['Battery Capacity']),
            "Condition": data['Condition'],
            "Launched Price (USA)": float(data['Launched Price (USA)'])
        }

        #make the prediction
        prediction = prerdictor.predict(input_data)
        prediction = round(prediction, 2)
        return jsonify({"predicted_price": prediction}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
        