"""Calculator package."""

from .calculator import Calculator
from .utils import (
    is_number,
    format_result,
    save_history_to_file,
    load_history_from_file,
    validate_operation,
    parse_expression
)

__version__ = "1.0.0"
__author__ = "Your Name"

__all__ = [
    "Calculator",
    "is_number",
    "format_result",
    "save_history_to_file",
    "load_history_from_file",
    "validate_operation",
    "parse_expression"
]
