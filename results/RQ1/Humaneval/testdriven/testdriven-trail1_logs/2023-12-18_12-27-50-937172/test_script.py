import numpy as np

def derivative(xs: list) -> list:
    return np.polyder(xs).coeffs.tolist()
import unittest

class Test(unittest.TestCase):
    def test_derivative_1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative_2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()