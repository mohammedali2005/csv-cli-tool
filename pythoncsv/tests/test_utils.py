# tests/test_utils.py

import pytest
from csv_processor import utils

def test_parse_condition_valid():
    assert utils.parse_condition("price>500") == ('price', '>', '500')
    assert utils.parse_condition("brand=apple") == ('brand', '=', 'apple')
    assert utils.parse_condition("rating < 4.5") == ('rating', '<', '4.5')

def test_parse_condition_invalid():
    assert utils.parse_condition("price!500") is None
    assert utils.parse_condition("brand") is None

def test_parse_key_value_valid():
    assert utils.parse_key_value("column=value") == ('column', 'value')
    assert utils.parse_key_value("price=asc") == ('price', 'asc')

def test_parse_key_value_invalid():
    assert utils.parse_key_value("column:value") is None
    assert utils.parse_key_value("price") is None

def test_try_convert_to_float():
    assert utils.try_convert_to_float("123.45") == 123.45
    assert utils.try_convert_to_float("100") == 100.0
    assert utils.try_convert_to_float("text") == "text"
    assert utils.try_convert_to_float(None) is None