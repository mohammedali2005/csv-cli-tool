# csv_processor/main_logic.py

import csv
import operator
from typing import List, Dict, Any

from .utils import try_convert_to_float

# Operator mapping for clean conditional logic
OPERATOR_MAP = {
    '>': operator.gt,
    '<': operator.lt,
    '=': operator.eq
}

def load_data(file_path: str) -> List[Dict[str, Any]]:
    """Loads data from a CSV file into a list of dictionaries."""
    try:
        with open(file_path, mode='r', encoding='utf-8') as infile:
            return list(csv.DictReader(infile))
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file at '{file_path}' was not found.")
    except Exception as e:
        raise IOError(f"Error reading or parsing the file: {e}")

def apply_where(data: List[Dict[str, Any]], column: str, op_str: str, value: str) -> List[Dict[str, Any]]:
    """Filters data based on a given condition."""
    if op_str not in OPERATOR_MAP:
        raise ValueError(f"Unsupported operator: '{op_str}'. Supported operators are: >, <, =")
    
    op_func = OPERATOR_MAP[op_str]
    filtered_data = []

    for row in data:
        if column not in row:
            raise KeyError(f"Filtering error: Column '{column}' not found in the data.")
        
        row_value = try_convert_to_float(row[column])
        condition_value = try_convert_to_float(value)

        # Ensure type consistency for comparison
        if type(row_value) != type(condition_value):
            # If one is a float and the other isn't, we can't compare
            if isinstance(row_value, float) or isinstance(condition_value, float):
                 continue # Skip rows that can't be compared
        
        if op_func(row_value, condition_value):
            filtered_data.append(row)
            
    return filtered_data

def apply_orderby(data: List[Dict[str, Any]], column: str, direction: str) -> List[Dict[str, Any]]:
    """Sorts data by a specific column."""
    if direction.lower() not in ['asc', 'desc']:
        raise ValueError(f"Unsupported sort direction: '{direction}'. Use 'asc' or 'desc'.")

    is_reverse = direction.lower() == 'desc'

    if not data or column not in data[0]:
        raise KeyError(f"Sorting error: Column '{column}' not found in the data.")

    # Use a lambda function to handle sorting on values that might be numeric or strings
    return sorted(data, key=lambda row: try_convert_to_float(row.get(column, 0)), reverse=is_reverse)