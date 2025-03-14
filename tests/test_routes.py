"""
Unit tests for Flask routes handling loan approval predictions.

These tests mock external dependencies and validate:
1. Home page accessibility.
2. Loan approval prediction with form data and JSON.
3. Handling both approved and rejected outcomes.
"""

from unittest.mock import patch
import pytest
import json
from app import app  # Import app from __init__.py


# Mock the features of dict that will be sent in the POST request
mock_form_dict_data = {
    "Age": '30',
    "Income": '50000',
    "Credit Score": '700',
    "Debt-to-Income Ratio": '0.3',
    "Loan Amount": '20000',
    "Assets Value": "10000",
    "Previous Defaults": '0',
    "Employment Status": "Employed",
    "Years at Current Job": '4'
}

# Mock the features of json that will be sent in the POST request
mock_form_json_data = json.dumps(mock_form_dict_data, default=str)

# Mock the cast_to_actual_types function to return a processed dictionary
mock_processed_data = {
    "Age": 30,
    "Credit Score": 700,
    "Previous Defaults": 0,
    "Years at Current Job": 4,
    "Income": 50000.0,
    "Debt-to-Income Ratio": 0.3,
    "Loan Amount": 20000.0,
    "Assets Value": 10000,
    "Employment Status": "Employed"
}


@pytest.fixture  # Sets up a Flask test client to simulate HTTP requests.
def client():
    app.config['TESTING'] = True  # Enable test mode
    client = app.test_client()    # Create a Flask test client
    yield client


def test_home_page(client):
    # Simulate a GET request to the home page
    response = client.get('/index')

    assert response.status_code == 200


@patch('app.utils.cast_to_actual_types')  # Mock cast_to_actual_types
@patch('ml.predict.predict')  # Mock the predict function
def test_predict_loan_approval_dict(mock_predict, mock_cast_to_actual_types, client):
    # Mock the return value of cast_to_actual_types function
    mock_cast_to_actual_types.return_value = mock_processed_data
    
    # Mock the return value of predict function
    mock_predict.return_value[0] = 1  # Simulate "Approved"

    response = client.post('/predict', json=mock_form_dict_data)  # simulate submitting a form with data.

    assert response.status_code == 200

    # Ensure cast_to_actual_types function was called with correct data
    mock_cast_to_actual_types.assert_called_with(mock_form_dict_data)
    # Ensure mock_predict function was called with correct data
    mock_predict.assert_called_with(mock_processed_data)

@patch('app.utils.cast_to_actual_types')  # Mock cast_to_actual_types
@patch('ml.predict.predict')  # Mock the predict function
def test_predict_loan_approval_json(mock_predict, mock_cast_to_actual_types, client):
    # Mock the return value of cast_to_actual_types function
    mock_cast_to_actual_types.return_value = mock_processed_data
    
    # Mock the return value of predict function
    mock_predict.return_value[0] = 1  # Simulate "Approved"

    response = client.post('/predict', json=mock_form_json_data)  # simulate submitting a form with data.

    assert response.status_code == 200

    # Ensure cast_to_actual_types function was called with correct data
    mock_cast_to_actual_types.assert_called_with(mock_form_json_data)
    # Ensure mock_predict function was called with correct data
    mock_predict.assert_called_with(mock_processed_data)


@patch('app.utils.cast_to_actual_types')  # Mock cast_to_actual_types
@patch('ml.predict.predict')
def test_predict_loan_approval_rejected(mock_predict, mock_cast_to_actual_types, client):
    # Mock the return value of cast_to_actual_types function
    mock_cast_to_actual_types.return_value = mock_processed_data
    
    # Mock the return value to simulate "Rejected"
    mock_predict.return_value[0] = 0

    # Simulate the POST request to /predict
    response = client.post('/predict', json=mock_form_dict_data)

    assert response.status_code == 200

