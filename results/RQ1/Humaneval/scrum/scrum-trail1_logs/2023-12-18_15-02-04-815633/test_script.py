import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
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
        raise ValueError("List must have an even number of coefficients")
    
    largest_coefficient = max(xs, key=abs)
    if largest_coefficient == 0:
        raise ValueError("Largest non-zero coefficient is required for a solution")

    for i in range(len(xs)):
        xs[i] /= largest_coefficient

    epsilon = 1e-10
    x = 1.0
    while abs(poly(xs, x)) > epsilon:
        x = x - poly(xs, x) / poly([i for i in range(len(xs) - 1, 0, -1)], x)
    return x
import unittest
import math

class Test(unittest.TestCase):
    def test_poly(self):
        self.assertEqual(poly([1, 2], 1), 3)
        self.assertEqual(poly([-6, 11, -6, 1], 1), 0)

    def test_find_zero(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)

if __name__ == '__main__':
    unittest.main()