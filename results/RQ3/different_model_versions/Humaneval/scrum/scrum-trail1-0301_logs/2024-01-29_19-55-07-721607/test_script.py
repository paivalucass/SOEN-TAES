def fib(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Input should be an integer")
    if n < 0:
        raise ValueError("Input should be a non-negative integer")
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b
import unittest

class TestFib(unittest.TestCase):
    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(fib(2), 1)

    def test_fib_3(self):
        self.assertEqual(fib(3), 2)

    def test_fib_4(self):
        self.assertEqual(fib(4), 3)

    def test_fib_5(self):
        self.assertEqual(fib(5), 5)

    def test_fib_6(self):
        self.assertEqual(fib(6), 8)

    def test_fib_7(self):
        self.assertEqual(fib(7), 13)

    def test_fib_8(self):
        self.assertEqual(fib(8), 21)

    def test_fib_9(self):
        self.assertEqual(fib(9), 34)

    def test_fib_10(self):
        self.assertEqual(fib(10), 55)

if __name__ == '__main__':
    unittest.main()