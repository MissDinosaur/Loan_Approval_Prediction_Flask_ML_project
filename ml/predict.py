import pickle
import numpy as np

ordered_columns = [
    "Age", "Income", "Credit Score", "Debt-to-Income Ratio", "Loan Amount",
    "Payment History", "Previous Defaults", "Employment Status", "Years at Current Job"
]


sample_data = {
    "Age": 30,
    "Income": 50000,
    "Credit Score": 700,
    "Debt-to-Income Ratio": 0.3,
    "Loan Amount": 20000,
    "Payment History": 'Excellent',
    "Previous Defaults": 0,
    "Employment Status": "Employed",
    "Years at Current Job": 5
}


def predict(data: dict):
    # Load the prediction model
    model_name = 'best_prediction.pkl'
    with open(model_name, 'rb') as file:
        model = pickle.load(file)

    # features need one-hot encoded as it contains non-numeric values.
    features = [data[x] for x in ordered_columns]

    # transform features
    final_features = features

    # reshape final_features
    final_features = np.array(final_features).reshape(1, -1)
    prediction = model.predict(final_features)

    return prediction

