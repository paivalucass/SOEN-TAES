def opposite_Signs(x, y):
    return (x < 0) != (y < 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(opposite_Signs(1, -2), True)

if __name__ == '__main__':
    unittest.main()