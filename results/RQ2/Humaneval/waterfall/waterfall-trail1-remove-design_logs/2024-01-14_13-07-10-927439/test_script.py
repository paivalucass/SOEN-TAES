import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    if len(xs) % 2 != 0:
        raise ValueError("Input list must have an even number of coefficients")
    if max(xs, key=abs) == 0:
        raise ValueError("Largest coefficient must be non-zero")
    epsilon = 1e-10
    for i in range(-100, 101):
        if abs(poly(xs, i)) < epsilon:
            return i
import math

class Test(unittest.TestCase):
    def test_find_zero_1(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, 2)

    def test_find_zero_2(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, 2)

if __name__ == '__main__':
    unittest.main()