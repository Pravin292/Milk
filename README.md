# Milk Quality Prediction System 🥛

A machine learning-powered web application that predicts milk quality (Low, Medium, or High) based on various physical and chemical parameters.

## Core Features
- **AI-Driven Analysis**: Uses an XGBoost model with ~99.7% accuracy.
- **Premium UI**: Modern, glassmorphic design for a superior user experience.
- **Real-time Predictions**: Instant feedback on milk grade.

## Parameters Analyzed
- `pH Level`
- `Temperature`
- `Taste` (Good/Bad)
- `Odor` (Good/Bad)
- `Fat Content` (Optimal/Low)
- `Turbidity` (High/Low)
- `Colour Value`

## Tech Stack
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, XGBoost, Pandas
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design), JavaScript (ES6+)

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5001` in your browser.

## Model Performance
- **XGBoost Accuracy**: 99.69%
- **Decision Tree Accuracy**: 99.37%
- **Gradient Boosting Accuracy**: 99.06%
