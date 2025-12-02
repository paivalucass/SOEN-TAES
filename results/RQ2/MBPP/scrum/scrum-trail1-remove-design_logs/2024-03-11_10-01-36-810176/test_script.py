def closest_num(N):
    if not isinstance(N, int):
        return "Error"
    if N <= 0:
        return "N is already the smallest possible value"
    return N - 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()