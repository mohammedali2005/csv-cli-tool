# tests/test_aggregation.py

import pytest
from csv_processor.operations import apply_aggregate

@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    return [
        {'product': 'A', 'price': '100', 'stock': '10'},
        {'product': 'B', 'price': '200', 'stock': '5'},
        {'product': 'C', 'price': '300', 'stock': '2'},
    ]

def test_aggregate_avg(sample_data):
    result = apply_aggregate(sample_data, 'price', 'avg')
    assert result['avg(price)'] == 200.0

def test_aggregate_min(sample_data):
    result = apply_aggregate(sample_data, 'stock', 'min')
    assert result['min(stock)'] == 2.0

def test_aggregate_max(sample_data):
    result = apply_aggregate(sample_data, 'price', 'max')
    assert result['max(price)'] == 300.0

def test_aggregate_on_empty_data():
    result = apply_aggregate([], 'price', 'avg')
    assert result['avg(price)'] == 0.0

def test_aggregate_invalid_function(sample_data):
    with pytest.raises(ValueError, match="Unsupported aggregation function: 'median'"):
        apply_aggregate(sample_data, 'price', 'median')

def test_aggregate_non_numeric_column(sample_data):
    with pytest.raises(ValueError, match="Column 'product' contains non-numeric values"):
        apply_aggregate(sample_data, 'product', 'avg')

def test_aggregate_invalid_column(sample_data):
    with pytest.raises(KeyError, match="Column 'rating' not found"):
        apply_aggregate(sample_data, 'rating', 'max')