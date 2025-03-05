integer_column = ["Age", "Credit Score", "Previous Defaults", "Years at Current Job", "Assets Value"]
float_column = ["Income", "Debt-to-Income Ratio", "Loan Amount"]
str_column = ["Employment Status"]

def cast_to_actual_types(original_dict: dict[str, str]):
    features_dict = {}

    for k, v in original_dict.items():
        if v in ["", None]:  # Handle empty values gracefully
            features_dict[k] = None
            continue

        try:
            if k in integer_column:
                v = float(v)  # Convert to float first (to handle '0.1')
                features_dict[k] = round(v)
            elif k in float_column:
                features_dict[k] = float(v)  # Convert to float safely
            elif k in str_column:
                features_dict[k] = str(v)
        except ValueError:
            print(f"Warning: Could not convert {v} for key '{k}'")  # Debugging
            features_dict[k] = None  # Assign None for problematic values

    return features_dict
