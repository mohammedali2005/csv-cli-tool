# csv_processor/utils.py

import re
from typing import Tuple, Any, Optional

def parse_condition(condition_str: str) -> Optional[Tuple[str, str, str]]:
    """
    Parses a condition string like "column>value" into its components.
    
    Args:
        condition_str: The string to parse.

    Returns:
        A tuple of (column, operator, value) or None if format is invalid.
    """
    match = re.match(r'^(\w+)\s*([<>=])\s*(.+)$', condition_str)
    if match:
        column, operator, value = match.groups()
        return column, operator, value
    return None

def parse_key_value(param_str: str) -> Optional[Tuple[str, str]]:
    """
    Parses a key-value string like "column=value" into its components.
    
    Args:
        param_str: The string to parse.

    Returns:
        A tuple of (key, value) or None if format is invalid.
    """
    if '=' in param_str:
        return tuple(param_str.split('=', 1))
    return None

def try_convert_to_float(value: Any) -> Any:
    """
    Tries to convert a value to a float, otherwise returns it as is.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return value