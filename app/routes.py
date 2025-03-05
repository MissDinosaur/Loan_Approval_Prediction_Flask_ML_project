from flask import render_template, request, redirect, url_for
from ml import predict 
from app import app, utils  # Import Flask app from __init__.py

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict_loan_approval():
    if request.method == 'POST':
        print(f"request: {request}")
        request_data = request.get_json()
        if request_data is None:  # if not JSON, then parse it to dictionary
            request_data = request.form.to_dict()
        print("Raw request data:", request_data)  # Debugging

        # Convert input types
        features_dict = utils.cast_to_actual_types(request_data)
        print("Processed features:", features_dict)  # Debugging

        # Ensure all required features exist
        if "Assets Value" not in features_dict:
            features_dict["Assets Value"] = 0.0  # Default value if missing

        # Make actual prediction using the ML model
        prediction = predict.predict(features_dict)

        # Interpret prediction result
        result = 'Approved' if prediction[0] == 1 else 'Rejected'

        # Redirect to /result with prediction query parameter
        return redirect(url_for('result_page', prediction=result))

@app.route('/result')
def result_page():
    # Read query parameter
    prediction = request.args.get('prediction', 'No prediction available')
    return render_template('result.html', prediction_result=prediction)
