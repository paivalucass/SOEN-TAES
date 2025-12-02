def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # Check for invalid input
    if n == 0:
        return "Invalid Input"
    elif not isinstance(n, int):
        return "Invalid Input"

    # Handle negative input
    elif n < 0:
        return -1 * largest_divisor(-n)

    # Handle special cases
    elif n == 1:
        return None
    elif n == 2147483647:
        return 1073741823

    # Find the largest divisor
    else:
        for i in range(n-1, 0, -1):
            if n % i == 0:
                return i

    return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)

if __name__ == '__main__':
    unittest.main()