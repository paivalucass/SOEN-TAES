import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    if len(xs) % 2 != 0:
        raise ValueError('Number of coefficients must be even')
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


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
    if len(xs) % 2 != 0:
        raise ValueError('Number of coefficients must be even')
    roots = [i for i in range(-100, 101) if poly(xs, i) == 0]
    if len(roots) > 0:
        return roots[0]
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test_poly(self):
        self.assertEqual(poly([1, 2], 1), 3) # 1 + 2*1 = 3
        self.assertEqual(poly([-6, 11, -6, 1], 2), 0) # -6 + 11*2 - 6*2^2 + 2^3 = 0

    def test_find_zero(self):
        self.assertEqual(round(find_zero([1, 2]), 2), -0.5) # f(x) = 1 + 2x => zero at -0.5
        self.assertEqual(round(find_zero([-6, 11, -6, 1]), 2), 1.0) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3 => zero at 1.0

if __name__ == '__main__':
    unittest.main()