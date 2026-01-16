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
        "married": [True, False, None, None, True],
        "job": [None, None, None, None, None]
    })

@pytest.mark.parametrize(
    "col, threshold, expected_out",
    [
        ("age", 0.25, True), #below threshold
        ("sex", 0.0, True), #exactly at the threshold, col with no missing values
        ("sex", 0, True), #exactly at the threshold, col with no missing values with int
        (0, 0.25, False), # above threshold, int col  for "name"
        ("age", 0.20, True), # exactly at the threshold
        ("married", 0.39, False), # just right above the threshold
        (4, 0.99, False), # edge just below threshold, int col for "job"
        ("job", 1.0, True), # edge at exact threshold
        (2, 1, True) # edge at exact threshold with int
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
    with pytest.raises(KeyError, match="Column is not found in the Dataframe."):
        missing_values_validate(sample_dataframe, "1", 0.23)
    with pytest.raises(KeyError, match="Column is not found in the Dataframe."):
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
    with pytest.raises(ValueError, match="Threshold is invalid: negative threshold"):
        missing_values_validate(sample_dataframe, "name", -1)
    with pytest.raises(ValueError, match="Threshold is invalid: larger than 1"):
        missing_values_validate(sample_dataframe, "age", 2)


@pytest.mark.parametrize(
    "df, col, threshold, error_str",
    [
        ({"name": ["Alex"]}, "name", 0.05, "Input 1 must be a pandas Dataframe"), # invalid input 1 not pd Dataframe
        (pd.DataFrame(), 0, 0.05, "Input 1 must be a pandas Dataframe"), # invalid input 1 empty DataFrame
        (None, 1, 0.2, "Input 1 must be a pandas Dataframe"), # invalid input 1 empty DataFrame
        (pd.DataFrame({"name": ["Alex", None, None, "Austin", None]}), 
         ["1", "name"], 0.1, "Input 2 must be a string or integer"), # invalid input 2 list
        (pd.DataFrame({"name": ["Alex", None, None, "Austin", None]}), 
         None, 0.1, "Input 2 must be a string or integer"), # invalid input 2 None
        (pd.DataFrame({"name": ["Alex", None, None, "Austin", None]}), 
         0.2, 0.12, "Input 2 must be a string or integer"), # invalid input 2 float instead of int
        (pd.DataFrame({"age": [21, 43, 23, None, 38]}), 
         "age", "0.20", "Input 3 must be numeric"), #invalid input 3 string
        (pd.DataFrame({"age": [21, 43, 23, None, 38]}), 
         "age", None, "Input 3 must be numeric"), #invalid input 3 None
    ]
)

def test_missing_values_validate_invalid_input_type(df, col, threshold, error_str):
    """
    Test that missing_values_validate raises exception for inputs with incorrect data types.
    """
    with pytest.raises(TypeError, match=error_str):
        missing_values_validate(df, col, threshold)
