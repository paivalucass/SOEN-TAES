import math

def poly(xs: list, x: float) -> float:
    """Evaluates polynomial with coefficients xs at point x."""
    return sum([coeff * x**i for i, coeff in enumerate(xs)])

def find_zero(xs: list) -> float:
    """Find zero point of polynomial with coefficients xs."""
    if len(xs) % 2 != 0:
        raise ValueError("Input list 'xs' must have an even number of coefficients")
    return -xs[1] / xs[0]
import unittest

class Test(unittest.TestCase):
    def test_find_zero_1(self):
        self.assertEqual(round(find_zero([1, 2]), 2), -0.5)

    def test_find_zero_2(self):
        self.assertEqual(round(find_zero([-6, 11, -6, 1]), 2), 1.0)

if __name__ == '__main__':
    unittest.main()