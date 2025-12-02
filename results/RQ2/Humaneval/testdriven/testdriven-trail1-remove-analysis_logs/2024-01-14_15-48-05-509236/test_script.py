def fib4(n: int):
    if n < 0 or type(n) != int:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        a, b, c, d = 0, 0, 2, 0
        for i in range(4, n+1):
            a, b, c, d = b, c, d, a + b + c + d
        return d
import unittest

class TestFib4(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()