def is_polite(n):
    if n <= 0:
        return "Input validation error"
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for i in range(3, n+1):
            c = a + b + 1
            a, b = b, c - 1
        return c - 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()