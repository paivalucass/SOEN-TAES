def hexagonal_num(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    memoization_cache = {}

    def calculate_hexagonal_num(n):
        return n * (2 * n - 1)

    def memoize(func):
        cache = {}
        def wrapper(n):
            if n not in cache:
                cache[n] = func(n)
            return cache[n]
        return wrapper

    calculate_hexagonal_num = memoize(calculate_hexagonal_num)

    return calculate_hexagonal_num(n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hexagonal_num(10), 190)

if __name__ == '__main__':
    unittest.main()