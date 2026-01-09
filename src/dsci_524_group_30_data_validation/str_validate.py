def validate_dataframe(df, schema):
    """
    Validate a DataFrame against a schema definition.
    
    Checks that specified columns exist and have only allowed values.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to validate.
    schema : dict
        Dictionary defining validation rules for each column. Keys are column
        names (str), values are dictionaries with the following optional keys:
        
        - 'dtype' : type
            Expected data type (e.g., str, int, float). Currently only validates
            str type explicitly.
        - 'allowed_values' : list
            List of permitted values for the column. Any value not in this list
            will be flagged as invalid.
        - 'nullable' : bool, default False
            Whether the column can contain null/NaN values.
    
    Returns
    -------
    bool
        True if validation passes.
    
    Raises
    ------
    ValueError
        If any validation checks fail. The error message contains a newline-separated
        list of all validation failures found.
    
    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'status': ['Active', 'Inactive', 'Active'],
    ...     'category': ['A', 'B', 'A']
    ... })
    >>> schema = {
    ...     'status': {
    ...         'dtype': str,
    ...         'allowed_values': ['Active', 'Inactive', 'Pending'],
    ...         'nullable': False
    ...     },
    ...     'category': {
    ...         'dtype': str,
    ...         'allowed_values': ['A', 'B', 'C']
    ...     }
    ... }
    >>> validate_dataframe(df, schema)
    True
    
    >>> df_invalid = pd.DataFrame({
    ...     'status': ['Active', 'Invalid', None],
    ...     'category': ['A', 'D', 'A']
    ... })
    >>> validate_dataframe(df_invalid, schema)
    Traceback (most recent call last):
        ...
    ValueError: status: Contains null values
    status: Invalid values: {'Invalid'}
    category: Invalid values: {'D'}
    
    Notes
    -----
    - Missing columns in the schema are not validated
    - Extra columns in the DataFrame are ignored
    - For 'dtype' validation, only str type is explicitly checked
    - Null values are dropped before checking allowed_values
    """
    errors = []
    
    for col, rules in schema.items():
        if col not in df.columns:
            errors.append(f"Missing column: {col}")
            continue
        
        series = df[col]
        
        # Check nulls
        if not rules.get('nullable', False) and series.isna().any():
            errors.append(f"{col}: Contains null values")
        
        # Check allowed values
        if 'allowed_values' in rules:
            allowed = set(rules['allowed_values'])
            actual = set(series.dropna().unique())
            invalid = actual - allowed
            if invalid:
                errors.append(f"{col}: Invalid values: {invalid}")
        
        # Check dtype
        if 'dtype' in rules:
            expected_type = rules['dtype']
            non_null = series.dropna()
            if len(non_null) > 0:
                if expected_type == str:
                    if not all(isinstance(x, str) for x in non_null):
                        errors.append(f"{col}: Not all values are strings")
    
    if errors:
        raise ValueError("\n".join(errors))
    
    return True