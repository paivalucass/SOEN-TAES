def fib4(n: int):
    a, b, c, d = 0, 0, 2, 0
    for i in range(4, n+1):
        a, b, c, d = b, c, d, a + b + c + d
    return d
import unittest

class Test(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()