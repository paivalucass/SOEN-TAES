def perimeter_pentagon(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError("side_length must be a non-negative numeric value")
    perimeter = 5 * side_length
    return perimeter
import unittest

class Test(unittest.TestCase):
    def test_perimeter_pentagon(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()