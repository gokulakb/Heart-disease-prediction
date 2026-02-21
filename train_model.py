import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import os

# Verify file exists
if not os.path.exists('heart.csv'):
    print("Error: heart.csv file not found in current directory!")
    print("Current directory contents:", os.listdir())
    exit()

# Load data
try:
    data = pd.read_csv('heart.csv')
    print("Data loaded successfully. First few rows:")
    print(data.head())
    
    # Preprocessing
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    # Train model
    pipeline.fit(X_train, y_train)
    
    # Save model
    os.makedirs('model', exist_ok=True)
    joblib.dump(pipeline, 'model/heart_model.pkl')
    print("Model trained and saved successfully to model/heart_model.pkl")
    
except Exception as e:
    print(f"Error occurred: {str(e)}")