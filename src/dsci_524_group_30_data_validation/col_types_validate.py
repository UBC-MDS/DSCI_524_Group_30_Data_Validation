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
    allow_extra_cols: bool = True,
    column_schema: dict[str, str | type] | None = None,
):
    """
    Validates that a DataFrame contains the expected number of each
    logical column category and/or that specific columns match
    expected data types.

    This function performs two types of validation on a Pandas DataFrame:

    1. Count-based validation: Ensures the DataFrame contains the
    expected number of columns in each logical column category
    (e.g., numeric, text, categorical).

    2. Column-specific validation: Ensures that user-specified
    column names exist in the DataFrame and match their expected
    logical data types.

    All column count arguments are keyword-only. Users may also choose
    to allow extra, unspecified columns. All lowercase.

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
        A message stating whether all checks passed.
        If validation fails, the message describes which columns
        are missing, mismatched, or unexpected.

    Notes
    -------
    - Keyword arguments are required for all column type arguments.
    - Count-based and column-specific validation may be used together.
    - If both validation modes are provided, both must pass for
    validation to check complete.

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
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("dataframe must be a pandas DataFrame")

    if column_schema is not None and not isinstance(column_schema, dict):
        raise TypeError("column_schema must be a dictionary if provided")

    report = []

    schema_used = False
    count_used = False

    if column_schema:
        schema_used = True
        for col, expected in column_schema.items():
            if col not in dataframe.columns:
                report.append(f"Missing required column: '{col}'")
                continue

            if isinstance(expected, str):
                expected_type = expected.lower()
            elif expected is int:
                expected_type = "integer"
            elif expected is float:
                expected_type = "float"
            elif expected is bool:
                expected_type = "boolean"
            elif expected is str:
                expected_type = "text"
            else:
                report.append(
                    f"Warning: Unsupported expected type for column '{col}': {expected}"
                )
                continue

            actual_dtype = dataframe[col].dtype

            # check logical type
            if expected_type == "integer":
                valid = pd.api.types.is_integer_dtype(dataframe[col])
            elif expected_type == "float":
                valid = pd.api.types.is_float_dtype(dataframe[col])
            elif expected_type == "numeric":
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
                continue

            if actual_count != expected_count:
                report.append(
                    f"Expected {expected_count} '{logical_type}' columns, but found {actual_count}"
                )

    counted_cols = set()
    if count_used:
        for logical_type, expected_count in type_args.items():
            if expected_count > 0:
                if logical_type == "numeric":
                    counted_cols |= set(
                        dataframe.select_dtypes(include=["number"]).columns
                    )
                elif logical_type == "integer":
                    counted_cols |= set(
                        dataframe.select_dtypes(include=["int64", "Int64"]).columns
                    )
                elif logical_type == "float":
                    counted_cols |= set(
                        dataframe.select_dtypes(include=["float64", "Float64"]).columns
                    )
                elif logical_type == "boolean":
                    counted_cols |= set(
                        dataframe.select_dtypes(include=["bool"]).columns
                    )
                elif logical_type == "categorical":
                    counted_cols |= set(
                        dataframe.select_dtypes(include=["category"]).columns
                    )
                elif logical_type == "text":
                    counted_cols |= set(
                        dataframe.select_dtypes(include=["object", "string"]).columns
                    )
                elif logical_type == "datetime":
                    counted_cols |= set(
                        dataframe.select_dtypes(
                            include=["datetime64[ns]", "datetime64[ns, UTC]"]
                        ).columns
                    )

    if schema_used and column_schema:
        counted_cols |= set(column_schema.keys())

    if not allow_extra_cols and (count_used or schema_used):
        extra_cols = set(dataframe.columns) - counted_cols
        if extra_cols:
            report.append(f"Unexpected extra columns: {sorted(extra_cols)}")

    if report:
        return "\n".join(report)
    else:
        if schema_used and count_used:
            return (
                "All column categories and specified columns are valid. Check complete!"
            )
        elif schema_used:
            return "All specified columns match their expected types. Check complete!"
        else:
            return "All column categories are present in the expected numbers. Check complete!"
