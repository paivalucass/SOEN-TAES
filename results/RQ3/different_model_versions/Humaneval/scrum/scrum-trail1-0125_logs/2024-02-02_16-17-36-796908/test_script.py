def derivative(xs: list) -> list:
    if len(xs) < 2:
        return []

    deriv = [xs[i] * i for i in range(1, len(xs))]
    return deriv
import unittest


class Test(unittest.TestCase):
    def test_derivative(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()