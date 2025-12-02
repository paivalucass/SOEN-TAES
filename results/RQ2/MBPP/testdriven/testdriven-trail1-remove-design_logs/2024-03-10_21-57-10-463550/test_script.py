def closest_num(N):
    return abs(N) - 1 if N != 0 else -1
import unittest

class Test(unittest.TestCase):
    def test_closest_num(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()