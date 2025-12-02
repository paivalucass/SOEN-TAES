def closest_num(N):
    if not isinstance(N, int):
        raise ValueError("Input must be an integer")
    if N < 1:
        return -1
    closest_smaller = N - 1
    return closest_smaller
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()