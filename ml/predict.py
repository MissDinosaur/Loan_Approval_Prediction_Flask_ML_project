import pickle
import numpy as np
import pandas as pd


def predict(data: dict):
    # Load the prediction model
    predict_model_name = 'ml/final_model.pkl'
    one_hot_encoder_name = "ml/preprocessor.pkl"
    scaler_name = "ml/scaler.pkl"
    indices_name = "ml/top_indices.pkl"

    with open(predict_model_name, 'rb') as file:
        predict_model = pickle.load(file)

    with open(one_hot_encoder_name, 'rb') as file:
        one_hot_encoder = pickle.load(file)

    with open(scaler_name, 'rb') as file:
        scaler = pickle.load(file)

    with open(indices_name, 'rb') as file:
        top_indices = pickle.load(file)

    print(f"Have {len(data.keys())} keys")

    raw_features = pd.DataFrame([data])
    
    # transform raw features: encode string values and scale numeric values.
    encoded_features = one_hot_encoder.transform(raw_features)
    scaled_features = scaler.transform(encoded_features)
    final_feature = scaled_features[:, top_indices]
    

    prediction = predict_model.predict(final_feature)

    return prediction
