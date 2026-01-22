# Welcome to DSCI_524_Group_30_Data_Validation

## Summary

This package is an open source project which performs common data validation checks on a Pandas dataframe. This package aims to provide clear,
informative, and concise output from running each function, designed to help to user learn more about their data. Functions are flexible and a variety of arguments are included within each function, to ensure full adaptibilty for data validation with any Pandas dataframe. This is useful in any data science pipeline, providing reproducibility, full functionality, and effectiveness.

### Functions Included

1. Column Validation Function: Validates that a DataFrame contains the expected number of each given logical column category.
2. Missing Values Threshold Function: This function checks whether the given column in the pandas dataframe has missing values at or below the given threshold.
3. Values Outlier Function: Validates that a DataFrame column contains an acceptable proportion of values outside a user-defined range.
4. Categorical Column Function: Validate categorical column properties in a pandas DataFrame.

The project looks to re-imagine some of the functions of [Pandera](https://pandera.readthedocs.io/en/stable/) in a more user-friendly way. It aims mainly to improve output of the Panderas function, making it more informative and interpretable.

## Setting up the Developement Environment

1. To get started, clone the repository to your local device.

2. Change directory into the repository

```bash
cd DSCI_524_Group_30_Data_Validation
```

1. Create the Conda environment from the lock file

```bash
conda-lock install -n project-env conda-lock.yml
```

1. Activate the environment

```bash
conda activate project-env
```

You should now see (project-env) in your terminal prompt.

1. Make sure you have quarto installed. You can install from here:

<https://quarto.org/docs/get-started/>

## Installing the Package

You can install this package from the local source into your preferred Python environment using pip:

```bash
pip install -e .
```

## Running Tests

You can run tests which validate all functions in the package using pytest.

```bash
pytest -v
```

-v results in a more verbose output, showing the names of all tests and if they pass or not.

## Build Documentation

```bash
quartodoc build --watch

quarto preview
```

Documentation deployment is automated.

## Example Use

```python
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
```

## Contributors

Daniel Yorke, Cynthia Agata Limantono, Shrijaa Venkatasubramanian Subashini, and Wendy Frankel

## Copyright

- Copyright © 2026 Daniel Yorke, Cynthia Agata Limantono, Shrijaa Venkatasubramanian Subashini, and Wendy Frankel
- Free software distributed under the [MIT License](./LICENSE).
