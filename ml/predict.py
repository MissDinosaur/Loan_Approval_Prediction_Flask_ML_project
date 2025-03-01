import pickle
import numpy as np

ordered_columns = [
    "Age", "Income", "Credit Score", "Debt-to-Income Ratio", "Loan Amount",
    "Payment History", "Previous Defaults", "Employment Status", "Years at Current Job"
]

sample_data = {
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


def predict(data: dict):
    # Load the prediction model
    model_name = 'best_prediction.pkl'
    with open(model_name, 'rb') as file:
        model = pickle.load(file)

    # extract the valuues into a list with the specific order
    features = [data.get(x, None) for x in ordered_columns]

    # transform features: features need one-hot encoded as it contains non-numeric values.
    final_features = features

    # reshape final_features
    final_features = np.array(final_features).reshape(1, -1)
    prediction = model.predict(final_features)

    return prediction

