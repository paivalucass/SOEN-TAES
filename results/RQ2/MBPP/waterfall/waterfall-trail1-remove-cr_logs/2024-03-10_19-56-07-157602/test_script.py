def perimeter_pentagon(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Input length must be a number")
    if side_length <= 0:
        raise ValueError("Input length must be a positive number")

    perimeter = 5 * side_length

    return perimeter
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perimeter_pentagon(5), 25)

if __name__ == '__main__':
    unittest.main()