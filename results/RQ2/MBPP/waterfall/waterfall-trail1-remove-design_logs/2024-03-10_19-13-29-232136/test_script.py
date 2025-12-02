def find_lucas(n):
    if n < 0:
        return "error handling"
    elif n == 0:
        return 2
    else:
        a, b = 2, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_lucas(9), 76)

if __name__ == '__main__':
    unittest.main()