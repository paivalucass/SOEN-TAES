def modp(n: int, p: int) -> int:
    result = 1
    base = 2 % p
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        n = n // 2
        base = (base * base) % p
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