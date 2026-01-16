import pandas as pd

def missing_values_validate(df: pd.DataFrame, col: str, threshold: float | int) -> bool:
    """
    Validate the amount of missing values in a pandas DataFrame.

    This function checks whether the given column in the pandas
    DataFrame has missing values at or below the given threshold.

    Parameters
    ----------
    df : pd.DataFrame
        the pandas DataFrame containing missing values.
    col : str
        the column name (str) containing missing values to validate.
    threshold : float or int
        the decimal threshold of missing values that is acceptable to check.
        Must be between 0 and 1 (inclusive). For instance, 0.20 for threshold 
        means only 20% or lower of the observations are allowed to be missing. 

    Returns
    -------
    bool 
        True if the proportion of missing values is at or below
        the threshold, otherwise False.

    Raises
    ------
    TypeError
        If df is None or not a pandas DataFrame or
        if threshold is not numeric (float or int) or
        if col is not a string.
    KeyError
        If col does not exist in the dataframe.
    ValueError
        If threshold is not between 0.0 and 1.0 (inclusive) 


    Examples
    --------
    >>> import pandas as pd
    >>> data = pd.DataFrame({
            "name": ["Alex", None, None, "Austin", None],
            "age": [21, 43, 23, None, 38],
            "sex": ["M", "F", "F", "M", "F"],
            "married": [True, False, None, None, True]})
    >>> missing_values_validate(df=data, col="age", threshold=0.25)
    True
    >>> missing_values_validate(df=data, col="name", threshold=0.05)
    False
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input 1 must be a pandas Dataframe")

    if not isinstance(col, (str, int)):
        raise TypeError("Input 2 must be a string or integer")
    
    if not isinstance(threshold, (float, int)):
        raise TypeError("Input 3 must be numeric")
    
    if threshold < 0:
        raise ValueError("Threshold is invalid: negative threshold")
    
    if threshold > 1:
        raise ValueError("Threshold is invalid: larger than 1")
    
    if df.empty:
        raise ValueError("Dataframe cannot be empty")
    
    try:
        na_frac = df[col].isna().mean()
    except KeyError:
        raise KeyError("Column is not found in the Dataframe")

    if na_frac <= threshold:
        print("The amount of missing values are valid. Checks completed!")
        return True
    else:
        print(f"Invalid check: the amount of missing values is {na_frac}, exceeding the threshold: {threshold}. Checks completed!")
        return False
