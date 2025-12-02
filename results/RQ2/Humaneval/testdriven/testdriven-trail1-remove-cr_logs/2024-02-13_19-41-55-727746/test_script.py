import math

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    try:
        result = math.gcd(a, b)
        return result
    except TypeError:
        raise TypeError("Inputs must be integers")
    except ValueError:
        raise ValueError("Inputs must be non-negative")

import unittest

class Test(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()