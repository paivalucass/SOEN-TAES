import math


def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * x ** i for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    roots = np.roots(xs)
    for root in roots:
        if abs(poly(xs, root)) < 1e-6:
            return root
    return None
import unittest

class Test(unittest.TestCase):
    def test_find_zero_1(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)

    def test_find_zero_2(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)

if __name__ == '__main__':
    unittest.main()