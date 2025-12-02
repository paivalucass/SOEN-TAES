def fibfib(n: int) -> int:
    if n < 0:
        raise ValueError("Input value cannot be negative")
    elif not isinstance(n, int):
        raise TypeError("Input value must be an integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            temp = a + b + c
            a, b, c = b, c, temp
        return c
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