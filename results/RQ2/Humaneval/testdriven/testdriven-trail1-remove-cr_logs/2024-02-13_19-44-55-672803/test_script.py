def fib4(n: int):
    result = [0, 0, 2, 0]
    if n <= 3:
        return result[n]
    for i in range(4, n+1):
        next_fib = result[3] + result[2] + result[1] + result[0]
        result[0] = result[1]
        result[1] = result[2]
        result[2] = result[3]
        result[3] = next_fib
    return result[3]
import unittest

class Test(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()