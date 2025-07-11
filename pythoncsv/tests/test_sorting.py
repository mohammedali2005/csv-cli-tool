# tests/test_sorting.py

import pytest
from csv_processor.main_logic import apply_orderby

@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    return [
        {'name': 'B', 'brand': 'Z', 'price': '200', 'rating': '4.8'},
        {'name': 'C', 'brand': 'Y', 'price': '300', 'rating': '4.6'},
        {'name': 'A', 'brand': 'X', 'price': '100', 'rating': '4.9'}
    ]

def test_sort_ascending_numeric(sample_data):
    result = apply_orderby(sample_data, 'price', 'asc')
    assert [row['name'] for row in result] == ['A', 'B', 'C']

def test_sort_descending_numeric(sample_data):
    result = apply_orderby(sample_data, 'rating', 'desc')
    assert [row['name'] for row in result] == ['A', 'B', 'C']

def test_sort_ascending_string(sample_data):
    result = apply_orderby(sample_data, 'brand', 'asc')
    assert [row['name'] for row in result] == ['A', 'C', 'B']

def test_sort_invalid_direction(sample_data):
    with pytest.raises(ValueError, match="Unsupported sort direction: 'up'"):
        apply_orderby(sample_data, 'price', 'up')

def test_sort_invalid_column(sample_data):
    with pytest.raises(KeyError, match="Sorting error: Column 'stock' not found"):
        apply_orderby(sample_data, 'stock', 'asc')