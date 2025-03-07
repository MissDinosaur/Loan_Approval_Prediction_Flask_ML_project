# Flask + ML Project

## Project Overview

Description of project purpose and usage.



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

- **Data Proccess**: Scikit-learn, pandas
- **Machine Learning**: Scikit-learn, joblib, pickle
- **Backend**: flask, flask-caching
- **Fronend**: HTML(Jinja2)
- **Deployment**: 


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

## Deploying the Project