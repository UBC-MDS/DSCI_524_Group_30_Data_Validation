def col_types(
    dataframe: pd.DataFrame,
    *,
    numeric_cols: int = 0,
    integer_cols: int = 0,
    float_cols: int = 0,
    boolean_cols: int = 0,
    categorical_cols: int = 0,
    text_cols: int = 0,
    datetime_cols: int = 0,
    column_schema: dict[str, str | type] | None = None,
    allow_extra_cols: bool = False,
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

    Returns
    -------
    str
        Message which either confirms that all columns are present in the
        expected amounts, or prints out column types which are unexpected,
        in what numbers, and their titles (if there are column titles).

        If allow_extra_cols = True, and there are unexpected columns,
        function will print out the unexpected columns.

    Notes
    -------
        Keyword arguments are required for all column type arguments.

        Validation results are printed as a string.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
            "city": ["Vancouver", "Toronto", "Calgary", "Winnipeg"],
            "name": ["John Smith", "Bron Crift", "Pylon Gift", "Akon Sarmist"]
            "gender": ["M", "F", "F", "M"],
            "age": [25, 32, 41, 29]
        })
    >>> col_types(
            dataframe=df,
            numeric_cols = 1,
            categorical_cols = 2,
            text_cols = 1,
        )
    All column categories are present in the expected numbers. Check complete!
    """
