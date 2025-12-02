def modp(n: int, p: int):
    if not isinstance(n, int) or not isinstance(p, int):
        raise TypeError
    if n < 0:
        return modp(-n, p)
    if p == 0:
        return None
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * n) % p
        n = n // 2
        n_squared = (n * n) % p
        if n_squared == 0:
            return result
        if n % 2 == 0:
            n = n_squared
    return result
import unittest

class TestModp(unittest.TestCase):
    def test_modp(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()