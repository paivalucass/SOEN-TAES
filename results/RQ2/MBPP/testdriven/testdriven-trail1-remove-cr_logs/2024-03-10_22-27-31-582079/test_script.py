def square_perimeter(a):
    perimeter = 4 * a
    return perimeter
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_perimeter(10), 40)

if __name__ == '__main__':
    unittest.main()