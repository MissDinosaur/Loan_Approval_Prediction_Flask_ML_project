import pytest
from ml import predict

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
def test_predict_functionality(input_data):
    result = predict.predict(input_data)

    assert result[0] in [1, 0]

def test_predict_with_invalid_type():
    with pytest.raises(ValueError, match="Unsupported model_loaded_type. Use 'joblib' or 'pickle'."):
        predict.predict(applicant_1, model_loaded_type="invalid_type") 
