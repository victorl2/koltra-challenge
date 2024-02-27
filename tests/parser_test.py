import pytest
from src.service.parser import Parser

@pytest.mark.parametrize("input_str,expected", [
    ("150g Square, 250g Oval, 50g Rectangle, 100g Triangle, 50g Circle, 50g Circle, 200g Rectangle", (True, "Input is valid")),
    ("150g Square, 25g Oval, 50g Rectangle", (False, "Weight must be a multiple of 50 with a max of 250 grams")),
    ("150g Square, 250g Hexagon", (False, "Invalid shape: Hexagon, must be one of Circle, Oval, Rectangle, Square, Triangle")),
    ("150 Square, 250g Oval", (False, "Weight must be in grams")),
    ("", (False, "Invalid format: Each gift should be in the format '<weight>g <shape>'")),
])
def test_validate_input(input_str, expected):
    parser = Parser()
    assert parser.validate_gifts(input_str) == expected

@pytest.mark.parametrize("input_str,expected", [
    ("150g Square, 250g Oval, 50g Rectangle, 100g Triangle, 50g Circle", [("Square", 150), ("Oval", 250), ("Rectangle", 50), ("Triangle", 100), ("Circle", 50)]),
    ("50g Circle, 50g Circle", [("Circle", 50), ("Circle", 50)]),
])
def test_parse_gifts(input_str, expected):
    assert Parser.parse_gifts(input_str) == expected
