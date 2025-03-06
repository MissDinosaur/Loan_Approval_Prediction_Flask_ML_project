# Flask backend routes
from flask import render_template, request
import hashlib
from ml import predict
from app import app, cache, utils


# Generate a unique cache key based on input data
def generate_cache_key():
    request_data = request.get_json() or request.form.to_dict()
    sorted_data = tuple(sorted(request_data.items()))  # Ensure consistency
    return hashlib.md5(str(sorted_data).encode()).hexdigest()  # Hash for uniqueness

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
@cache.cached(timeout=180, key_prefix=generate_cache_key)  # Cache for 3 minutes
def predict_loan_approval():
    if request.method == 'POST':
        print(f"request: {request}")

        # parse the request data
        request_data = request.get_json()
        if request_data is None:  # if not json, then parse it to dictionary
            request_data = request.form.to_dict()
        
        features_dict = utils.cast_to_actual_types(request_data)

        # Make prediction
        prediction = predict.predict(features_dict)

        # Interpret prediciton
        result = ''
        if prediction[0] == 1:
            result = 'Approved'
        else:
            result = 'Rejected'

        return render_template('result.html', prediction_result=result)
