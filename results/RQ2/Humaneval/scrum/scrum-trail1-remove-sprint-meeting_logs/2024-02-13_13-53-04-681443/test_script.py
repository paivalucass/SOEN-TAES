def fib4(n: int) -> int:
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2
    result = [0, 0, 2, 0]
    for i in range(4, n + 1):
        result[i % 4] = result[(i - 1) % 4] + result[(i - 2) % 4] + result[(i - 3) % 4] + result[(i - 4) % 4]
    return result[n % 4]
import unittest

class Test(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()