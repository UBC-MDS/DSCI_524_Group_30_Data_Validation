# Welcome to DSCI_524_Group_30_Data_Validation

|        |        |
|--------|--------|
| Package | [![Latest TestPyPI Version](https://img.shields.io/badge/dynamic/json?color=blue&label=testpypi&query=%24.info.version&url=https%3A%2F%2Ftest.pypi.org%2Fpypi%2FDSCI_524_Group_30_Data_Validation%2Fjson)](https://test.pypi.org/project/DSCI_524_Group_30_Data_Validation/) [![Supported Python Versions](https://img.shields.io/badge/python-3.10+-blue.svg)](https://test.pypi.org/project/DSCI_524_Group_30_Data_Validation/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

## Summary

This package is an open source project which performs common data validation checks on a Pandas dataframe. This package aims to provide clear,
informative, and concise output from running each function, designed to help to user learn more about their data. Functions are flexible and a variety of arguments are included within each function, to ensure full adaptibilty for data validation with any Pandas dataframe. This is useful in any data science pipeline, providing reproducibility, full functionality, and effectiveness.

### Functions Included
| Function | Inputs | Outputs | Description |
|----------|--------|---------|-------------|
| `col_types_validate` | `dataframe: pd.DataFrame`<br>`numeric_cols: int`(default: `0`)<br>`integer_cols: int`(default: `0`)<br>`float_cols: int`(default: `0`)<br>`boolean_cols: int`(default: `0`)<br>`categorical_cols: int`(default: `0`)<br>`text_cols: int`(default: `0`)<br>`datetime_cols: int`(default: `0`)<br>`allow_extra_cols: bool`(default: `False`)<br>`column_schema: dict[str, str or type]`(optional) | `str` | Validates that a DataFrame contains the expected number of each given logical column category. |
| `missing_values_validate` | `df: pd.DataFrame`<br>`col: str`<br>`threshold: float or int` | `bool` | Checks whether the given column in the pandas dataframe has missing values over the given threshold (0-1) or not.|
| `outliers_validate` | `dataframe: pd.DataFrame`<br>`col: str`<br>`lower_bound: float`<br>`upper_bound: float`<br>`threshold: float` | `str` | Validates that a DataFrame column contains an acceptable proportion of values outside a user-defined range. |
| `categorical_validate` | `dataframe: pd.DataFrame`<br>`column: str`<br>`num_cat: int`<br>`case: str`(optional, default: `None`)<br>`spaces: bool = False`(default: `False`) | `str` | Validate categorical column properties in a pandas DataFrame. |

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
Either install from Test-Pypi using the following:

```bash
pip install -i https://test.pypi.org/simple/ dsci-524-group-30-data-validation
```

Or you can install this package from the local source into your preferred Python environment using pip:

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

### Build Quartodoc Site
Quartodoc is installed in the environment.yml file
```bash
quartodoc build --verbose
```

### Live preview locally (requires Quarto installed)

If you have Quarto installed locally, you can generate the API reference pages and preview the documentation website:

```bash
quarto preview
```

Documentation building / deployment is automated through GitHub Actions.

## Example Use

### Column Validation Function (`col_types_validate`)
Count-based validation only:
```python
import pandas as pd
from dsci_524_group_30_data_validation.col_types_validate import col_types_validate
df = pd.DataFrame({
     "city": ["Vancouver", "Toronto", "Calgary", "Winnipeg"],
     "name": ["John Smith", "Bron Crift", "Pylon Gift", "Akon Sarmist"],
     "gender": ["M", "F", "F", "M"],
     "age": [25, 32, 41, 29]
     })
col_types_validate(
    dataframe=df,
    integer_cols=1,
    text_cols=3
    )
```
Expected output:
```python
'All column categories present in the expected numbers.Check complete!'
```

Column-specific validation using logical type strings:
```python
col_types_validate(
    dataframe=df,
    column_schema={
      "age": "integer",
      "city": "text",
      "name": "text"
    }
  )
```
Expected output:
```python
'All specified columns match their expected types. Check complete!'
```

Combined count-based and column-specific validation:
```python
col_types_validate(
    dataframe=df,
    integer_cols=1,
    text_cols=3,
    column_schema={
      "age": "integer"
    }
  )
```
Expected output:
```python
'All column categories and specified columns are valid. Check complete!'
```

### Missing Values Threshold Function (`missing_values_validate`)
Passed the threshold requirement example:
```python
import pandas as pd
from dsci_524_group_30_data_validation.missing_values_validate import missing_values_validate
data = pd.DataFrame({
        "name": ["Alex", None, None, "Austin", None],
        "age": [21, 43, 23, None, 38],
        "sex": ["M", "F", "F", "M", "F"],
        "married": [True, False, None, None, True]})
missing_values_validate(df=data, col="age", threshold=0.25)
```
Expected output:
```python
The amount of missing values are valid. Checks completed!
True
```

Not passing the threshold requirement example:
```python
missing_values_validate(df=data, col="name", threshold=0.05)
```
Expected output:
```python
Invalid check: the amount of missing values is 0.6, exceeding the threshold: 0.05. Checks completed!
False
```

### Values Outlier Function (`outliers_validate`)
Example where outlier proportion is within the threshold:
```python
import pandas as pd
from dsci_524_group_30_data_validation.outlier_validation import outliers_validate
df = pd.DataFrame({"age": [25, 32, 41, 29, 200]})
outliers_validate(
    dataframe=df,
    col="age",
    lower_bound=0,
    upper_bound=100,
    threshold=0.20
    )
```
Expected output:
```python
'The proportion of outliers is within the acceptable threshold. Check complete!'
```

Example where outlier proportion exceeds the threshold:
```python
df = pd.DataFrame({"score": [10, 12, 999, 11, 1000]})
outliers_validate(
    dataframe=df,
    col="score",
    lower_bound=0,
    upper_bound=100,
    threshold=0.10
  )
```
Expected output:
```python
'The proportion of outliers exceeds the threshold 0.1. Check complete!'
```

### Categorical Column Function (`categorical_validate`)
```python
import pandas as pd
from dsci_524_group_30_data_validation.str_validate import categorical_validate
df = pd.DataFrame({
     "city": ["Vancouver", "Toronto", "Calgary", None],
     "gender": ["M", "F", "F", "M"],
     "age": [25, 32, 41, 29]
     })
categorical_validate(
    dataframe=df,
    column="city",
    num_cat=3,
    case="title",
    spaces=False
    )
```
Expected output:
```python
Expected and actual number of categories are equal
All categories are in title case
'Checks completed!'
```

## Continuous Integration / GitHub Badges

[![codecov](https://codecov.io/gh/UBC-MDS/DSCI_524_Group_30_Data_Validation/branch/main/graph/badge.svg?token=sT0UlVC1nn)](https://codecov.io/gh/UBC-MDS/DSCI_524_Group_30_Data_Validation)

### Workflows

[![Build Docs](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/docs.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/docs.yml)

[![CI](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/build.yml)

[![Dependabot Updates](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/dependabot/dependabot-updates)

[![Publish to Test PyPI](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/publish-test-pypi.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/publish-test-pypi.yml)

[![Build Pages Deployment](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/pages/pages-build-deployment)

[![Publish Docs](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/publish-docs.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_Group_30_Data_Validation/actions/workflows/publish-docs.yml)

## Contributors

Daniel Yorke, Cynthia Agata Limantono, Shrijaa Venkatasubramanian Subashini, and Wendy Frankel

## Copyright

- Copyright © 2026 Daniel Yorke, Cynthia Agata Limantono, Shrijaa Venkatasubramanian Subashini, and Wendy Frankel
- Free software distributed under the [MIT License](./LICENSE).
