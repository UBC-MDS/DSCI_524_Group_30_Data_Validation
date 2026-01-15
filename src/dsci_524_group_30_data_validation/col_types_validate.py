import pandas as pd


def col_types_validate(
    dataframe: pd.DataFrame,
    *,
    numeric_cols: int = 0,
    integer_cols: int = 0,
    float_cols: int = 0,
    boolean_cols: int = 0,
    categorical_cols: int = 0,
    text_cols: int = 0,
    datetime_cols: int = 0,
    allow_extra_cols: bool = False,
    column_schema: dict[str, str | type] | None = None,
):
    """
    Validates that a DataFrame contains the expected number of each
    logical column category and/or that specific columns match
    expected data types.

    This function performs two types of validation on a Pandas DataFrame:

    1. **Count-based validation**: Ensures the DataFrame contains the
    expected number of columns in each logical column category
    (e.g., numeric, text, categorical).

    2. **Column-specific validation**: Ensures that user-specified
    column names exist in the DataFrame and match their expected
    logical data types.

    All column count arguments are keyword-only. Users may also choose
    to allow extra, unspecified columns.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The DataFrame to validate.

    numeric_cols : int, default 0
        Total number of numeric columns (integers and floats combined).

    integer_cols : int, default 0
        Number of integer-valued numeric columns.

    float_cols : int, default 0
        Number of floating-point numeric columns.

    boolean_cols : int, default 0
        Number of boolean columns.

    categorical_cols : int, default 0
        Number of categorical columns (pandas 'category' dtype).

    text_cols : int, default 0
        Number of text columns ('string' or 'object' dtype).

    datetime_cols : int, default 0
        Number of datetime-like columns ('datetime64' or timezone-aware).

    allow_extra_cols : bool, default False
        Whether to allow columns that are not accounted for by the
        specified validation rules. If False, unexpected columns
        will be reported as validation failures.

    column_schema : dict[str, str or type], optional
        Mapping of column names to expected logical data types.
        Each specified column must exist in the DataFrame and match
        the expected type.

    Supported logical types include:
        - "numeric"
        - "integer"
        - "float"
        - "boolean"
        - "categorical"
        - "text"
        - "datetime"

    Returns
    -------
    str
        A validation message indicating whether all checks passed.
        If validation fails, the message describes which columns
        are missing, mismatched, or unexpected.

    Notes
    -------
    - Keyword arguments are required for all column type arguments.
    - Count-based and column-specific validation may be used together.
    - If both validation modes are provided, *both must pass* for
    validation to succeed.

    Examples
    --------
    Count-based validation only:

    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "city": ["Vancouver", "Toronto", "Calgary", "Winnipeg"],
    ...     "name": ["John Smith", "Bron Crift", "Pylon Gift", "Akon Sarmist"],
    ...     "gender": ["M", "F", "F", "M"],
    ...     "age": [25, 32, 41, 29]
    ... })
    >>> col_types(
    ...     dataframe=df,
    ...     integer_cols=1,
    ...     text_cols=3
    ... )
    'All column categories present in the expected numbers.
    Check complete!'

    Column-specific validation using logical type strings:

    >>> col_types(
    ...     dataframe=df,
    ...     column_schema={
    ...         "age": "integer",
    ...         "city": "text",
    ...         "name": "text"
    ...     }
    ... )
    'All specified columns match their expected types. Check complete!'

    Combined count-based and column-specific validation:

    >>> col_types(
    ...     dataframe=df,
    ...     integer_cols=1,
    ...     text_cols=3,
    ...     column_schema={
    ...         "age": "integer"
    ...     }
    ... )
    'All column categories and specified columns are valid. Check complete!'

    """

    import pandas as pd

    report = []

    schema_used = False
    count_used = False

    if column_schema is not None:
        for col, expected in column_schema.items():
            # 1. Check column exists
            if col not in dataframe.columns:
                report.append(f"Missing required column: '{col}'")
                continue

            # 2. Normalize expected type
            if isinstance(expected, str):
                expected_type = expected.lower()
            elif expected is int:
                expected_type = "integer"
            elif expected is float:
                expected_type = "float"
            elif expected is bool:
                expected_type = "boolean"
            else:
                report.append(
                    f"Warning: Unsupported expected type for column "
                    f"'{col}': {expected}"
                )
                continue

            # 3. Get actual dtype
            actual_dtype = dataframe[col].dtype

            # 4. Check if dtype matches expected logical type
            if expected_type == "integer":
                valid = pd.api.types.is_integer_dtype(dataframe[col])
            elif expected_type == "float":
                valid = pd.api.types.is_float_dtype(dataframe[col])
            elif expected_type == "numeric":
                # numeric = integer OR float
                valid = pd.api.types.is_numeric_dtype(dataframe[col])
            elif expected_type == "boolean":
                valid = pd.api.types.is_bool_dtype(dataframe[col])
            elif expected_type == "text":
                valid = pd.api.types.is_string_dtype(
                    dataframe[col]
                ) or pd.api.types.is_object_dtype(dataframe[col])
            elif expected_type == "categorical":
                valid = pd.api.types.is_categorical_dtype(dataframe[col])
            elif expected_type == "datetime":
                valid = pd.api.types.is_datetime64_any_dtype(dataframe[col])
            else:
                report.append(
                    f"Warning: Unknown logical type for column '{col}': '{expected_type}'"
                )
                continue
            if not valid:
                report.append(
                    f"Column '{col}' expected type '{expected_type}' but found dtype '{actual_dtype}'"
                )

    type_args = {
        "numeric": numeric_cols,
        "integer": integer_cols,
        "float": float_cols,
        "boolean": boolean_cols,
        "categorical": categorical_cols,
        "text": text_cols,
        "datetime": datetime_cols,
    }

    for logical_type, expected_count in type_args.items():
        if expected_count > 0:
            count_used = True
            # Compute actual count
            if logical_type == "numeric":
                actual_count = dataframe.select_dtypes(include=["number"]).shape[1]
            elif logical_type == "integer":
                actual_count = dataframe.select_dtypes(
                    include=["int64", "Int64"]
                ).shape[1]
            elif logical_type == "float":
                actual_count = dataframe.select_dtypes(
                    include=["float64", "Float64"]
                ).shape[1]
            elif logical_type == "boolean":
                actual_count = dataframe.select_dtypes(include=["bool"]).shape[1]
            elif logical_type == "categorical":
                actual_count = dataframe.select_dtypes(include=["category"]).shape[1]
            elif logical_type == "text":
                actual_count = dataframe.select_dtypes(
                    include=["object", "string"]
                ).shape[1]
            elif logical_type == "datetime":
                actual_count = dataframe.select_dtypes(
                    include=["datetime64[ns]", "datetime64[ns, UTC]"]
                ).shape[1]
            else:
                continue  # should never happen

            if actual_count != expected_count:
                report.append(
                    f"Expected {expected_count} '{logical_type}' columns, but found {actual_count}"
                )

    if allow_extra_cols:
        # Columns not counted in counts and not in column_schema
        counted_cols = set(dataframe.columns)
        if column_schema:
            counted_cols -= set(column_schema.keys())
        # Report any extra columns
        extra_cols = set(dataframe.columns) - counted_cols
        if extra_cols:
            report.append(f"Extra columns present: {sorted(extra_cols)}")

    if report:
        return "\n".join(report)
    else:
        # Determine success message based on which modes were used
        if schema_used and count_used:
            return (
                "All column categories and specified columns are valid. Check complete!"
            )
        elif schema_used:
            return "All specified columns match their expected types. Check complete!"
        else:  # count-based only
            return "All column categories are present in the expected numbers. Check complete!"
