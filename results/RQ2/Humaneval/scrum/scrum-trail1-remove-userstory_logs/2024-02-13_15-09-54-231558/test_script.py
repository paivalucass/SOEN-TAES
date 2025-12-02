def fibfib(n: int):
    if n < 0:
        raise ValueError("Input n must be a non-negative integer")

    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b, c = 0, 0, 1
    for i in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c
import unittest

class Test(unittest.TestCase):
    def test_fibfib(self):
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(8), 24)

if __name__ == '__main__':
    unittest.main()