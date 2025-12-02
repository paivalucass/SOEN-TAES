def derivative(xs: list) -> list:
    if len(xs) <= 1:
        return [0]

    derivative_coeffs = [xs[i] * i for i in range(1, len(xs))]
    return derivative_coeffs
import unittest

class Test(unittest.TestCase):
    def test_derivative1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()