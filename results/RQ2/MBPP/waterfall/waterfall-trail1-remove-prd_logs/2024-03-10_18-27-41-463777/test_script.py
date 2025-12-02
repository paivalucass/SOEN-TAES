def closest_num(N: int) -> int:
    if not isinstance(N, int):
        raise ValueError("Input N must be an integer")

    if N <= 0:
        raise ValueError("Input N must be a positive integer")

    result = N - 1
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()