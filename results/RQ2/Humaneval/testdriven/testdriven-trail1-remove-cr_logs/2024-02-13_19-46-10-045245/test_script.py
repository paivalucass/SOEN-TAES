def derivative(xs: list):
    if not isinstance(xs, list):
        raise TypeError("Input coefficients must be provided in a list")

    if not all(isinstance(x, (int, float)) for x in xs):
        raise ValueError("Input coefficients must be numbers")

    derivative_coeffs = [coefficient * power for power, coefficient in enumerate(xs)][1:]

    return derivative_coeffs

import unittest

class Test(unittest.TestCase):
    def test_derivative1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()