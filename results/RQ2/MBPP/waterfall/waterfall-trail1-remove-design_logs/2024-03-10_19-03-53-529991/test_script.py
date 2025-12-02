def square_perimeter(a):
    if isinstance(a, (int, float)):
        return 4 * a
    else:
        return "InvalidInputError"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_perimeter(10), 40)

if __name__ == '__main__':
    unittest.main()