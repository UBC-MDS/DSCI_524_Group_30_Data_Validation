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
    'All column categories are present in the expected numbers. Check complete!'


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
