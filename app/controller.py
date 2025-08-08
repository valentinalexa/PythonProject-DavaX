from app.services.math_services import pow_func, factorial, fibonacci
from app.databases import get_from_cache, save_to_cache, save_to_log
from app.worker import run_async
from datetime import datetime


def pow_operation(x: float, y: float) -> float:
    cached = get_from_cache("pow", x, y)
    if cached is not None:
        print(f"Power {x}^{y} already cached: {cached}")
        return cached

    result = run_async(pow_func, x, y)
    save_to_cache("pow", x, y, result)
    save_to_log("pow", x, y, result)
    return result


def factorial_operation(n: int) -> int:
    cached = get_from_cache("factorial", n, None)
    if cached is not None:
        print(f"Factorial {n} already cached: {cached}")
        return cached

    result = run_async(factorial, n)
    save_to_cache("factorial", n, None, result)
    save_to_log("factorial", n, None, result)
    return result


def fibonacci_operation(n: int) -> int:
    cached = get_from_cache("fibonacci", n, None)
    if cached is not None:
        print(f"Fibonacci {n} already cached: {cached}")
        return cached

    result = run_async(fibonacci, n)
    save_to_cache("fibonacci", n, None, result)
    save_to_log("fibonacci", n, None, result)
    return result
