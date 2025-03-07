"""
Test Module for Prediction Function

This module contains unit tests for the `predict` function from the `ml`
package.

Tests:
    - test_predict_functionality: Ensures valid predictions (0 or 1) are
        returned for different inputs.
    - test_predict_with_invalid_type: Validates error handling for
        unsupported model types.

Dependencies:
    - pytest: For running and managing test cases.
    - ml.predict: Module being tested.
"""

import pytest
from ml import predict

# Sample applicants for testing
applicant_1 = {
    'Age': 55,
    'Income': 10000,
    'Credit Score': 400,
    'Loan Amount': 200000,
    'Employment Status': 'Employed',
    'Years at Current Job': 10,
    'Debt-to-Income Ratio': 0.3,
    'Assets Value': 200000,
    'Previous Defaults': 1
}

applicant_2 = {
    "Age": 30,
    "Credit Score": 700,
    "Previous Defaults": 0,
    "Years at Current Job": 4,
    "Income": 30000.0,
    "Debt-to-Income Ratio": 0.03,
    "Loan Amount": 200000.0,
    'Assets Value': 150000,
    "Employment Status": "Employed"
}


@pytest.mark.parametrize("input_data", [applicant_1, applicant_2])
def test_predict_functionality(input_data: dict) -> None:
    """
    Test the `predict` function for valid inputs.

    Ensures the prediction result is either 0 (rejected) or 1 (approved).

    Parameters:
        input_data (dict): Input data representing applicant features.

    Raises:
        AssertionError: If the prediction is not 0 or 1.
    """
    result = predict.predict(input_data)
    assert result[0] in [0, 1], f"Unexpected prediction result: {result[0]}"


def test_predict_with_invalid_type() -> None:
    """
    Test the `predict` function with an unsupported model loading type.

    Ensures a `ValueError` is raised when an invalid model loading type is provided.

    Raises:
        AssertionError: If no error or an incorrect error is raised.
    """
    with pytest.raises(ValueError, match="Unsupported loading_type. Use 'joblib' or 'pickle'."):
        predict.predict(applicant_1, loading_type="invalid_type")
