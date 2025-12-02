def largest_divisor(n: int) -> int:
    if n <= 1:
        return 1
    largest_div = 1
    for i in range(2, n):
        if n % i == 0:
            largest_div = i
    return largest_div
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_divisor(15), 5)

if __name__ == '__main__':
    unittest.main()