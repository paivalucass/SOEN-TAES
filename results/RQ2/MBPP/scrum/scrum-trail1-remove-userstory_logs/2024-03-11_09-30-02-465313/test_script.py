def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(9))
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(10))

if __name__ == '__main__':
    unittest.main()