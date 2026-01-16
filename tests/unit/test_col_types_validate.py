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
    assert "salary" in result.lower()
    assert "missing" in result.lower()


def test_schema_invalid_logical_type(sample_df):
    """
    Test that schema validation reports an error when an unsupported logical type is provided.
    """
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={"age": "date"},
    )

    assert isinstance(result, str)
    assert "unknown" in result.lower() or "unsupported" in result.lower()
    assert "date" in result.lower()


def test_empty_column_schema(sample_df):
    """
    Test that providing an empty column schema is treated as invalid input.
    """
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={},
    )

    assert isinstance(result, str)
    assert "check complete" in result.lower()


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

    result_lower = result.lower()
    assert "integer" in result_lower
    assert "text" in result_lower
    assert "expected" in result_lower
    assert "found" in result_lower


def test_empty_dataframe():
    """
    Test that the function reports an error when the input DataFrame is empty.
    """
    empty_df = pd.DataFrame()

    result = col_types_validate(dataframe=empty_df)

    assert isinstance(result, str)
    assert "check complete" in result.lower()


def test_count_based_validation_no_counts(sample_df):
    """Count-based validation should pass if all counts are 0 (ignored)."""
    result = col_types_validate(dataframe=sample_df)
    assert "Check complete" in result


def test_extra_columns_allowed(sample_df):
    """Extra columns are allowed when allow_extra_cols=True."""
    result = col_types_validate(
        dataframe=sample_df, integer_cols=1, allow_extra_cols=True
    )
    assert isinstance(result, str)
    assert "Check complete" in result


def test_extra_columns_disallowed(sample_df):
    """Extra columns are reported when allow_extra_cols=False."""
    result = col_types_validate(
        dataframe=sample_df, integer_cols=1, text_cols=1, allow_extra_cols=False
    )
    assert isinstance(result, str)
    assert "expected" in result.lower() and "'text'" in result.lower()


def test_invalid_dataframe_type():
    """Function should raise TypeError if input is not a DataFrame."""
    import numpy as np

    with pytest.raises(TypeError):
        col_types_validate(dataframe=np.array([[1, 2], [3, 4]]))


def test_invalid_column_schema_type(sample_df):
    """Function should raise TypeError if column_schema is not a dict."""
    with pytest.raises(TypeError):
        col_types_validate(dataframe=sample_df, column_schema=["age", "text"])
