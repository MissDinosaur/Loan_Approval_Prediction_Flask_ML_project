"""
Data Type Casting Module

This module provides utilities for casting data to their appropriate types.

Functionality:
    - `cast_to_actual_types`: Converts string representations of data into
      their appropriate types (int, float, or str) based on predefined columns.

Columns:
    - Integer Columns: Age, Credit Score, Previous Defaults, Years at Current
      Job, Assets Value
    - Float Columns: Income, Debt-to-Income Ratio, Loan Amount
    - String Columns: Employment Status

Dependencies:
    - Python Standard Library: No external dependencies required.
"""


# Column categories for type casting
integer_column = ["Age", "Credit Score", "Previous Defaults",
                  "Years at Current Job", "Assets Value"]
float_column = ["Income", "Debt-to-Income Ratio", "Loan Amount"]
str_column = ["Employment Status"]


def cast_to_actual_types(original_dict: dict[str, str]) -> dict:
    """
    Cast input dictionary values to their respective data types.

    This function iterates over the provided dictionary and converts values
    to integers, floats, or strings based on predefined column categories.

    Parameters:
        original_dict (Dict[str, str]): Input dictionary with string values.

    Returns:
        Dict[str, Any]: Dictionary with values cast to appropriate data types.

    Example:
     >>> cast_to_actual_types({"Age": "25", "Income": "45000.5",
                                "Employment Status": "Employed"})
        {"Age": 25, "Income": 45000.5, "Employment Status": "Employed"}
    """
    features_dict = {}

    for k, v in original_dict.items():
        if v in ["", None]:  # Handle empty or missing values gracefully
            features_dict[k] = None
            continue

        try:
            if k in integer_column:
                v = float(v)  # Convert to float first to handle cases like '0.1'
                features_dict[k] = round(v)
            elif k in float_column:
                features_dict[k] = float(v)  # Convert to float safely
            elif k in str_column:
                features_dict[k] = str(v)  # Ensure string type
            else:
                features_dict[k] = v  # Keep as-is for unlisted columns
        except ValueError:
            print(f"Warning: Could not convert value '{v}' for key '{k}'")
            features_dict[k] = None  # Assign None for problematic values

    return features_dict
