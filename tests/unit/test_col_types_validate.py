import pandas as pd
import pytest
from dsci_524_group_30_data_validation.col_types_validate import col_types_validate


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "city": ["Vancouver", "Toronto", "Calgary", "Winnipeg"],
            "name": ["John Smith", "Bron Crift", "Pylon Gift", "Akon Sarmist"],
            "gender": ["M", "F", "F", "M"],
            "age": [25, 32, 41, 29],
        }
    )


def test_col_types_validate_count_based_success(sample_df):
    """
    Test that count-based validation succeeds when expected column counts match.
    """
    result = col_types_validate(
        dataframe=sample_df,
        integer_cols=1,
        text_cols=3,
    )

    assert isinstance(result, str)
    assert "Check complete" in result


def test_col_types_validate_schema_success(sample_df):
    """
    Test that schema-based validation succeeds when column types match expectations.
    """
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={"age": "integer", "city": "text", "name": "text"},
    )

    assert isinstance(result, str)
    assert "Check complete" in result


def test_col_types_validate_schema_type_mismatch(sample_df):
    """
    Test that schema-based validation reports an error when a column has the wrong type.
    """
    result = col_types_validate(dataframe=sample_df, column_schema={"age": "text"})

    assert isinstance(result, str)
    assert "Column 'age' expected type 'text'" in result
