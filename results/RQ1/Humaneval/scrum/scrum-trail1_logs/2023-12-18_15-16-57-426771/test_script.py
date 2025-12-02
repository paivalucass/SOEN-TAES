def fibfib(n: int) -> int:
    memo = [0, 0, 1]
    for i in range(3, n+1):
        fib = memo[i-1] + memo[i-2] + memo[i-3]
        memo.append(fib)
    return memo[n]
import unittest

class TestFibFib(unittest.TestCase):
    def test_fibfib_1(self):
        self.assertEqual(fibfib(1), 0)
    
    def test_fibfib_5(self):
        self.assertEqual(fibfib(5), 4)
        
    def test_fibfib_8(self):
        self.assertEqual(fibfib(8), 24)

if __name__ == '__main__':
    unittest.main()