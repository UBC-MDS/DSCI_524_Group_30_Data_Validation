def missing_values_validate(df: pd.DataFrame, col: str | int, threshold: float | int) -> bool:
    """
    Validate the amount of missing values in a pandas DataFrame.

    This function checks whether the given column in the pandas
    DataFrame has missing values at or below the given threshold.

    Parameters
    ----------
    df : pd.DataFrame
        the pandas DataFrame containing missing values.
    col : str or int
        the column name (str) or index (int) containing missing values to validate.
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
        if col is not a string or an integer.
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
