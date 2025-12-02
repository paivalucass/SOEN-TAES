def closest_num(N):
    closest_smaller = N - 1
    assert closest_smaller < N, "The closest smaller number should be less than N"
    return closest_smaller
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()