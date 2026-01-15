import pandas as pd

def categorical_validate(
    dataframe: pd.DataFrame,
    column: str,
    num_cat: int,
    case: str = None,
    spaces: bool = False
):
    """
    Validate categorical column properties in a pandas DataFrame.

    This function performs a series of validation checks on a specified
    categorical column. Checks include validating the number of unique 
    categories and enforcing consistent casing and formatting rules such 
    as title case, uppercase, lowercase, and presence of spaces.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The pandas DataFrame containing the categorical column.
    column : str
        Name of the column to validate.
    num_cat : int
        Expected number of unique categories in the column, excluding 
        missing values (NaN, None, etc.).
    case : str, optional
        Expected case format for all categories. Valid options are:
        - "upper" : All categories should be uppercase
        - "lower" : All categories should be lowercase
        - "title" : All categories should be in title case (first letter 
          of each word capitalized, as determined by str.istitle())
        If None (default), no case validation is performed.
    spaces : bool, default=False
        If True, checks whether all categories contain at least one space.

    Returns
    -------
    str
        A confirmation message 'Checks completed!' indicating that all 
        validation checks have been executed. This message is returned 
        regardless of whether validations passed or failed. Individual 
        check results are printed to stdout during execution.

    Raises
    ------
    KeyError
        If the specified column does not exist in the dataframe.
    ValueError
        If num_cat is negative or if case is not one of the valid options 
        ("upper", "lower", "title", None).
    TypeError
        If the column does not contain string/categorical data.

    Notes
    -----
    - Missing values are removed prior to all validation checks.
    - Case validation is only performed if the case parameter is specified.
    - Validation results are reported via printed messages rather than
      raised exceptions.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     "city": ["Vancouver", "Toronto", "Calgary", None],
    ...     "gender": ["M", "F", "F", "M"],
    ...     "age": [25, 32, 41, 29]
    ... })
    >>> categorical_validate(
    ...     dataframe=df,
    ...     column="city",
    ...     num_cat=3,
    ...     case="title",
    ...     spaces=False
    ... )
    Expected and actual number of categories are equal
    All categories are in title case
    'Checks completed!'
       """
    
    # Validate case parameter
    valid_cases = ["upper", "lower", "title", None]
    if case not in valid_cases:
        raise ValueError(
            f"Invalid case parameter: '{case}'. "
            f"Must be one of {valid_cases}."
        )
    
    # Validate num_cat parameter
    if num_cat <= 0:
        raise ValueError("num_cat must be > 0.")
    
    # Validate dataframe is pd.Dataframe
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("dataframe must be a pd.DataFrame")
    
    # Check that column dtype is str or catagorical
    col = dataframe[column]
    dtype = col.dtype
    if dtype.kind not in {"O", "U", "S"} and str(dtype) != "category":
        raise TypeError(
            f"Column '{column}' must contain string or categorical data, "
            f"not {dtype}"
        )

    # Check if column exists
    if column not in dataframe.columns:
        raise KeyError(f"Column '{column}' does not exist in dataframe.")
    
    # Select column and drop NAs
    col = dataframe[column].dropna().astype(str)

    # Check if col has expected number of categories
    if num_cat == col.nunique():
        print("Expected and actual number of categories are equal")
    else:
        print("Expected and actual number of categories are NOT equal")

    # Check case formatting
    if case == "title":
        if col.str.istitle().all():
            print("All categories are in title case")
        else:
            print("Inconsistent case type (not title case)")
    elif case == "upper":
        if col.str.isupper().all():
            print("All categories are uppercase")
        else:
            print("Inconsistent case type (not uppercase)")
    elif case == "lower":
        if col.str.islower().all():
            print("All categories are lowercase")
        else:
            print("Inconsistent case type (not lowercase)")

    # Check for spaces present
    if spaces:
        if col.str.contains(r"\s", regex=True).all():
            print("All categories contain spaces")
        else:
            print("Not all categories contain spaces")

    return "Checks completed!"