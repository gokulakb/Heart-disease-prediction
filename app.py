from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model/heart_model.pkl')

@app.route('/')
def home():
    return redirect(url_for('home_page'))  # Redirect to home page first

@app.route('/home')
def home_page():
    return render_template('home.html')  # This is now the landing page

@app.route('/assessment')
def assessment():
    return render_template('form.html')  # Renamed from 'form' to 'assessment'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        form_data = {
            'age': float(request.form['age']),
            'sex': float(request.form['sex']),
            'cp': float(request.form['cp']),
            'trestbps': float(request.form['trestbps']),
            'chol': float(request.form['chol']),
            'fbs': float(request.form['fbs']),
            'restecg': float(request.form['restecg']),
            'thalach': float(request.form['thalach']),
            'exang': float(request.form['exang']),
            'oldpeak': float(request.form['oldpeak']),
            'slope': float(request.form['slope']),
            'ca': float(request.form['ca']),
            'thal': float(request.form['thal'])
        }
        
        features = np.array([[form_data['age'], form_data['sex'], form_data['cp'], 
                           form_data['trestbps'], form_data['chol'], form_data['fbs'],
                           form_data['restecg'], form_data['thalach'], form_data['exang'],
                           form_data['oldpeak'], form_data['slope'], form_data['ca'],
                           form_data['thal']]])
        
        prediction = model.predict(features)[0]
        
        disease_types = {
            0: "No Heart Disease",
            1: "Typical Angina",
            2: "Atypical Angina",
            3: "Non-anginal Pain",
            4: "Asymptomatic"
        }
        
        result = {
            'prediction': prediction,
            'disease_type': disease_types.get(prediction, "Unknown"),
            'is_positive': prediction != 0
        }
        
        return render_template('result.html', result=result, form_data=form_data)
    
    return redirect(url_for('assessment'))

if __name__ == '__main__':
    app.run(debug=True)