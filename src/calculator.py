"""
A simple calculator module for demonstration purposes.
"""

from typing import Union
import math


class Calculator:
    """A calculator class with basic arithmetic operations."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Raise base to the power of exponent."""
        result = math.pow(base, exponent)
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def square_root(self, x: Union[int, float]) -> float:
        """Calculate square root of x."""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(x)
        self.history.append(f"√{x} = {result}")
        return result
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
    
    def get_history(self) -> list:
        """Get calculation history."""
        return self.history.copy()
