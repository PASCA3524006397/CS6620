"""
Tests for the utils module.
"""

import pytest
import json
import os
import tempfile
from src.utils import (
    is_number,
    format_result,
    save_history_to_file,
    load_history_from_file,
    validate_operation,
    parse_expression
)


class TestUtils:
    """Test cases for utility functions."""
    
    def test_is_number(self):
        """Test number validation."""
        assert is_number("123") is True
        assert is_number("123.45") is True
        assert is_number("-67") is True
        assert is_number("0") is True
        assert is_number("abc") is False
        assert is_number("") is False
        assert is_number("12.34.56") is False
    
    def test_format_result(self):
        """Test result formatting."""
        assert format_result(5) == "5"
        assert format_result(5.0) == "5"
        assert format_result(3.14159, 2) == "3.14"
        assert format_result(3.14159, 4) == "3.1416"
        assert format_result(-2.5) == "-2.5"
    
    def test_save_and_load_history(self):
        """Test saving and loading history to/from file."""
        history = ["2 + 3 = 5", "4 * 5 = 20"]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            filename = f.name
        
        try:
            # Test saving
            assert save_history_to_file(history, filename) is True
            assert os.path.exists(filename)
            
            # Test loading
            loaded_history = load_history_from_file(filename)
            assert loaded_history == history
            
        finally:
            if os.path.exists(filename):
                os.unlink(filename)
    
    def test_load_nonexistent_file(self):
        """Test loading from non-existent file."""
        result = load_history_from_file("nonexistent_file.json")
        assert result == []
    
    def test_validate_operation(self):
        """Test operation validation."""
        assert validate_operation('+') is True
        assert validate_operation('-') is True
        assert validate_operation('*') is True
        assert validate_operation('/') is True
        assert validate_operation('**') is True
        assert validate_operation('sqrt') is True
        assert validate_operation('%') is False
        assert validate_operation('invalid') is False
    
    def test_parse_expression(self):
        """Test expression parsing."""
        assert parse_expression("2+3") == ('+', 2.0, 3.0)
        assert parse_expression("10 - 5") == ('-', 10.0, 5.0)
        assert parse_expression("4*6") == ('*', 4.0, 6.0)
        assert parse_expression("8/2") == ('/', 8.0, 2.0)
        assert parse_expression("2**3") == ('**', 2.0, 3.0)
        assert parse_expression("sqrt(9)") == ('sqrt', 9.0, None)
    
    def test_parse_invalid_expression(self):
        """Test parsing invalid expressions."""
        with pytest.raises(ValueError, match="Unable to parse expression"):
            parse_expression("invalid")
        
        with pytest.raises(ValueError, match="Invalid square root expression"):
            parse_expression("sqrt(abc)")
