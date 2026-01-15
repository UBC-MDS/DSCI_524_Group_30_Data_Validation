def missing_values_validate(df: pd.DataFrame, col: str, threshold: float) -> bool:
    """
    Validate the amount of missing values in a pandas dataframe.

    This function checks whether the given column in the pandas
    dataframe has missing values at or below the given threshold.

    Parameters
    ----------
    df : pd.DataFrame
        the pandas dataframe containing missing values.
    col : str
        the column containing missing values to validate.
    threshold : float
        the decimal threshold of missing values that is acceptable to check.
        So 0.20 for threshold means only 20% or lower of the observations in
        the column that are allowed to be missing.

    Returns
    -------
    bool 
        return True if the proportion of missing values is at or below
        the threshold, otherwise return False

    Raises
    ------
    TypeError
        If df is None or not a pandas DataFrame or
        if threshold is not numeric (float) or
        if col is not a string.
    KeyError
        If col does not exist in the dataframe.
    ValueError
        If threshold is not between 0.0 and 1.0.


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
