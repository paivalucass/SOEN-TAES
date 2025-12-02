def derivative(xs: list):
    if not xs:
        raise ValueError("Empty list not allowed")

    if not all(isinstance(x, (int, float)) for x in xs):
        raise ValueError("Non-numeric coefficients not allowed")

    n = len(xs)
    if n == 1:
        return [0]

    result = [xs[i] * i for i in range(1, n)]
    return result
import unittest

class Test(unittest.TestCase):
    def test_derivative_1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative_2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()