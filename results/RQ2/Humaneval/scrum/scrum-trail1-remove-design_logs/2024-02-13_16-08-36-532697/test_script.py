def derivative(xs: list, step: int = 1) -> list:
    if len(xs) < 2:
        return [0]
    
    result = [xs[i] * i * step for i in range(1, len(xs))]
    return result
import unittest

class Test(unittest.TestCase):
    def test_derivative_example1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative_example2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()