def largest_divisor(n: int) -> int:
    """ 
    For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n <= 0:
        raise ValueError("Input should be a positive integer")

    largest_divisor = 1
    for i in range(1, n):
        if n % i == 0:
            largest_divisor = i

    if largest_divisor == n:
        return 1  # if n is a prime number, return 1 as the largest divisor
    else:
        return largest_divisor

import unittest

class Test(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)

if __name__ == '__main__':
    unittest.main()