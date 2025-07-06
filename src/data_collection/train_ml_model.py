import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def train_ml_model(year):
    data_dir = Path(__file__).resolve().parents[2] / 'data'
    input_file = data_dir / f'f1_preprocessed_laps_{year}.csv'
    
    # Load dataset
    df = pd.read_csv(input_file)
    print(f"Loaded dataset: {input_file}")
    print(f"Dataset shape: {df.shape}")
    
    # Features & Target
    feature_cols = [
        'DriverNumber', 'LapNumber', 'Stint',
        'Compound', 'TrackStatus', 'RaceName'
    ]
    target_col = 'LapTime'
    
    X = df[feature_cols]
    y = df[target_col]
    
    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Model: Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Evaluation
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\n✅ Model Trained Successfully!")
    print(f"Mean Absolute Error (MAE): {mae:.3f} seconds")
    print(f"R2 Score: {r2:.3f}")
    
    # Save model (optional, for later)
    import joblib
    model_path = data_dir / 'lap_time_predictor_model.pkl'
    joblib.dump(model, model_path)
    print(f"\n✅ Model saved at: {model_path}")

if __name__ == "__main__":
    train_ml_model(2023)
