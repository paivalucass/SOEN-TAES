def closest_num(N):
    if N <= 0:
        return -1
    else:
        return N - 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()