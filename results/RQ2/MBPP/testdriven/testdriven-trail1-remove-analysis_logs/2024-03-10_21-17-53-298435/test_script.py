def minimum(a, b):
    return min(a, b)
import unittest

class Test(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(1, 2), 1)

if __name__ == '__main__':
    unittest.main()