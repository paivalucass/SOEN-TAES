def fib4(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    if n < 0:
        return "Invalid input"
    
    a, b, c, d = 0, 0, 2, 0
    if n <= 3:
        return a + b + c + d
    else:
        for _ in range(4, n + 1):
            a, b, c, d = b, c, d, a + b + c + d
        return a + b + c + d
import unittest

class Test(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()