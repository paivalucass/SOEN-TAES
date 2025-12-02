def derivative(xs: list):
    result = [xs[i] * i for i in range(1, len(xs))]
    return result

print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
import unittest

class Test(unittest.TestCase):
    def test_derivative_1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative_2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()