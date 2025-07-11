# tests/test_filtering.py

import pytest
from csv_processor.main_logic import apply_where

@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    return [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
        {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
        {'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'}
    ]

def test_filter_greater_than_numeric(sample_data):
    result = apply_where(sample_data, 'price', '>', '500')
    assert len(result) == 2
    assert result[0]['name'] == 'iphone 15 pro'
    assert result[1]['name'] == 'galaxy s23 ultra'

def test_filter_less_than_numeric(sample_data):
    result = apply_where(sample_data, 'rating', '<', '4.7')
    assert len(result) == 2
    assert result[0]['name'] == 'redmi note 12'
    assert result[1]['name'] == 'poco x5 pro'

def test_filter_equal_to_string(sample_data):
    result = apply_where(sample_data, 'brand', '=', 'apple')
    assert len(result) == 1
    assert result[0]['brand'] == 'apple'

def test_filter_no_results(sample_data):
    result = apply_where(sample_data, 'price', '>', '2000')
    assert len(result) == 0

def test_filter_invalid_column(sample_data):
    with pytest.raises(KeyError, match="Filtering error: Column 'color' not found in the data."):
        apply_where(sample_data, 'color', '=', 'blue')

def test_filter_invalid_operator(sample_data):
    with pytest.raises(ValueError, match="Unsupported operator: '!='."):
        apply_where(sample_data, 'price', '!=', '999')