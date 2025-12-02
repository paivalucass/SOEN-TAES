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
    roots = [coeff for coeff in xs if coeff != 0]
    degree = len(roots) - 1
    if degree % 2 != 0:
        degree -= 1
    for x in range(1, 100):
        if round(sum([coeff * x ** (degree - i) for i, coeff in enumerate(xs)]), 2) == 0:
            return round(x, 2)
import math
import unittest

class Test(unittest.TestCase):
    def test_find_zero_1(self):
        self.assertEqual(round(find_zero([1, 2]), 2), -0.5)

    def test_find_zero_2(self):
        self.assertEqual(round(find_zero([-6, 11, -6, 1]), 2), 1.0)

if __name__ == '__main__':
    unittest.main()