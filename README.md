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

## Getting Started

1. To get started, clone the repository to your local device.

2. Create the Conda environment from the lock file

```
conda-lock install -n project-env conda-lock.yml
```

1. Activate the environment

```
conda activate project-env
```

You should now see (project-env) in your terminal prompt.

## Installing the Package

You can install this package into your preferred Python environment using pip:

```bash
pip install dsci_524_group_30_data_validation
```

TODO: Add a brief example of how to use the package to this section

To use dsci_524_group_30_data_validation in your code:

```python
>>> import dsci_524_group_30_data_validation
>>> dsci_524_group_30_data_validation.hello_world()
```

## Contributors

Daniel Yorke, Cynthia Agata Limantono, Shrijaa Venkatasubramanian Subashini, and Wendy Frankel

## Copyright

- Copyright © 2026 Daniel Yorke, Cynthia Agata Limantono, Shrijaa Venkatasubramanian Subashini, and Wendy Frankel
- Free software distributed under the [MIT License](./LICENSE).
