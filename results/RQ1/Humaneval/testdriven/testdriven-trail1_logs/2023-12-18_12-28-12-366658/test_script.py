def fibfib(n: int) -> int:
    memoization = {}
    
    def compute_fib(m: int) -> int:
        if m in memoization:
            return memoization[m]
        if m == 0:
            return 0
        if m == 1:
            return 0
        if m == 2:
            return 1
        result = compute_fib(m-1) + compute_fib(m-2) + compute_fib(m-3)
        memoization[m] = result
        return result
    
    if n < 0:
        raise ValueError("Input value cannot be negative")
    if n > 100:
        raise ValueError("Input value is too large")
    
    return compute_fib(n)
import unittest

class Test(unittest.TestCase):
    def test_fibfib(self):
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(8), 24)

if __name__ == '__main__':
    unittest.main()