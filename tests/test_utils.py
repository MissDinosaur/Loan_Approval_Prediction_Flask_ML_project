"""
Module for testing the cast_to_actual_types function in the utils module.

This module verifies that the function correctly converts input data from
stringformat to their respective numeric and categorical data types.
The tests includevarious edge cases to ensure the function behaves as expected.

Tests:
    - Valid data conversion.
    - Handling of missing keys.
    - Empty input.
    - Invalid numeric conversion.
"""

import pytest
from app import utils


def test_cast_to_actual_types():
    """
    Test that cast_to_actual_types correctly converts valid input data.

    Ensures that string representations of numeric and categorical values are
    accurately cast to their appropriate Python data types.
    """
    mock_data = {
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

    expected_data = {
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
    assert utils.cast_to_actual_types(mock_data) == expected_data


@pytest.mark.parametrize("input_data, expected_output", [
    (   # Test missing keys
        {"Age": "40", "Income": "60000"},
        {"Age": 40, "Income": 60000}
    ),
    (   # Test empty input
        {},
        {}
    ),
    (   # Test invalid numeric conversion
        {"Age": "thirty"},
        {"Age": None}
    ),
    (   # Test invalid numeric conversion
        {"Previous Defaults": '0.0'},
        {"Previous Defaults": 0}
    )
])
def test_cast_to_actual_types_various_cases(input_data, expected_output):
    """
    Test cast_to_actual_types with various input cases.

    This function verifies the handling of:
    - Missing keys: Partial input should return only valid conversions.
    - Empty input: Should return an empty dictionary.
    - Invalid numeric conversion: Should return None for invalid entries.
    """
    if isinstance(expected_output, dict):
        assert utils.cast_to_actual_types(input_data) == expected_output
    else:
        with expected_output:
            utils.cast_to_actual_types(input_data)
