def median_trapezium(base1, base2, height):
    if base1 <= 0 or base2 <= 0 or height <= 0:
        return "Invalid Input"
    else:
        return ((base1 + base2) * height) / 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_trapezium(15, 25, 35), 20)

if __name__ == '__main__':
    unittest.main()