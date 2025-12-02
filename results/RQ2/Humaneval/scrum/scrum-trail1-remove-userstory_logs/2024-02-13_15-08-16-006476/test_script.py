def fib(n: int):
    if n < 0:
        raise ValueError("Input n cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
import unittest

class Test(unittest.TestCase):
    def test_fib_10(self):
        self.assertEqual(fib(10), 55)

    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_8(self):
        self.assertEqual(fib(8), 21)

if __name__ == '__main__':
    unittest.main()