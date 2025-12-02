def derivative(xs: list) -> list:
    if not isinstance(xs, list):
        raise TypeError("Input should be a list of numbers")

    if len(xs) < 2:
        return []

    derivative_result = []
    for i in range(1, len(xs)):
        derivative_result.append(xs[i] * i)

    return derivative_result
import unittest

class Test(unittest.TestCase):
    def test_derivative(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()