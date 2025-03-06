"""
Model Loading and Prediction Module

This module provides utilities to load machine learning models and perform
predictions using pre-trained models and preprocessing components.

Functions:
    - load_model: Loads models from disk using joblib (recommended) or pickle.
    - predict: Performs prediction on input data after preprocessing.

Recommendation:
    - Use joblib for loading ML models and preprocessing objects due to its
    efficiency:
        1. Faster: Optimized for large NumPy arrays.
        2. Memory-efficient: Uses memory mapping for faster access and reduced
            RAM usage.

Dependencies:
    - pickle: For loading models in pickle format.
    - pandas: For handling input data.
    - joblib: For faster model serialization/deserialization.
    - os: For handling file paths.
"""

import pickle
import pandas as pd
import joblib
import os
from typing import  Any


def load_model(*model_names: str,
               model_loaded_type: str = 'joblib') -> Any | list:
    """
    Load machine learning models from disk.

    This function loads models saved in either joblib or pickle format from
    the 'models' directory.

    Parameters:
        model_names (str): Variable-length argument of model filenames to load.
        model_loaded_type (str): The model serialization type
        ('joblib' or 'pickle'). Default is 'joblib'.

    Returns:
        Union[Any, List[Any]]: A single model object if one model is loaded,
        or a list of models.

    Raises:
        ValueError: If an unsupported model_loaded_type is provided.

    Example:
        >>> load_model('model_joblib.pkl', 'preprocessor_joblib.pkl')
        [model_object, preprocessor_object]
    """
    models = []
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for name in model_names:
        print(f"Loading model: {name}")
        file_path = os.path.join(base_dir, "models", name)
        print(f"File path: {file_path}")

        if model_loaded_type == 'joblib':
            models.append(joblib.load(file_path))
        elif model_loaded_type == 'pickle':
            with open(file_path, 'rb') as file:
                models.append(pickle.load(file))
        else:
            raise ValueError("Unsupported model_loaded_type. Use 'joblib' or 'pickle'.")

    return models if len(models) > 1 else models[0]


def predict(data: dict, model_loaded_type: str = 'joblib'):
    """
    Perform predictions using a pre-trained machine learning model.

    This function loads the prediction model, one-hot encoder, and scaler,
    applies preprocessing, and returns the prediction result.

    Parameters:
        data (Dict[str, Any]): Input data for prediction as a dictionary.
        model_loaded_type (str): Model serialization type
        ('joblib' or 'pickle'). Default is 'joblib'.

    Returns:
        Any: The prediction result from the model.

    Raises:
        ValueError: If an unsupported model_loaded_type is provided.

    Example:
        >>> predict({"Age": 35, "Income": 75000.0})
        array([1])
    """
    # Define model file names based on serialization type
    if model_loaded_type == 'joblib':
        model_names = ['model_joblib.pkl', 'preprocessor_joblib.pkl',
                       'scaler_joblib.pkl']
    elif model_loaded_type == 'pickle':
        model_names = ['model.pkl', 'preprocessor.pkl', 'scaler.pkl']
    else:
        raise ValueError("Unsupported model_loaded_type. Use 'joblib' or 'pickle'.")

    # Load the prediction model and preprocessing components
    predict_model, one_hot_encoder, scaler = load_model(*model_names)

    # Convert input data to DataFrame
    raw_features = pd.DataFrame([data])

    # Preprocess input data: encode and scale features
    encoded_features = one_hot_encoder.transform(raw_features)
    final_feature = scaler.transform(encoded_features)

    # Generate prediction
    prediction = predict_model.predict(final_feature)

    return prediction
