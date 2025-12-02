def test_three_equal(x, y, z):
    if x == y == z:
        return 3
    else:
        return len(set([x, y, z]))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_three_equal(1, 1, 1), 3)

if __name__ == '__main__':
    unittest.main()