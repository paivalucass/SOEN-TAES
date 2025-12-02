def fibfib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    a, b, c = 0, 0, 1
    for _ in range(3, n+1):
        a, b, c = b, c, a + b + c
    return c
import unittest

class Test(unittest.TestCase):
    def test_fibfib_1(self):
        self.assertEqual(fibfib(1), 0)

    def test_fibfib_5(self):
        self.assertEqual(fibfib(5), 4)

    def test_fibfib_8(self):
        self.assertEqual(fibfib(8), 24)

if __name__ == '__main__':
    unittest.main()