def missing_values_validate(df: pd.Dataframe, col: str, threshold: float):
    """
    Validate the amount of missing values in a pandas dataframe.

    This function checks whether the given column in the pandas
    dataframe has missing values at or below the given threshold.

    Parameters
    ----------
    df : pd.Dataframe
        the pandas dataframe containing missing values.
    col : str
        the column containing missing values to validate.
    threshold : float
        the decimal threshold of missing values that is acceptable to check.

    Returns
    -------
    str 
        A message confirmation if the check is validated or not.
        Return "The amount of missing values are valid" if the missing values 
        check is at the given threshold or lower. Otherwise, return "The amount 
        of missing values exceeds the threshold {threshold value}".

    Examples
    --------
    >>> import pandas as pd
    >>> data = pd.DataFrame({
            "name": ["Alex", NA, NA, "Austin", NA]
            "age": [21, 43, 23, NA, 38]
            "sex": ["M", "F", "F", "M", "F"]})
    >>> missing_values(df=data, col="age", threshold=0.25)
    "The amount of missing values are valid"
    "Checks completed!"
    """