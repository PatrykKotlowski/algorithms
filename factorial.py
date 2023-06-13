from datetime import datetime
from typing import Callable


def recursive_factorial(n):
    """Recursive implementation of factorial."""
    if n == 0:
        return 1
    return n * recursive_factorial(n-1)


def memoize_factorial(n):
    """Memoized implementation of factorial."""
    memory = {0: 1}

    def helper(_n):
        if _n in memory:
            return memory[_n]
        val = _n * helper(_n-1)
        memory[_n] = val

        return val

    return helper(n)


def tabulation_factorial(n):
    """Tabulation implementation of factorial."""
    memory = {0: 1}
    if n == 0:
        return memory[0]
    for i in range(1, n):
        memory[i] = i * memory[i-1]

    return n * memory[n-1]


def tabulation_only_one_value_factorial(n):
    """Tabulation implementation of factorial with storing only one value."""
    if n == 0:
        return 1
    previous = 1
    for i in range(1, n):
        previous = i * previous

    return n * previous


def test_factorial(factorial_func: Callable[[int], int]):
    """
    Test factorial functions

    :param factorial_func: Factorial function to be tested
    """
    start = datetime.now()
    assert factorial_func(0) == 1
    assert factorial_func(1) == 1
    assert factorial_func(2) == 2
    assert factorial_func(4) == 24
    assert factorial_func(8) == 40320
    end = datetime.now()
    print(f"Function took {(end - start).microseconds} microseconds")


if __name__ == '__main__':
    test_factorial(recursive_factorial)
    test_factorial(memoize_factorial)
    test_factorial(tabulation_factorial)
    test_factorial(tabulation_only_one_value_factorial)
