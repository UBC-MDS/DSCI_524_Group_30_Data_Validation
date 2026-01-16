# Testing the str_validate function
import pandas as pd
import pytest
from dsci_524_group_30_data_validation.str_validate import categorical_validate

@pytest.fixture
def full_df():
    """Comprehensive dataframe with multiple column types."""
    return pd.DataFrame({
        "gender": ["M", "F", "F", "M", "F", "M", "M", "F", "F", "M"],
        "city": ["Vancouver", "Toronto", "Toronto", "Calgary", "Vancouver",
                 "Calgary", "Toronto", "Vancouver", "Calgary", "Toronto"],
        "education": ["HS", "College", "University", "HS", "University",
                      "College", "HS", "University", "College", "HS"],
        "age": [23, 35, 29, 42, 31, 27, 38, 26, 34, 45],
        "income": [45000, 72000, 68000, 81000, 75000,
                   62000, 79000, 56000, 71000, 85000]
    })

def test_data_type(full_df):  
    """Test that non-string categorical columns raise TypeError."""
    with pytest.raises(TypeError, match="categorical|string"):
        categorical_validate(dataframe=full_df, column="income", num_cat=10)

def test_num_cat_positive(full_df):
    """Test that negative num_cat raises ValueError."""
    with pytest.raises(ValueError):
        categorical_validate(dataframe= full_df, column = "city", num_cat = -10)

def test_column_not_exists(full_df):
    """Test that non-existent column raises KeyError."""
    with pytest.raises(KeyError, match="fruit|column"):
        categorical_validate(full_df, column="fruit", num_cat=3)

def test_num_cat_correct(full_df):   
    """Test if the function reterns the correct number of categories"""
    result = categorical_validate(full_df, column="city", num_cat=3)
    assert result == "Checks completed!"

def test_invalid_dataframe_type():
    """Test that non-DataFrame input raises TypeError."""
    not_a_df = {"city": ["Vancouver", "Toronto"]}
    
    with pytest.raises(TypeError, match="pd.DataFrame"):
        categorical_validate(dataframe= not_a_df, column="city", num_cat=2)

def test_invalid_column_type(full_df):
    """Test that non-string column name raises TypeError."""  
    with pytest.raises(TypeError, match="string|str"):
        categorical_validate(full_df, column=123, num_cat=2)

# Test case="title" - pass branch
def test_case_title_pass(capsys, full_df):
    """Test that title case validation passes."""
    result = categorical_validate(full_df, column="city", num_cat=3, case="title")
    captured = capsys.readouterr()
    
    assert result == "Checks completed!"
    assert "in title case" in captured.out


# Test case="title" - fail branch
def test_case_title_fail(capsys):
    """Test that title case validation fails for lowercase data."""
    df = pd.DataFrame({"city": ["vancouver", "toronto", "calgary"]})
    result = categorical_validate(df, column="city", num_cat=3, case="title")
    captured = capsys.readouterr()
    
    assert result == "Checks completed!"
    assert "Inconsistent" in captured.out


# Test case="upper" - pass branch
def test_case_upper_pass(capsys):
    """Test that uppercase validation passes."""
    df = pd.DataFrame({"code": ["ABC", "DEF", "GHI"]})
    result = categorical_validate(df, column="code", num_cat=3, case="upper")
    captured = capsys.readouterr()
    
    assert result == "Checks completed!"
    assert "uppercase" in captured.out


# Test case="upper" - fail branch
def test_case_upper_fail(capsys):
    """Test that uppercase validation fails for lowercase data."""
    df = pd.DataFrame({"code": ["abc", "def", "ghi"]})
    result = categorical_validate(df, column="code", num_cat=3, case="upper")
    captured = capsys.readouterr()
    
    assert result == "Checks completed!"
    assert "Inconsistent" in captured.out


# Test case="lower" - pass branch
def test_case_lower_pass(capsys):
    """Test that lowercase validation passes."""
    df = pd.DataFrame({"color": ["red", "blue", "green"]})
    result = categorical_validate(df, column="color", num_cat=3, case="lower")
    captured = capsys.readouterr()
    
    assert result == "Checks completed!"
    assert "lowercase" in captured.out


# Test case="lower" - fail branch
def test_case_lower_fail(capsys):
    """Test that lowercase validation fails for uppercase data."""
    df = pd.DataFrame({"color": ["RED", "BLUE", "GREEN"]})
    result = categorical_validate(df, column="color", num_cat=3, case="lower")
    captured = capsys.readouterr()
    
    assert result == "Checks completed!"
    assert "Inconsistent" in captured.out


# Test spaces=True - pass branch
def test_spaces_present_pass(capsys):
    """Test that spaces validation passes when all have spaces."""
    df = pd.DataFrame({"province": ["British Columbia", "Nova Scotia"]})
    result = categorical_validate(df, column="province", num_cat=2, spaces=True)
    captured = capsys.readouterr()
    
    assert result == "Checks completed!"
    assert "contain spaces" in captured.out


# Test spaces=True - fail branch
def test_spaces_absent_fail(capsys):
    """Test that spaces validation fails when spaces are absent."""
    df = pd.DataFrame({"city": ["Vancouver", "Toronto", "Calgary"]})
    result = categorical_validate(df, column="city", num_cat=3, spaces=True)
    captured = capsys.readouterr()
    
    assert result == "Checks completed!"
    assert "Not all" in captured.out

