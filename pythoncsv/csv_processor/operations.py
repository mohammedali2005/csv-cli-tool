# csv_processor/operations.py

from typing import List, Dict, Callable, Any

def _calculate_avg(data: List[float]) -> float:
    return sum(data) / len(data) if data else 0.0

def _calculate_min(data: List[float]) -> float:
    return min(data) if data else 0.0

def _calculate_max(data: List[float]) -> float:
    return max(data) if data else 0.0

# Extensible registry of aggregation functions
AGGREGATION_FUNCTIONS: Dict[str, Callable[[List[float]], float]] = {
    'avg': _calculate_avg,
    'min': _calculate_min,
    'max': _calculate_max,
}

def apply_aggregate(data: List[Dict[str, Any]], column: str, func_name: str) -> Dict[str, Any]:
    """
    Applies a named aggregation function to a specific column in the dataset.

    Args:
        data: The list of data rows (dictionaries).
        column: The name of the column to aggregate.
        func_name: The name of the aggregation function ('avg', 'min', 'max').

    Returns:
        A dictionary containing the aggregation result.
    
    Raises:
        ValueError: If the aggregation function is not supported or the column
                    contains non-numeric data.
        KeyError: If the specified column does not exist.
    """
    if func_name not in AGGREGATION_FUNCTIONS:
        raise ValueError(f"Unsupported aggregation function: '{func_name}'. Supported functions are: {', '.join(AGGREGATION_FUNCTIONS.keys())}")

    aggregation_func = AGGREGATION_FUNCTIONS[func_name]
    
    try:
        # Check for column existence on the first row if data exists
        if data and column not in data[0]:
            raise KeyError(f"Aggregation error: Column '{column}' not found in the data.")
        
        numeric_data = [float(row[column]) for row in data]
    except ValueError:
        raise ValueError(f"Aggregation error: Column '{column}' contains non-numeric values and cannot be aggregated.")
    except KeyError:
        # This handles the case where the column exists in some rows but not others,
        # or if the data is empty and the check above was skipped.
        raise KeyError(f"Aggregation error: Column '{column}' not found in the data.")


    result = aggregation_func(numeric_data)
    result_key = f"{func_name}({column})"
    
    return {result_key: result}