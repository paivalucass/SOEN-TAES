def opposite_Signs(x, y):
    if (x < 0 and y > 0) or (x > 0 and y < 0):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(opposite_Signs(1, -2), True)

if __name__ == '__main__':
    unittest.main()