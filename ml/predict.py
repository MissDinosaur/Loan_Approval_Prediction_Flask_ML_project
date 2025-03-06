import pickle
import pandas as pd
import joblib
import os


def load_model(*model_names, model_loaded_type:str = 'joblib'):
    """
    Recommond joblib. Because
    1. Faster: joblib is optimized for storing large NumPy arrays, which are common in ML models.
    2. More Efficient: It uses memory mapping, allowing large models to be loaded faster without consuming extra RAM.
    So, for saving ML models & preprocessing objects (Scikit-Learn, XGBoost) → Use joblib (faster, more efficient).
    """
    models = [] 
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for name in model_names:
        print(f"model name: {name}")
        file_path = os.path.join(base_dir,"models", name)
        print(f"file_path: {file_path}")
        if model_loaded_type == 'joblib':
            models.append(joblib.load(file_path))
        elif model_loaded_type == 'pickle':
            with open(file_path, 'rb') as file:
                models.append(pickle.load(file))
        else:
            raise ValueError("Unsupported model_loaded_type. Use 'joblib' or 'pickle'.")

    return models if len(models) > 1 else models[0]


def predict(data: dict, model_loaded_type:str = 'joblib'):
    # Load the prediction model and preprocessing components
    model_names = []
    if model_loaded_type == 'joblib':
        model_names = ['model_joblib.pkl', "preprocessor_joblib.pkl", "scaler_joblib.pkl"]
    elif model_loaded_type == 'pickle':
        model_names = ['model.pkl', "preprocessor.pkl", "scaler.pkl"]
    else:
        raise ValueError("Unsupported model_loaded_type. Use 'joblib' or 'pickle'.")
    
    predict_model, one_hot_encoder, scaler = load_model(*model_names)
    raw_features = pd.DataFrame([data])

    # Transform raw features: encode string values and scale numeric values.
    encoded_features = one_hot_encoder.transform(raw_features)
    final_feature = scaler.transform(encoded_features)

    # Predict using the model
    prediction = predict_model.predict(final_feature)

    return prediction  
