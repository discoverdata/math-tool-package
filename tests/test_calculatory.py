from src.lib.calculator import add, substract, multiply, divide
import pytest

def test_add():
    assert add(3,5) == 8

def test_substract():
    assert substract(5,2) == 3

def test_multiply():
    assert multiply(2,4) == 8

def test_divide():
    assert divide(4,2) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError, match = "Division by zero is not allowed"):
        divide (5,0)

