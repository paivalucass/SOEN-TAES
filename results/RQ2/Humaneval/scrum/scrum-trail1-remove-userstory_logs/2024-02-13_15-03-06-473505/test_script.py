import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * x**i for i, coeff in enumerate(xs)])


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
    if xs[-1] == 0:
        raise ValueError('Largest non-zero coefficient must not be 0')
    solutions = []
    for i in range(1, len(xs)):
        x = i * 0.1  # starting point
        prev_x = x
        while True:
            next_x = prev_x - poly(xs, prev_x) / poly([i * coeff for coeff in xs[:-1]], prev_x)
            if abs(next_x - prev_x) < 0.0001:
                solutions.append(round(next_x, 1))
                break
            prev_x = next_x
    return solutions[0]
import math
import unittest

class Test(unittest.TestCase):
    def test_poly(self):
        self.assertEqual(poly([1, 2], 1), 3)

    def test_find_zero(self):
        self.assertEqual(round(find_zero([1, 2]), 2), -0.5)
        self.assertEqual(round(find_zero([-6, 11, -6, 1]), 2), 1.0)

if __name__ == '__main__':
    unittest.main()