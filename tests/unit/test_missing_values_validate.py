import pytest
import os
import sys
import pandas as pd
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dsci_524_group_30_data_validation.missing_values_validate import missing_values_validate


@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        "name": ["Alex", None, None, "Austin", None],
        "age": [21, 43, 23, None, 38],
        "sex": ["M", "F", "F", "M", "F"],
        "married": [True, False, None, None, True]
    })

@pytest.mark.parametrize(
    "col, threshold, expected_out",
    [
        ("sex", 0.05, True), #below threshold
        ("name", 0.25, False), # above threshold
        ("age", 0.20, True), # exactly at the threshold
        ("married", 0.39, False), # just right above the threshold
    ]
)

@pytest.mark.parametrize(
    "df, col, threshold, error_str",
    [
        ({"name": ["Alex"]}, "name", 0.05, "Input 1 must be a pandas Dataframe"),
        (sample_dataframe, 1, 0.1, "Input 2 must be a string"),
        (sample_dataframe, "age", "0.20", "Input 3 must be numeric"),
        (["Alex", None], ["name"], {"1": 0.05}, "Input 1 must be a pandas Dataframe."),
    ]
)

def test_missing_values_validate(sample_dataframe, col, threshold, expected_out):
    """
    Test that missing_values_validate works as expected for example below,
     above, and at exact the threshold.
    """
    out = missing_values_validate(sample_dataframe, col, threshold)
    assert  expected_out == out, f"Expected {expected_out} but got {out}"

def test_missing_values_validate_invalid_col(sample_dataframe):
    """
    Test that missing_values_validate raises exception for column not found in dataframe.
    """
    with pytest.raises(KeyError, match="Column is not found in the dataframe."):
        missing_values_validate(sample_dataframe, "1", 0.23)
    with pytest.raises(KeyError, match="Column is not found in the dataframe."):
        missing_values_validate(sample_dataframe, "", 0.23)

def test_missing_values_validate_invalid_threshold(sample_dataframe):
    """
    Test that missing_values_validate raises exception for invalid threshold.
    Threshold must be >= 0 and <= 1
    """
    with pytest.raises(ValueError, match="Threshold is invalid: negative threshold"):
        missing_values_validate(sample_dataframe, "name", -0.01)
    with pytest.raises(ValueError, match="Threshold is invalid: larger than 1"):
        missing_values_validate(sample_dataframe, "age", 1.01)

def test_missing_values_validate_invalid_input_type(df, col, threshold, error_str):
    """
    Test that missing_values_validate raises exception for inputs with incorrect data types.
    """
    with pytest.raises(TypeError, match=error_str):
        missing_values_validate(df, col, threshold)
    with pytest.raises(AttributeError, match="Dataframe cannot be None."):
        missing_values_validate(None, "age", 0.2)





