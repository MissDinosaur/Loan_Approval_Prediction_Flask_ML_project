# Flask backend routes
from flask import render_template, request
from ml import predict 
from app import app  # Import Flask app from __init__.py


integer_column = ["Age", "Credit Score", "Previous Defaults", "Years at Current Job"]
float_column = ["Income", "Debt-to-Income Ratio", "Loan Amount"]
str_colun = ["Payment History", "Employment Status"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict_loan_approval():
    #features = [float(request.form[x]) for x in important_columns]

    request_data = request.form  # dict[str, str]
    features_dict = {}
    
    for k, v in request_data.items():
        if k in integer_column:
            features_dict[k] = int(v)
        if k in float_column:
            features_dict[k] = float(v)
        if k in str_colun:
            features_dict[k] = str(v)
        
    # Make prediction
    prediction = predict.predict(features_dict)

    # Interpret prediciton
    result = ''
    if prediction == 0:
        result = 'Approved'
    else:
        result = 'Rejected'

    return render_template('result.html', prediction_text=f'The client is {result} for the loan application')

#if __name__ == '__main__':
#    app.run(debug=True)