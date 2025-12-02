def perfect_squares(a, b):
    if a < 0 or b < 0 or a > b:
        raise ValueError("Input values must be positive integers and a must be less than or equal to b")

    result = [x**2 for x in range(int(a ** 0.5), int(b ** 0.5) + 1)]
    return result
import unittest

class Test(unittest.TestCase):
    def test_perfect_squares(self):
        self.assertEqual(perfect_squares(1, 30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()