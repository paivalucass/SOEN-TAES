import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list) -> float:
    n = len(xs)
    if n % 2 != 0 or xs[-1] == 0:
        raise ValueError("Input coefficients array must have an even number of elements and the largest non-zero coefficient must be present")
    
    def f(x):
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    
    x1 = 1.0
    x2 = 2.0
    while abs(x1 - x2) >= 1e-6:
        f1 = f(x1)
        f2 = f(x2)
        x1, x2 = x2, x2 - f2 * (x2 - x1) / (f2 - f1)
    
    return x1
import unittest
import math

class Test(unittest.TestCase):
    def test_poly(self):
        self.assertEqual(poly([1, 2], 1), 3)
        self.assertEqual(poly([-6, 11, -6, 1], 2), 0)

    def test_find_zero(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)

if __name__ == '__main__':
    unittest.main()