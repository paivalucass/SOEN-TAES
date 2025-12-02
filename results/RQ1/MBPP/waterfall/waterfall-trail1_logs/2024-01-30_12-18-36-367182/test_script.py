def square_perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Input should be a numeric value")

    if a <= 0:
        raise ValueError("Side length should be a positive number")

    return 4 * a
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_perimeter(10), 40)

if __name__ == '__main__':
    unittest.main()