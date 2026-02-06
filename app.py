from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

GRADE_MAP = {0: 'Low', 1: 'Medium', 2: 'High'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = [
            float(data['ph']),
            float(data['temperature']),
            int(data['taste']),
            int(data['odor']),
            int(data['fat']),
            int(data['turbidity']),
            int(data['colour'])
        ]
        
        prediction = model.predict([features])[0]
        grade = GRADE_MAP[prediction]
        
        return jsonify({
            'success': True,
            'grade': grade,
            'prediction': int(prediction)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
