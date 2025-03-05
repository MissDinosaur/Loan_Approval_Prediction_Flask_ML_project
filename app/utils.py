integer_column = ["Age", "Credit Score", "Previous Defaults", "Years at Current Job"]
float_column = ["Income", "Debt-to-Income Ratio", "Loan Amount", "Assets Value"]
str_colun = ["Employment Status"]

def cast_to_actual_types(original_dict: dict[str, str]):
    features_dict = {}
    
    for k, v in original_dict.items():
        if k in integer_column:
            features_dict[k] = int(v)
        if k in float_column:
            features_dict[k] = float(v)
        if k in str_colun:
            features_dict[k] = str(v)

    return features_dict   