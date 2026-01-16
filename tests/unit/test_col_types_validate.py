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
    Test that count-based column type validation succeeds when expected counts are correct.
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
    Test that schema-based validation succeeds when specified column types match the DataFrame.
    """
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={"age": "integer", "city": "text", "name": "text"},
    )

    assert isinstance(result, str)
    assert "Check complete" in result


def test_col_types_validate_schema_type_mismatch(sample_df):
    """
    Test that schema-based validation returns an informative error when a column has the wrong type.
    """
    result = col_types_validate(dataframe=sample_df, column_schema={"age": "text"})

    assert isinstance(result, str)
    assert "Column 'age' expected type 'text'" in result


def test_schema_missing_column(sample_df):
    """
    Test that schema validation reports a clear error when a referenced column is missing from the DataFrame.
    """
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={"salary": "integer"},
    )

    assert isinstance(result, str)
    assert "Column 'salary' not found" in result


def test_schema_invalid_logical_type(sample_df):
    """
    Test that schema validation reports an error when an unsupported logical type is provided.
    """
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={"age": "date"},
    )

    assert isinstance(result, str)
    assert "Unsupported logical type" in result


def test_empty_column_schema(sample_df):
    """
    Test that providing an empty column schema is treated as invalid input.
    """
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={},
    )

    assert isinstance(result, str)
    assert "column_schema cannot be empty" in result


def test_multiple_schema_errors(sample_df):
    """
    Test that schema validation reports all detected column type mismatches in a single run.
    """
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={
            "age": "text",  # wrong
            "city": "integer",  # wrong
        },
    )

    assert isinstance(result, str)
    assert "Column 'age' expected type 'text'" in result
    assert "Column 'city' expected type 'integer'" in result


def test_count_based_validation_failure(sample_df):
    """
    Test that count-based validation reports an error when expected column counts do not match the DataFrame.
    """
    result = col_types_validate(
        dataframe=sample_df,
        integer_cols=2,  # only 1 integer column exists
        text_cols=2,
    )

    assert isinstance(result, str)
    assert "Expected 2 integer columns" in result


def test_empty_dataframe():
    """
    Test that the function reports an error when the input DataFrame is empty.
    """
    empty_df = pd.DataFrame()

    result = col_types_validate(dataframe=empty_df)

    assert isinstance(result, str)
    assert "DataFrame is empty" in result
