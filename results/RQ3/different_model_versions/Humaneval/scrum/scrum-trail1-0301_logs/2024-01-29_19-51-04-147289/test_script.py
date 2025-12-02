import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def poly_derivative(xs: list, x: float) -> float:
    """
    Calculates the derivative of a polynomial with coefficients xs at point x.
    Returns the derivative of the polynomial at point x.
    """
    return sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs) if i > 0])

def find_zero(xs: list, max_iter: int = 100) -> float:
    """
    Finds an approximate zero point of the polynomial with coefficients xs
    using the Newton-Raphson method.
    Returns only one zero point, even if there are many.
    It takes a list xs having an even number of coefficients and largest non-zero
    coefficient as it guarantees a solution.
    If there are odd number of coefficients or the largest coefficient is zero,
    the function will raise a ValueError with an appropriate error message.
    The maximum number of iterations can be set by the user.
    """
    if len(xs) % 2 != 0 or xs[0] == 0:
        raise ValueError("Invalid input: List must have even number of coefficients and the largest coefficient must be non-zero.")
    
    if poly(xs, 1.0) == 0:
        return 1.0

    x0 = 1.0
    f = lambda x: poly(xs, x)
    fp = lambda x: poly_derivative(xs, x)

    eps = 0.0001

    for i in range(max_iter):
        x1 = x0 - f(x0)/fp(x0)

        if abs(x1 - x0) < eps:
            return x1

        x0 = x1

    raise RuntimeError("Method did not converge within the specified number of iterations.")
import unittest
import math

class Test(unittest.TestCase):
    def test_find_zero(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)

    def test_poly(self):
        self.assertAlmostEqual(poly([1, 2], 0), 1, places=2)
        self.assertAlmostEqual(poly([1, 2], 1), 3, places=2)
        self.assertAlmostEqual(poly([-6, 11, -6, 1], 1), 0, places=2)

if __name__ == '__main__':
    unittest.main()

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ 
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("Input list must have even number of coefficients and largest non-zero coefficient")

    # Calculate the discriminant
    a = xs[-2]
    b = xs[-3]
    c = xs[-4]
    disc = b * b - 4 * a * c

    # Find the roots
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)

    # Return the root that is not imaginary and has the correct sign
    if root1.real != root1 or root1 < 0:
        return root2.real
    else:
        return root1.real