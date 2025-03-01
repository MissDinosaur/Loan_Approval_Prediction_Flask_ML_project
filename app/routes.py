# Flask backend routes
from flask import render_template, request
from ml import predict 
from app import app, utils  # Import Flask app from __init__.py


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict_loan_approval():
    request_data = request.form  # dict[str, str]
    print("Raw request data:", request_data)  # Debugging
    features_dict = utils.cast_to_actual_types(request_data)
    print("Processed features:", features_dict)  # Debugging

    # Make prediction
    prediction = predict.predict(features_dict)

    # Interpret prediciton
    result = ''
    if prediction == 1:
        result = 'Approved'
    else:
        result = 'Rejected'

    return render_template('result.html', prediction_text=f'The client is {result} for the loan application')
