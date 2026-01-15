# Testing the str_validate function
import pandas as pd
import pytest
from dsci_524_group_30_data_validation.str_validate import categorical_validate

@pytest.fixture
def full_df():
    """Comprehensive dataframe with multiple column types."""
    return pd.DataFrame({
        "gender": ["M", "F", "F", "M", "F", "M", "M", "F", "F", "M"],
        "city": ["Vancouver", "Toronto", "Toronto", "Calgary", "Vancouver",
                 "Calgary", "Toronto", "Vancouver", "Calgary", "Toronto"],
        "education": ["HS", "College", "University", "HS", "University",
                      "College", "HS", "University", "College", "HS"],
        "age": [23, 35, 29, 42, 31, 27, 38, 26, 34, 45],
        "income": [45000, 72000, 68000, 81000, 75000,
                   62000, 79000, 56000, 71000, 85000]
    })

def test_data_type(full_df):  
    """Test that non-string categorical columns raise TypeError."""
    with pytest.raises(TypeError, match="categorical|string"):
        categorical_validate(dataframe=full_df, column="income", num_cat=10)

def test_num_cat_positive(full_df):
    """Test that negative num_cat raises ValueError."""
    with pytest.raises(ValueError):
        categorical_validate(dataframe= full_df, column = "city", num_cat = -10)

def test_column_not_exists(full_df):
    """Test that non-existent column raises KeyError."""
    with pytest.raises(KeyError, match="fruit|column"):
        categorical_validate(full_df, column="fruit", num_cat=3)

def test_num_cat_correct(full_df):   
    result = categorical_validate(full_df, column="city", num_cat=3)
    assert result == "Checks completed!"

def test_invalid_dataframe_type():
    """Test that non-DataFrame input raises TypeError."""
    not_a_df = {"city": ["Vancouver", "Toronto"]}
    
    with pytest.raises(TypeError, match="DataFrame"):
        categorical_validate(not_a_df, column="city", num_cat=2)

def test_invalid_column_type(full_df):
    """Test that non-string column name raises TypeError."""  
    with pytest.raises(TypeError, match="string|str"):
        categorical_validate(full_df, column=123, num_cat=2)