# Flask + ML Project

## Project Overview

Loan Approval Prediction Model
This project implements a machine learning model to predict whether a loan application should be approved or denied based on financial risk assessment data. The model is built using logistic regression and includes data preprocessing, feature engineering, model training, evaluation, and prediction capabilities.



## Project Architecture

```plaintext
Loan_Approval_Prediction_Flask_ML_project/
│── app/                    # Core frontend and backend code for the Flask application
│   ├── templates/          # Frontend HTML templates
│   │   ├── index.html      # Home Page
│   │   ├── input.html      # User Input Page
│   │   ├── result.html     # Prediction Result Page
│   ├── __init__.py         # Initialize falsk app and set up configs
│   ├── routes.py           # ⭐ Main backend logic (Flask request handling & ML interaction)
│   ├── utils.py            # Utility functions
|
│── ml/                     # Machine learning module (data, training & prediction, models)
│   ├── data_source/        # Data source
│   │   ├── financial_risk_assessment.csv
│   ├── models/             # ML model and data processors
│   ├── loan_approval_model.ipynb    # Data processing, model training and model saving
│   ├── predict.py          # Predict function, loading and invoking the models
|
│── tests/                  # Test code
│   ├── test_predict.py
│   ├── test_routes.py      
│   ├── test_utils.py       
│── main.py                 # Flask entry point (run the backend server)
│── requirements.txt        # Dependency list
│── config.py               # Configuration file
│── README.md               # Project documentation
```

## Technologies Used

<<<<<<< Updated upstream
- **Data Proccess**: Scikit-learn, pandas
- **Machine Learning**: Scikit-learn, joblib, pickle
- **Backend**: flask, flask-caching
- **Fronend**: HTML(Jinja2)
- **Deployment**: 
=======
- **Data Proccess**: Scikit-learn, pandas, NumPy, Matplotlib
- **Machine Learning**: Scikit-learn, joblib, SciPy, pickle
- **Backend**: flask, flask_caching
- **Fronend**: HTML
- **Deployment**: Deployed on pythonanywhere.
>>>>>>> Stashed changes


### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-folder-name>
   ```

2. Create a virtual environment named <venvName> (Recommended Python version=3.11.0):
   ```bash
   python -m venv <venvName>  # Replace <venvName> by your venv name 
   ```

3. Activate the virtual environment <venvName>:
   ```bash
   # Replace <venvName> by your venv name 

   # Windows (CMD/Powershell)
   <venvName>\Scripts\activate

   # Windows (git bash)
   source <venvName>/Scripts/activate

   # macOS/Linux
   source <venvName>/bin/activate

   # if you wanna quit the current virtual environment
   deactivate
   ```

4. Install the dependencies (Recommended Python version=3.11.0):
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. Trigger this Flask server:
   ```bash
   python main.py
   ```

2. Open the app in your browser:
   ```bash
   http://127.0.0.1:5000/index
   ```

Features of the prediction model:

1. Data Preprocessing: Handles missing values, encodes categorical variables, and scales numerical features.
2. Data Visualization: Generates histograms and box plots to explore feature distributions and detect outliers.
3. Outlier Detection: Uses z-scores to identify outliers in numerical columns.
4. Feature Engineering: Simulates a target variable (Loan_Approval) based on logical rules applied to the dataset.
5. Model Training: Trains a logistic regression model on preprocessed data.
6. Prediction: Allows predictions on new data using the trained model.
7. Model Persistence: Saves the trained model and preprocessing objects using joblib for future use.

Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/loan-approval-prediction.git
   cd loan-approval-prediction
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. The requirements.txt file should include:
   1. pandas
   2. numpy
   3. scikit-learn
   4. matplotlib
   5. scipy
   6. joblib

Dataset:
   1. Source: The dataset used is financial_risk_assessment.csv, containing financial details of loan applicants.
   2. Preprocessing:
      1. Missing values are filled with the mode for categorical columns and the median for numerical columns.
      2. Categorical variables (e.g., Employment Status) are one-hot encoded.
      3. Numerical features are scaled using StandardScaler.

Model Details:
   1. Model Type: Logistic Regression
   2. Features Used:
      Age, Income, Credit Score, Loan Amount, Employment Status, Years at Current Job, Debt-to-Income Ratio, Assets Value, Previous Defaults
   3. Target Variable: Loan_Approval (1 for approved, 0 for denied)
   4. Preprocessing:
      1. One-hot encoding for categorical variables.
      2. Standard scaling for numerical variables.
   5. Evaluation Metrics:
      1. Accuracy
      2. Precision, Recall, F1-Score (via classification report)

## Deploying the Project