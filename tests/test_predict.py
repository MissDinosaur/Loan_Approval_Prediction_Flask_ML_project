from ml import predict

ordered_columns = [
    "Age", "Income", "Credit Score", "Debt-to-Income Ratio", "Loan Amount",
    "Assets Value", "Previous Defaults", "Employment Status", "Years at Current Job"
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


if __name__ == "__main__":
    result = predict.predict(input_data)
    print(f"result: {result[0]}")
