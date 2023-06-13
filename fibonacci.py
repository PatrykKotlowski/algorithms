"""Module with various implementations of fibonacci sequence."""
from datetime import datetime
from typing import Callable


def basic_fibonacci(n):
    """Basic implementation of fibonacci sequence."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return basic_fibonacci(n-1) + basic_fibonacci(n-2)


def memoization_fibonacci(n):
    """Memoized implementation of fibonacci sequence."""
    memory = {}

    def helper(_n):
        if _n == 0:
            return 0
        if _n == 1:
            return 1
        if _n in memory:
            return memory[_n]
        val = helper(_n-1) + helper(_n-2)
        memory[_n] = val
        return val

    return helper(n)


def tabulation_fibonacci(n):
    """Tabulation implementation of fibonacci sequence."""
    memory = {}

    if n == 0:
        return 0
    if n == 1:
        return 1
    memory[0], memory[1] = 0, 1
    for i in range(2, n):
        memory[i] = memory[i-1] + memory[i-2]
    return memory[n-1] + memory[n-2]


def test_fibonacci(fibonacci: Callable[[int], int]):
    """
    Test fibonacci function

    :param fibonacci: Method which calculates fibonacci sequence for given position
    """
    start = datetime.now()
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(9) == 34
    end = datetime.now()
    print(f"Test took {(end-start).microseconds} microseconds")


if __name__ == '__main__':
    test_fibonacci(basic_fibonacci)
    test_fibonacci(memoization_fibonacci)
    test_fibonacci(tabulation_fibonacci)
