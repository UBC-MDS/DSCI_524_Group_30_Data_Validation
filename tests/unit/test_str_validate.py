# Testing the str_validate function
import pandas as pd
import pytest
from dsci_524_group_30_data_validation.str_validate import categorical_validate

def test_data_type():
    df = pd.DataFrame({
    "income": [45000, 72000, 68000, 81000, 75000,
               62000, 79000, 56000, 71000, 85000]
    })
    
    with pytest.raises(TypeError, match="categorical|string"):
        categorical_validate(dataframe=df, column="income", num_cat=10)

def test_num_cat_positive():
    df = pd.DataFrame({
    "gender": ["M", "F", "F", "M", "F", "M", "M", "F", "F", "M"],
    "city": ["Vancouver", "Toronto", "Toronto", "Calgary", "Vancouver",
             "Calgary", "Toronto", "vancouver", "Calgary", "Toronto"],
    "education": ["HS", "College", "University", "HS", "University",
                  "College", "HS", "University", "College", "HS"],
    "age": [23, 35, 29, 42, 31, 27, 38, 26, 34, 45],
    "income": [45000, 72000, 68000, 81000, 75000,
               62000, 79000, 56000, 71000, 85000]
    })
    with pytest.raises(ValueError):
        categorical_validate(df, column = "city", num_cat = -10)

def test_column_exists():
    df = pd.DataFrame({
    "gender": ["M", "F", "F", "M", "F", "M", "M", "F", "F", "M"],
    "city": ["Vancouver", "Toronto", "Toronto", "Calgary", "Vancouver",
             "Calgary", "Toronto", "vancouver", "Calgary", "Toronto"],
    })

    with pytest.raises(ValueError):
        categorical_validate(df, column = "fruit", num_cat = 3)
