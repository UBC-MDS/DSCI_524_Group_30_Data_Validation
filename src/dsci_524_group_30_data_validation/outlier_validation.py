def outliers_validate(
    dataframe: pd.DataFrame,
    *,
    col: str,
    lower_bound: float,
    upper_bound: float,
    threshold: float,
):
    """
    Validates that a DataFrame column contains an acceptable proportion
    of values outside a user-defined range.

    This function performs validation checks to ensure that the proportion
    of values in the specified column that fall outside the given lower
    and upper bounds does not exceed the specified threshold.
    Keyword arguments are required.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The DataFrame containing the data to validate.

    col : str
        The column in which outliers will be identified.

    lower_bound : float
        The lower bound of the acceptable value range.

    upper_bound : float
        The upper bound of the acceptable value range.

    threshold : float
        The maximum acceptable proportion of outliers (between 0 and 1).

    Returns
    -------
    str
        Message which either confirms that the proportion of outliers is
        within the acceptable threshold, or reports that the threshold
        has been exceeded.

    Notes
    -------
        Keyword arguments are required for all parameters except
        the dataframe.

        Validation results are returned as a string.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "age": [18, 22, 25, 30, 120]
    ... })
    >>> outliers_validate(
    ...     dataframe=df,
    ...     col="age",
    ...     lower_bound=18,
    ...     upper_bound=65,
    ...     threshold=0.2,
    ... )
    "The proportion of outliers is within the acceptable threshold. Check complete!"
    """
    pass
