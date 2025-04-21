import matplotlib.pyplot as plt
import pandas as pd
from data_preprocessing import prepare_features, train_test_split
from linear_regression import LinearRegression

def train_and_evaluate():
    # load and prepare the dataset
    df = pd.read_csv('../data/refurbished_phones.csv')
    features = ['RAM', 'age_years', 'Battery Capacity', 'Screen Size', 'Condition_Encoded', 'Launched Price (USA)']
    X, y = prepare_features(df, features, target='refurbished_price')
    
    # separate training and testing data
    # 80% training and 20% testing
    X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2)
    
    # Train the model
    model = LinearRegression(learning_rate=0.01, epochs=1000)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    print("=== Métricas ===")
    print(f"MSE Train: {model.mse(y_train, y_pred_train):.2f}")
    print(f"MSE Test: {model.mse(y_test, y_pred_test):.2f}")
    print(f"R² Train: {model.r2_score(y_train, y_pred_train):.2f}")
    print(f"R² Test: {model.r2_score(y_test, y_pred_test):.2f}")
    
    # Viz
    plt.plot(model.loss_history)
    plt.title("Convergencia del Gradiente Descendente")
    plt.xlabel("Época")
    plt.ylabel("MSE")
    plt.show()

if __name__ == "__main__":
    train_and_evaluate()