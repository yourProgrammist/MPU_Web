from functools import lru_cache
import time

@lru_cache(10000)
def fact_rec(n: int) -> int:
    """
    Recursively calculates the factorial of n
    :param n: int
    :return: int
    """
    if n == 1:
        return n
    return n * fact_rec(n - 1)

def fact_it(n: int) -> int:
    """
    Iteratively calculates the factorial of n
    :param n: int
    :return: int
    """
    basis = 1
    for i in range(2, n + 1):
        basis *= i
    return basis



# n = 400
# fact_rec - 0.0002992153167724 s
# fact_it  - 0.0000591278076172 s
# fact_it < fact_rec