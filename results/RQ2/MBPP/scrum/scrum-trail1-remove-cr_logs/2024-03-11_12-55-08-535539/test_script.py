def next_Perfect_Square(N):
    if not isinstance(N, int) or N < 0:
        raise ValueError("Input N should be a positive integer")
    import math
    root = math.isqrt(N) + 1
    return root * root
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()