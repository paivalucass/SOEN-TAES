def square_perimeter(a):
    if type(a) != int:
        return "Error Message"
    if a <= 0 or a > 1000:
        return "Error Message"
    perimeter = 4 * a
    return perimeter
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_perimeter(10), 40)

if __name__ == '__main__':
    unittest.main()