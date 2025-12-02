def derivative(xs: list) -> list:
    if len(xs) < 2:
        raise ValueError("Input list must have at least two elements for derivative calculation")
    
    return [xs[i] * i for i in range(1, len(xs))]
import unittest

class Test(unittest.TestCase):
    def test_derivative(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()