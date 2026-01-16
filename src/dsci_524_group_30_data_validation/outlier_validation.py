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

    This function performs validation checks to ensure that the proportion
    of values in the specified column that fall outside the given lower
    and upper bounds does not exceed the specified threshold.
    Keyword arguments are required.

    Outliers are defined as values strictly less than `lower_bound` or strictly
    greater than `upper_bound`. Values equal to the bounds are not considered
    outliers. Missing values (NaN) are ignored when calculating the outlier
    proportion.

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

    Raises
    ------
    TypeError
        If `dataframe` is not a pandas DataFrame.
    ValueError
        If `col` is not in the DataFrame, if `lower_bound` is not less than
        `upper_bound`, if `threshold` is not between 0 and 1, or if the column
        contains no non-missing values.
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

    return f"The proportion of outliers exceeds the threshold {threshold}. Check complete!"
