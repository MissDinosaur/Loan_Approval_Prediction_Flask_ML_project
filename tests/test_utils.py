import pytest
from app import utils
from werkzeug.datastructures import ImmutableMultiDict


def test_cast_to_actual_types():
    mock_data = ImmutableMultiDict({
        "Age": '30',
        "Income": '50000',
        "Credit Score": '700',
        "Debt-to-Income Ratio": '0.3',
        "Loan Amount": '20000',
        "Assets Value": "10000",
        "Previous Defaults": '0',
        "Employment Status": "Employed",
        "Years at Current Job": '4'
    })

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
    (   #Test missing keys
        {"Age": "40", "Income": "60000"},
        {"Age": 40, "Income": 60000}
    ),
    (   # Test empty input
        {}, 
        {}
    ),
    (   # Test invalid numeric conversion
        {"Age": "thirty"},
        pytest.raises(ValueError)
    )
])
def test_cast_to_actual_types_various_cases(input_data, expected_output):
    if isinstance(expected_output, dict):
        assert utils.cast_to_actual_types(input_data) == expected_output
    else:
        with expected_output:
            utils.cast_to_actual_types(input_data)

