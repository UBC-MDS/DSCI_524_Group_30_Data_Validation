def categorical_validate(
    dataframe: pd.DataFrame,
    column: str,
    num_cat: int,
    title_case: bool = False,
    spaces: bool = False,
    lowercase: bool = False,
    uppercase: bool = False
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
        Expected number of unique (non-missing) categories in the column.
    title_case : bool, default=False
        If True, checks whether all categories follow title case formatting.
    spaces : bool, default=False
        If True, checks whether all categories contain at least one space.
    lowercase : bool, default=False
        If True, checks whether all categories are lowercase.
    uppercase : bool, default=False
        If True, checks whether all categories are uppercase.

    Returns
    -------
    str
        A confirmation message indicating that validation checks
        have completed.

    Notes
    -----
    - Missing values are removed prior to all validation checks.
    - All checks are applied only if the corresponding boolean flag is True.
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
    ...     title_case=True,
    ...     spaces=False
    ... )
    Expected and actual number of categories are equal
    All categories are in title case
    'Checks completed!'
    """
    
    # select column and drop NAs
    col = dataframe[column].dropna().astype(str)

    # check if col has expected number of categories
    if num_cat == col.nunique():
        print("Expected and actual number of categories are equal")
    else:
        print("Expected and actual number of categories are NOT equal")

    # checks if in title case
    if title_case:
        if col.str.istitle().all():
            print("All categories are in title case")
        else:
            print("Inconsistent case type (not title case)")

    # checks for spaces present
    if spaces:
        if col.str.contains(r"\s", regex=True).all():
            print("All categories contain spaces")
        else:
            print("Not all categories contain spaces")

    # checks for all uppercase
    if uppercase:
        if col.str.isupper().all():
            print("All categories are uppercase")
        else:
            print("Inconsistent case type (not uppercase)")

    # checks for all lower case
    if lowercase:
        if col.str.islower().all():
            print("All categories are lowercase")
        else:
            print("Inconsistent case type (not lowercase)")

    return "Checks completed!"
