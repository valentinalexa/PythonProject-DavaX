# app/services/math_service.py

def pow_func(x: float, y: float) -> float:
    """Return x raised to the power of y."""
    return x ** y


def factorial(n: int) -> int:
    """Return the factorial of n (non-negative integer)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


