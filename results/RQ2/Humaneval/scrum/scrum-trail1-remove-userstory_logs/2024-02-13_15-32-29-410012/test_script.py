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
        raise ValueError('The list of coefficients must have an even number of elements')
    max_nonzero_coefficient = max(xs, key=abs)
    if max_nonzero_coefficient == 0:
        raise ValueError('All coefficients are zero')
    roots = []
    for i in range(len(xs)):
        if(xs[i] == 0):
            continue
        for j in range(i + 1, len(xs)):
            if(xs[j] == 0):
                continue
            root = -xs[i] / xs[j]
            if(poly(xs, root) == 0):
                roots.append(round(root, 2))
    return roots[0]

import math

class Test(unittest.TestCase):
    def test_find_zero_1(self):
        self.assertEqual(find_zero([1, 2]), -0.5)

    def test_find_zero_2(self):
        self.assertEqual(find_zero([-6, 11, -6, 1]), 1.0)

if __name__ == '__main__':
    unittest.main()