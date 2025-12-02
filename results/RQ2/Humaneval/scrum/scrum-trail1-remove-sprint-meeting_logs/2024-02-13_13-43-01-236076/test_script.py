def largest_divisor(n: int) -> int:
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return i
    return 1
import unittest

class Test(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)

if __name__ == '__main__':
    unittest.main()