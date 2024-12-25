# src/lib/calculator.py

def add(x: float, y: float) -> float:
    """
    returns sum of two numbers
    """

    return x + y


def substract(x: float, y: float) -> float:
    """
    returns difference of two numbers
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """
    returns product of two numbers
    """
    return x * y


def divide(x: float, y: float) -> float:
    """
    returns product of two numbers
    """
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y
