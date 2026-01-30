# Welcome to DSCI_524_Group_30_Data_Validation

|        |        |
|--------|--------|
| Package | [![Latest TestPyPI Version](https://img.shields.io/badge/dynamic/json?color=blue&label=testpypi&query=%24.info.version&url=https%3A%2F%2Ftest.pypi.org%2Fpypi%2FDSCI_524_Group_30_Data_Validation%2Fjson)](https://test.pypi.org/project/DSCI_524_Group_30_Data_Validation/) [![Supported Python Versions](https://img.shields.io/badge/python-3.10+-blue.svg)](https://test.pypi.org/project/DSCI_524_Group_30_Data_Validation/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

## Summary

This package is an open source project which performs common data validation checks on a Pandas dataframe. This package aims to provide clear,
informative, and concise output from running each function, designed to help to user learn more about their data. Functions are flexible and a variety of arguments are included within each function, to ensure full adaptibilty for data validation with any Pandas dataframe. This is useful in any data science pipeline, providing reproducibility, full functionality, and effectiveness.

### Functions Included

1. Column Validation Function: Validates that a DataFrame contains the expected number of each given logical column category.
2. Missing Values Threshold Function: This function checks whether the given column in the pandas dataframe has missing values over the given threshold or not.
3. Values Outlier Function: Validates that a DataFrame column contains an acceptable proportion of values outside a user-defined range.
4. Categorical Column Function: Validate categorical column properties in a pandas DataFrame.

The project looks to re-imagine some of the functions of [Pandera](https://pandera.readthedocs.io/en/stable/) in a more user-friendly way. It aims mainly to improve output of the Panderas function, making it more informative and interpretable.

## Setting up the Development Environment

1. To get started, clone the repository to your local device.

```bash
git clone https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation.git
```

2. Change directory into the repository

```bash
cd DSCI_524_Group_30_Data_Validation
```

3. Create the Conda environment from the lock file

```bash
conda-lock install -n project-env conda-lock.yml
```

4. Activate the environment

```bash
conda activate project-env
```

You should now see (project-env) in your terminal prompt.

5. Make sure you have quarto installed for viewing the documentation site. You can install from here:

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
### Live preview locally (requires Quarto installed)

If you have Quarto installed locally, you can generate the API reference pages and preview the documentation website:

```bash
quarto preview
```

Documentation building / deployment is automated through GitHub Actions.

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

## Github Actions Badges

[![Build Docs](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/docs.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/docs.yml)

[![ci](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/build.yml)

[![Dependabot Updates](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/dependabot/dependabot-updates)

[![deploy-test-pypi](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/deploy.yml)

[![pages-build-deployment](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/pages/pages-build-deployment)

[![Publish Docs](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/publish-docs.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/publish-docs.yml)

## Contributors

Daniel Yorke, Cynthia Agata Limantono, Shrijaa Venkatasubramanian Subashini, and Wendy Frankel

## Copyright

- Copyright © 2026 Daniel Yorke, Cynthia Agata Limantono, Shrijaa Venkatasubramanian Subashini, and Wendy Frankel
- Free software distributed under the [MIT License](./LICENSE).
