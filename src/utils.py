"""
Utility functions for the calculator application.
"""

from typing import List, Union
import json
import os


def is_number(value: str) -> bool:
    """Check if a string represents a valid number."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def format_result(result: Union[int, float], precision: int = 2) -> str:
    """Format a numeric result for display."""
    if isinstance(result, int) or result.is_integer():
        return str(int(result))
    return f"{result:.{precision}f}"


def save_history_to_file(history: List[str], filename: str = "calculator_history.json") -> bool:
    """Save calculation history to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump({"history": history}, f, indent=2)
        return True
    except IOError:
        return False


def load_history_from_file(filename: str = "calculator_history.json") -> List[str]:
    """Load calculation history from a JSON file."""
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data.get("history", [])
    except (IOError, json.JSONDecodeError):
        return []


def validate_operation(operation: str) -> bool:
    """Validate if the operation is supported."""
    supported_operations = {'+', '-', '*', '/', '**', 'sqrt'}
    return operation in supported_operations


def parse_expression(expression: str) -> tuple:
    """Parse a simple mathematical expression."""
    expression = expression.replace(' ', '')
    
    # Handle square root
    if expression.startswith('sqrt(') and expression.endswith(')'):
        try:
            number = float(expression[5:-1])
            return ('sqrt', number, None)
        except ValueError:
            raise ValueError("Invalid square root expression")
    
    # Handle binary operations
    for op in ['**', '+', '-', '*', '/']:
        if op in expression:
            parts = expression.split(op, 1)
            if len(parts) == 2:
                try:
                    left = float(parts[0])
                    right = float(parts[1])
                    return (op, left, right)
                except ValueError:
                    continue
    
    raise ValueError("Unable to parse expression")
