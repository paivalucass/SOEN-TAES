def fib4(n: int):
    # The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    # fib4(0) -> 0
    # fib4(1) -> 0
    # fib4(2) -> 2
    # fib4(3) -> 0
    # fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    # Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    
    a, b, c, d = 0, 0, 2, 0
    for _ in range(4, n+1):
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