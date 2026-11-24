# Module inside mypackage: math_operations.py

def power(base, exponent):
    """Calculates base raised to the power of exponent."""
    return base ** exponent

def factorial(n):
    """Calculates the factorial of n using a loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
