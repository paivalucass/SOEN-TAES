def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x == y + z or y == x + z or z == x + y:
            return True
        else:
            return False
    else:
        return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3.6, -2.2, 2))

if __name__ == '__main__':
    unittest.main()