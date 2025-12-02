def any_int(x, y, z):
    if not all(isinstance(n, int) for n in [x, y, z]):
        return False
    else:
        return x == abs(y - z) or y == abs(x - z) or z == abs(x - y)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(any_int(5, 2, 7), True)
        self.assertEqual(any_int(3, 2, 2), False)
        self.assertEqual(any_int(3, -2, 1), True)
        self.assertEqual(any_int(3.6, -2.2, 2), False)

if __name__ == '__main__':
    unittest.main()