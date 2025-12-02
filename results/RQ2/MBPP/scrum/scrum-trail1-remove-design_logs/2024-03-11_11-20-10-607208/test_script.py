def is_perfect_square(n):
    if not isinstance(n, (int, float)):
        return "Invalid Input"
    if n < 0:
        return False
    if n == 0:
        return False
    for i in range(1, int(n/2)+2):
        if i*i == n:
            return True
    return False
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