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

def test_missing_values_validate():
    """
    Test that missing_values_validate works as expected for example below,
     above, and at exact the threshold.
    """

def test_missing_values_validate_invalid_col():
    """
    Test that missing_values_validate raises exception for column not found in dataframe.
    """

def test_missing_values_validate_invalid_threshold():
    """
    Test that missing_values_validate raises exception for invalid threshold.
    Threshold must be >= 0 and <= 1
    """

def test_missing_values_validate_invalid_input_type():
    """
    Test that missing_values_validate raises exception for inputs with incorrect data types.
    """





