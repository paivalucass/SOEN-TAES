def largest_divisor(n: int) -> int:
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_divisor(15), 5)

if __name__ == '__main__':
    unittest.main()