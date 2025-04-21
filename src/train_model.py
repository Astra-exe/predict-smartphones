import matplotlib.pyplot as plt
import pandas as pd
from data_preprocessing import prepare_features, train_test_split
from linear_regression import LinearRegression

def train_and_evaluate():
    # Cargar y preparar datos
    df = pd.read_csv('../data/refurbished_phones.csv')
    features = ['RAM', 'age_years', 'Launched Price (USA)']
    X, y = prepare_features(df, features, target='refurbished_price')
    
    # Dividir en train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Entrenar modelo
    model = LinearRegression(learning_rate=0.1, epochs=500)
    model.fit(X_train, y_train)
    
    # Evaluar
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    print("=== Métricas ===")
    print(f"MSE Train: {model.mse(y_train, y_pred_train):.2f}")
    print(f"MSE Test: {model.mse(y_test, y_pred_test):.2f}")
    print(f"R² Train: {model.r2_score(y_train, y_pred_train):.2f}")
    print(f"R² Test: {model.r2_score(y_test, y_pred_test):.2f}")
    
    # Visualización
    plt.plot(model.loss_history)
    plt.title("Convergencia del Gradiente Descendente")
    plt.xlabel("Época")
    plt.ylabel("MSE")
    plt.show()

if __name__ == "__main__":
    train_and_evaluate()