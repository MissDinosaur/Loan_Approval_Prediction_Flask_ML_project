"""
Flask Backend Routes Module

This module defines the routes for a Flask application, including caching
functionality andintegration with a machine learning model for loan approval
prediction.

Routes:
    - `/index`: Renders the home page.
    - `/input`: Renders the input form page.
    - `/predict`: Accepts POST requests with loan application data, predicts
                loan approval, and caches results for 3 minutes.

Dependencies:
    - Flask: For handling web requests and rendering templates.
    - hashlib: For generating unique cache keys.
    - ml: Custom module for running predictions.
    - app: Flask application instance and cache object.
    - utils: Utility functions for data processing.
"""

import hashlib
from flask import render_template, request, Response
from ml import predict
from app import app, cache, utils


def generate_cache_key():
    """
    Generate a unique cache key based on the input request data.

    This function captures the incoming request data, sorts it to ensure
    consistency, and returns a hashed value to use as a cache key.

    Returns:
        str: MD5 hash representing the unique cache key for the request data.
    """
    request_data = request.get_json() or request.form.to_dict()
    sorted_data = tuple(sorted(request_data.items()))  # Ensure consistent ordering
    return hashlib.md5(str(sorted_data).encode()).hexdigest()  # Create a hash


@app.route('/index')
def home():
    """
    Render the home page.

    Returns:
        str: Rendered HTML content of the `index.html` template.
    """
    return render_template('index.html')


@app.route('/input')
def input_page():
    """
    Render the input page where users can submit loan application data.

    Returns:
        str: Rendered HTML content of the `input.html` template.
    """
    return render_template('input.html')


@app.route('/predict', methods=['POST'])
@cache.cached(timeout=180, key_prefix=generate_cache_key)
def predict_loan_approval():
    """
    Handle loan approval prediction requests.

    This endpoint accepts POST requests with loan application data, processes
    the input, performs a prediction using the `predict` module, and renders
    the result.

    The result is cached for 3 minutes based on the input data to improve
    performance.

    Returns:
        Response: Rendered HTML content of the `result.html` template with the
        prediction result.
    """
    if request.method == 'POST':
        print(f"request: {request}")

        # Parse the request data
        request_data = request.get_json()
        if request_data is None:  # Handle non-JSON input
            request_data = request.form.to_dict()

        # Cast request data to expected data types
        features_dict = utils.cast_to_actual_types(request_data)

        # Make prediction
        prediction = predict.predict(features_dict)

        # Interpret prediction result
        result = 'Approved' if prediction[0] == 1 else 'Rejected'

        return render_template('result.html', prediction_result=result)

    return Response(status=405)  # Method Not Allowed
