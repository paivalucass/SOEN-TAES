def any_int(x, y, z):
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False

    if x == y + z or y == x + z or z == x + y:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(any_int(5, 2, 7), True)
        self.assertEqual(any_int(3, 2, 2), False)
        self.assertEqual(any_int(3, -2, 1), True)
        self.assertEqual(any_int(3.6, -2.2, 2), False)

if __name__ == '__main__':
    unittest.main()