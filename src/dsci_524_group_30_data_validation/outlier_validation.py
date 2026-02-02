import pandas as pd


def outliers_validate(
    dataframe: pd.DataFrame,
    *,
    col: str,
    lower_bound: float,
    upper_bound: float,
    threshold: float,
) -> str:
    """
    Validates that a DataFrame column contains an acceptable proportion
    of values outside a user-defined range.

    This function checks whether the proportion of non-missing values in the
    specified column that fall outside the interval [`lower_bound`, `upper_bound`]
    is less than or equal to the given `threshold`.

    Outliers are defined as values strictly less than `lower_bound` or strictly
    greater than `upper_bound`. Values equal to the bounds are not considered
    outliers. Missing values (NaN) are ignored when calculating the outlier
    proportion.

    All arguments except `dataframe` are keyword-only.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The DataFrame containing the data to validate.

    col : str
        Name of the column in which outliers will be identified.

    lower_bound : float
        The lower bound of the acceptable value range.

    upper_bound : float
        The upper bound of the acceptable value range.

    threshold : float
        The maximum acceptable proportion of outliers (between 0 and 1).

    Returns
    -------
    str
        A message stating whether the outlier proportion is within the
        acceptable threshold.

        If the outlier proportion is less than or equal to `threshold`, the
        function returns:

        "The proportion of outliers is within the acceptable threshold. Check complete!"

        Otherwise, it returns:

        "The proportion of outliers exceeds the threshold {threshold}. Check complete!"

    Raises
    ------
    TypeError
        If `dataframe` is not a pandas DataFrame.

    ValueError
        If `col` is not found in the DataFrame.
        If `lower_bound` is greater than or equal to `upper_bound`.
        If `threshold` is not between 0 and 1 (inclusive).
        If the column contains no non-missing values.

    Notes
    -----
    - Outliers are values strictly outside the interval
      (`lower_bound`, `upper_bound`).
    - Missing values are ignored when calculating the outlier proportion.
    - This function requires keyword arguments for `col`, `lower_bound`,
      `upper_bound`, and `threshold`.

    Examples
    --------
    Example where outlier proportion is within the threshold:

    >>> import pandas as pd
    >>> df = pd.DataFrame({"age": [25, 32, 41, 29, 200]})
    >>> outliers_validate(
    ...     dataframe=df,
    ...     col="age",
    ...     lower_bound=0,
    ...     upper_bound=100,
    ...     threshold=0.20
    ... )
    'The proportion of outliers is within the acceptable threshold. Check complete!'

    Example where outlier proportion exceeds the threshold:

    >>> df = pd.DataFrame({"score": [10, 12, 999, 11, 1000]})
    >>> outliers_validate(
    ...     dataframe=df,
    ...     col="score",
    ...     lower_bound=0,
    ...     upper_bound=100,
    ...     threshold=0.10
    ... )
    'The proportion of outliers exceeds the threshold 0.1. Check complete!'
    """

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("dataframe must be a pandas DataFrame")

    if col not in dataframe.columns:
        raise ValueError(f"Column '{col}' not found in DataFrame")

    if lower_bound >= upper_bound:
        raise ValueError("lower_bound must be less than upper_bound")

    if not (0 <= threshold <= 1):
        raise ValueError("threshold must be between 0 and 1")

    values = dataframe[col].dropna()

    if values.empty:
        raise ValueError(f"Column '{col}' contains no non-missing values")

    outliers = (values < lower_bound) | (values > upper_bound)
    outlier_proportion = outliers.mean()

    if outlier_proportion <= threshold:
        return "The proportion of outliers is within the acceptable threshold. Check complete!"

    return (
        f"The proportion of outliers exceeds the threshold {threshold}. Check complete!"
    )
