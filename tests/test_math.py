# tests/test_math.py

from app.services.math_services import pow_func, factorial, fibonacci

def test_pow_func():
    assert pow_func(2, 3) == 8
    assert pow_func(5, 0) == 1

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(6) == 8
