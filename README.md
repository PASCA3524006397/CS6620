Quick Setup
bash# Clone and enter directory
git clone[ https://github.com/yourusername/calculator-project.git](https://github.com/PASCA3524006397/CS6620)
cd calculator-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
Usage
pythonfrom src.calculator import Calculator

calc = Calculator()
print(calc.add(5, 3))        # 8
print(calc.multiply(4, 6))   # 24
print(calc.get_history())    # ['5 + 3 = 8', '4 * 6 = 24']
Running Tests
bash# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_calculator.py
Code Quality
bash# Lint code
flake8 .

# Check security
safety check
bandit -r src/
Project Structure
calculator-project/
├── src/                 # Source code
│   ├── calculator.py    # Main Calculator class
│   └── utils.py         # Utility functions
├── tests/               # Test files
├── .github/workflows/   # CI/CD pipeline
└── requirements*.txt    # Dependencies
Features

Basic arithmetic operations (add, subtract, multiply, divide, power, square root)
Calculation history tracking
File I/O for saving/loading history
Expression parsing
100% test coverage
Automated CI/CD with GitHub Actions

CI/CD
The workflow runs automatically on:

Pushes to main or develop
Pull requests
Manual trigger (Actions tab → Run workflow)

Tests run on Python 3.8, 3.9, 3.10, and 3.11 with linting and security checks.
