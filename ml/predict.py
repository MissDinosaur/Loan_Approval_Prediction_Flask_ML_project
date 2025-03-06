import pickle
import pandas as pd
import os

def predict(data: dict):
    # Get the directory of the current script (predict.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct absolute paths to the model and preprocessing files
    predict_model_name = os.path.join(script_dir, 'model.pkl')
    one_hot_encoder_name = os.path.join(script_dir, 'preprocessor.pkl')
    scaler_name = os.path.join(script_dir, 'scaler.pkl')

    # Load the model and preprocessing files
    with open(predict_model_name, 'rb') as file:
        predict_model = pickle.load(file)
    with open(one_hot_encoder_name, 'rb') as file:
        one_hot_encoder = pickle.load(file)
    with open(scaler_name, 'rb') as file:
        scaler = pickle.load(file)

    raw_features = pd.DataFrame([data])

    # Transform raw features: encode string values and scale numeric values.
    encoded_features = one_hot_encoder.transform(raw_features)
    final_feature = scaler.transform(encoded_features)

    #print(f"Encoded Features Shape: {encoded_features.shape}")
    #print(f"Scaled Features Shape: {final_feature.shape}")

    # Predict using the model
    prediction = predict_model.predict(final_feature)

    return prediction
