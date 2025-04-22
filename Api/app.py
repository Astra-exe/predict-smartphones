from flask import Flask, request, jsonify
from flask_cors import CORS
from prediction import PricePredictor
import os

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})

#load the model
prerdictor = PricePredictor('model_params.npz')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Datos recibidos:", data)
        
        #make sure the data is in the correct format
        input_data = {
            "RAM": int(data['RAM']),
            "age_years": int(data['age_years']),
            "Battery Capacity": int(data['Battery_Capacity']),
            "Condition": data['Condition'],
            "Launched Price (USA)": int(data['Launched_Price_USA'])
        }

        #make the prediction
        prediction = prerdictor.predict(input_data)
        return jsonify({'predicted_price': round(float(prediction), 2)}), 200
    
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({'error': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
        