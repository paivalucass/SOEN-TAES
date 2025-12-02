def opposite_signs(x, y):
    return (x < 0) != (y < 0)
import unittest

class Test(unittest.TestCase):
    def test_opposite_signs(self):
        self.assertTrue(opposite_signs(1, -2))

if __name__ == '__main__':
    unittest.main()