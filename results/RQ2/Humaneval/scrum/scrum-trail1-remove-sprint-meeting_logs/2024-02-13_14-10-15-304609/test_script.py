def any_int(x, y, z):
    return (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)) and ((x == y + z) or (y == x + z) or (z == x + y))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(any_int(5, 2, 7), True)
        self.assertEqual(any_int(3, 2, 2), False)
        self.assertEqual(any_int(3, -2, 1), True)
        self.assertEqual(any_int(3.6, -2.2, 2), False)

if __name__ == '__main':
    unittest.main()