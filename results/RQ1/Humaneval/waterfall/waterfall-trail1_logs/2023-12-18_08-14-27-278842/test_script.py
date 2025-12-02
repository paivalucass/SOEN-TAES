def modp(n: int, p: int) -> int:
    if not isinstance(n, int) or not isinstance(p, int) or n < 0 or p < 0:
        raise ValueError("n and p must be positive integers")
    if p == 0:
        raise ValueError("p cannot be zero")
    result = pow(2, n, p)
    return result
import unittest

class Test(unittest.TestCase):
    def test_modp(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()