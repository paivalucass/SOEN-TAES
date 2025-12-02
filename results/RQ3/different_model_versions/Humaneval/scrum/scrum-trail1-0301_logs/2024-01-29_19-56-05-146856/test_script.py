def derivative(xs: list):
    if len(xs) < 2:
        raise ValueError("Input list of coefficients must have at least two elements.")
    
    derived_xs = xs[1:]
    new_xs = [i * xs[i] for i in range(1, len(xs))]
    return new_xs
import unittest


class TestDerivative(unittest.TestCase):
    def test_derivative1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])


if __name__ == '__main__':
    unittest.main()