# from src.roman_converter.roman_converter import convert_to_roman

# def test_zero_returns_empty_string():
#     result = convert_to_roman(0)
#     assert result == ""

# def test_one_returns_I():
#     result = convert_to_roman(1)
#     assert result == "I"
    
# def test_five_returns_V():
#     result = convert_to_roman(5)
#     assert result == "V"

import pytest
from src.roman_converter.roman_converter import convert_to_roman

@pytest.mark.parametrize("input_value, expected_output", [
    (0, ""),
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (10, "X"),
    (19, "XIX"),
    (20, "XX"),
    (50, "L"),
])
def test_convert_to_roman(input_value, expected_output):
    result = convert_to_roman(input_value)
    assert result == expected_output
