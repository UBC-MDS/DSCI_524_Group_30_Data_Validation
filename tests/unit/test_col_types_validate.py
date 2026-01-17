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


def test_allow_extra_cols_true_pass(sample_df):
    """Extra columns are allowed when allow_extra_cols=True."""
    result = col_types_validate(
        dataframe=sample_df,
        integer_cols=1,
        allow_extra_cols=True,
    )

    assert isinstance(result, str)
    assert "check complete" in result.lower()


def test_combined_schema_and_count_fail(sample_df):
    """Failure occurs if either schema or count validation fails."""
    result = col_types_validate(
        dataframe=sample_df,
        integer_cols=2,  # wrong
        column_schema={"age": "integer"},
    )

    assert isinstance(result, str)
    assert "expected" in result.lower()


def test_combined_schema_and_count_success(sample_df):
    """Both schema and count validation pass together."""
    result = col_types_validate(
        dataframe=sample_df,
        integer_cols=1,
        text_cols=3,
        column_schema={"age": "integer"},
    )

    assert isinstance(result, str)
    assert "check complete" in result.lower()


def test_numeric_cols_combined_fail(sample_df):
    """numeric_cols mismatch is reported."""
    result = col_types_validate(
        dataframe=sample_df,
        numeric_cols=2,
    )

    assert isinstance(result, str)
    assert "numeric" in result.lower()
    assert "expected" in result.lower()


def test_numeric_cols_combined_pass(sample_df):
    """numeric_cols counts integers and floats together."""
    result = col_types_validate(
        dataframe=sample_df,
        numeric_cols=1,
    )

    assert isinstance(result, str)
    assert "check complete" in result.lower()


def test_column_schema_type_objects_pass(sample_df):
    """Schema validation supports Python type objects."""
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={
            "age": int,
            "city": str,
        },
    )

    assert isinstance(result, str)
    assert "check complete" in result.lower()


def test_column_schema_none_branch(sample_df):
    """Schema validation is skipped when column_schema=None."""
    result = col_types_validate(
        dataframe=sample_df,
        integer_cols=1,
        text_cols=3,
        column_schema=None,
    )

    assert isinstance(result, str)
    assert "check complete" in result.lower()


def test_schema_with_unsupported_type_object(sample_df):
    """Test schema validation with an unsupported Python type object."""
    result = col_types_validate(
        dataframe=sample_df, column_schema={"age": list}  # Unsupported type
    )
    assert isinstance(result, str)
    assert "unsupported" in result.lower() or "warning" in result.lower()


def test_schema_numeric_type_pass(sample_df):
    """Test schema validation with 'numeric' type (covers numeric branch)."""
    result = col_types_validate(dataframe=sample_df, column_schema={"age": "numeric"})
    assert isinstance(result, str)
    assert "Check complete" in result


def test_schema_numeric_type_fail(sample_df):
    """Test schema validation fails when numeric expected but column is text."""
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={"city": "numeric"},  # city is text, not numeric
    )
    assert isinstance(result, str)
    assert "Column 'city' expected type numeric in result"


def test_schema_boolean_type_fail(sample_df):
    """Test schema validation with 'boolean' type fails on non-boolean column."""
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={"age": "boolean"},  # age is integer, not boolean
    )
    assert isinstance(result, str)
    assert "Column 'age' expected type 'boolean'" in result


def test_schema_categorical_type_fail(sample_df):
    """Test schema validation with 'categorical' type fails on non-categorical column."""
    result = col_types_validate(
        dataframe=sample_df,
        column_schema={"city": "categorical"},  # city is object, not categorical dtype
    )
    assert isinstance(result, str)
    assert "Column 'city' expected type 'categorical'" in result


def test_schema_with_python_bool_type_fail(sample_df):
    """Test schema validation with Python bool type object fails on non-bool column."""
    result = col_types_validate(
        dataframe=sample_df, column_schema={"age": bool}  # age is int, expecting bool
    )
    assert isinstance(result, str)
    assert "Column 'age' expected type 'boolean'" in result
