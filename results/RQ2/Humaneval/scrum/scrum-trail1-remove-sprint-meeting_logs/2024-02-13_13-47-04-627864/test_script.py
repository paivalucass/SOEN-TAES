import math

def poly(xs: list, x: float) -> float:
    """Evaluates polynomial with coefficients xs at point x."""
    return sum([coeff * x**i for i, coeff in enumerate(xs)])

def find_zero(xs: list) -> float:
    """xs are coefficients of a polynomial. find_zero find x such that poly(x) = 0."""
    if len(xs) % 2 != 0:
        raise ValueError('Number of coefficients must be even')
    max_coeff = max(xs)
    root = -max_coeff / xs[-2]
    return round(root, 2)
import math
import unittest

class Test(unittest.TestCase):
    def test_find_zero_1(self):
        self.assertEqual(round(find_zero([1, 2]), 2), -0.5)

    def test_find_zero_2(self):
        self.assertEqual(round(find_zero([-6, 11, -6, 1]), 2), 1.0)

if __name__ == '__main__':
    unittest.main()