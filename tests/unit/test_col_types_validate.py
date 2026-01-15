import pandas as pd
import pytest
from dsci_524_group_30_data_validation.col_types_validate import col_types_validate

def test_col_types_validate:
    df = pd.DataFrame({
        "city": ["Vancouver", "Toronto", "Calgary", "Winnipeg"],
        "name": ["John Smith", "Bron Crift", "Pylon Gift", "Akon Sarmist"],
        "gender": ["M", "F", "F", "M"],
        "age": [25, 32, 41, 29]
    })

    # Count-based validation (expected success)
    result = col_types_validate(
        dataframe=df,
        integer_cols=1,
        text_cols=3
    )
    assert isinstance(result, str)
    assert "Check complete" in result

    # 2Column-schema validation with logical types (expected success)
    result = col_types_validate(
        dataframe=df,
        column_schema={
            "age": "integer",
            "city": "text",
            "name": "text"
        }
    )
    assert isinstance(result, str)
    assert "Check complete" in result

    # Schema validation failure (column exists but wrong type)
    with pytest.raises(TypeError):
        col_types_validate(
            dataframe=df,
            column_schema={
                "age": "text"  # age is integer, should raise TypeError
            }
        )
