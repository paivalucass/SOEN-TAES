def derivative(xs: list):
    if len(xs) == 0:
        raise ValueError("Error: Empty input list")
    if not all(isinstance(x, (int, float)) for x in xs):
        raise ValueError("Error: Input list contains non-numeric values")

    result = []
    for i in range(1, len(xs)):
        result.append(xs[i] * i)

    return result
import unittest

class Test(unittest.TestCase):
    def test_derivative(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()