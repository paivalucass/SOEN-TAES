def any_int(x, y, z):
    if all(isinstance(i, int) for i in [x, y, z]):
        return any(x == a + b or y == a + b or z == a + b for a, b in [(x, y), (y, z), (x, z)])
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