import numpy as np
import pandas as pd

class PricePredictor:
    def __init__(self, model_path):
        params = np.load(model_path, allow_pickle=True)
        self.theta = params['theta']
        self.X_mean = params['X_mean']
        self.X_std = params['X_std']
        self.features = params['features'].tolist()
        
    def preprocess_input(self, input_data):
        # Convert input data to DataFrame
        df = pd.DataFrame([input_data])
        
        # Map categorical feature 'Condition' to numerical values
        condition_map = {'Excelente': 3, 'Bueno': 2, 'regular': 1}
        df['Condition_Encoded'] = df['Condition'].map(condition_map)
        
        # Extraect features in the same order as the model was trained
        X = df[self.features].values.astype(float)
        
        # Normalize 
        X_normalized = (X - self.X_mean) / self.X_std
        
        # Add bias term
        return np.hstack(([[1]], X_normalized))
    
    def predict(self, input_data):
        X = self.preprocess_input(input_data)
        return X.dot(self.theta)[0][0]

# Ejemplo de uso
if __name__ == "__main__":
    predictor = PricePredictor('model_params.npz')
    
    # Ejemplo de input (debe coincidir con las features)
    nuevo_telefono = {
        "RAM": 6,
        "age_years": 2,
        "Battery Capacity": 4000,
        "Condition": "Bueno",
        "Launched Price (USA)": 699
    }
    
    prediccion = predictor.predict(nuevo_telefono)
    print(f"Precio estimado: ${prediccion:.2f}")