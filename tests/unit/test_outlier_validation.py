"""
Unit tests for `outliers_validate`.

These tests cover key edge cases based on the function specification:
- valid case with no outliers
- valid case when outlier proportion equals threshold
- invalid case when outlier proportion exceeds threshold
- invalid inputs (missing column, invalid threshold)
"""
import pandas as pd
import pytest

from dsci_524_group_30_data_validation.outlier_validation import outliers_validate

def test_outliers_validate_no_outliers_valid():
    """
    Test that the function returns a success message when there are no outliers
    and the threshold is 0.
    """
    df = pd.DataFrame({"age": [18, 20, 30, 40, 65]})
    result = outliers_validate(
        dataframe=df,
        col="age",
        lower_bound=18,
        upper_bound=65,
        threshold=0.0,
    )
    assert result == "The proportion of outliers is within the acceptable threshold. Check complete!"

def test_outliers_validate_outliers_equal_threshold_valid():
    """
    Test that the function returns a success message when the outlier proportion
    is exactly equal to the threshold.
    """
    df = pd.DataFrame({"age": [18, 20, 30, 40, 120]})  # 1 outlier / 5 = 0.2
    result = outliers_validate(
        dataframe=df,
        col="age",
        lower_bound=18,
        upper_bound=65,
        threshold=0.2,
    )
    assert result == "The proportion of outliers is within the acceptable threshold. Check complete!"
def test_outliers_validate_outliers_exceed_threshold_invalid():
    """
    Test that the function returns a failure message when the outlier proportion
    exceeds the given threshold.
    """
    df = pd.DataFrame({"age": [10, 20, 30, 40, 120]})  # 2 outliers / 5 = 0.4
    result = outliers_validate(
        dataframe=df,
        col="age",
        lower_bound=18,
        upper_bound=65,
        threshold=0.2,
    )
    assert result == "The proportion of outliers exceeds the threshold 0.2. Check complete!"


def test_outliers_validate_missing_column_raises():
    """
    Test that a ValueError is raised when the specified column does not exist
    in the DataFrame.
    """
    df = pd.DataFrame({"age": [18, 20, 30]})
    with pytest.raises(ValueError, match="Column 'height' not found"):
        outliers_validate(
            dataframe=df,
            col="height",
            lower_bound=0,
            upper_bound=100,
            threshold=0.2,
        )


def test_outliers_validate_invalid_threshold_raises():
    """
    Test that a ValueError is raised when the threshold is outside [0, 1].
    """
    df = pd.DataFrame({"age": [18, 20, 30]})
    with pytest.raises(ValueError, match="threshold must be between 0 and 1"):
        outliers_validate(
            dataframe=df,
            col="age",
            lower_bound=0,
            upper_bound=100,
            threshold=1.5,
        )
def test_outliers_validate_all_nan_column_raises():
    """
    Test that a ValueError is raised when the specified column contains only
    missing values (no non-missing values to validate).
    """
    df = pd.DataFrame({"x": [None, None, None]})
    with pytest.raises(ValueError, match="contains no non-missing values"):
        outliers_validate(
            dataframe=df,
            col="x",
            lower_bound=0,
            upper_bound=10,
            threshold=0.2,
        )


def test_outliers_validate_invalid_bounds_equal_raises():
    """
    Test that a ValueError is raised when lower_bound equals upper_bound.
    """
    df = pd.DataFrame({"x": [1, 2, 3]})
    with pytest.raises(ValueError, match="lower_bound must be less than upper_bound"):
        outliers_validate(
            dataframe=df,
            col="x",
            lower_bound=5,
            upper_bound=5,
            threshold=0.2,
        )
def test_outliers_validate_non_dataframe_raises():
    """
    Test that a TypeError is raised when the input is not a pandas DataFrame.
    """
    with pytest.raises(TypeError, match="dataframe must be a pandas DataFrame"):
        outliers_validate(
            dataframe=[1, 2, 3],
            col="x",
            lower_bound=0,
            upper_bound=10,
            threshold=0.2,
        )