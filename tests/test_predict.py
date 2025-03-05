from ml import predict

ordered_columns = [
    "Age", "Income", "Credit Score", "Debt-to-Income Ratio", "Loan Amount",
    "Payment History", "Previous Defaults", "Employment Status", "Years at Current Job"
]

full_ordered_columns = [
    'Age', 'Gender', 'Education Level', 'Marital Status', 'Income',
    'Credit Score', 'Loan Amount', 'Loan Purpose', 'Employment Status', 
    'Years at Current Job', 'Payment History', 'Debt-to-Income Ratio', 
    'Assets Value', 'Number of Dependents', 'City', 'State', 'Country', 
    'Previous Defaults', 'Marital Status Change', 'Risk Rating'
]

input_data = {
    "Age": 30,
    "Credit Score": 700,
    "Previous Defaults": 0,
    "Years at Current Job": 4,
    "Income": 50000.0,
    "Debt-to-Income Ratio": 0.3,
    "Loan Amount": 20000.0,
    "Payment History": "Excellent",
    "Employment Status": "Employed"
}

full_columns_data = {
    'Age': '40',
    'Gender': 'Male',
    'Education Level': 'Master',
    'Marital Status': 'Married',
    'Income': '80000',
    'Credit Score': '750',
    'Loan Amount': '20000',
    'Loan Purpose': 'Home',
    'Employment Status': 'Employed',
    'Years at Current Job': '10',
    'Payment History': 'Excellent',
    'Debt-to-Income Ratio': '0.2',
    'Assets Value': '150000',
    'Number of Dependents': '2',
    'City': 'New York',
    'State': 'NY',
    'Country': 'USA',
    'Previous Defaults': '0',
    'Marital Status Change': 'No',
    'Risk Rating': 'Low'
}

result = predict.predict(full_columns_data)
print(f"result: {result[0]}")


# ValueError: columns are missing: 
# {'Marital Status', 'Country', 'Risk Rating', 'Number of Dependents', 
# 'Education Level', 'State', 'City', 'Assets Value', 'Loan Purpose', 'Marital Status Change', 'Gender'}