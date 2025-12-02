def largest_divisor(n: int) -> int:
    largest = 1
    for i in range(2, n):
        if n % i == 0:
            largest = i
    return largest
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_divisor(15), 5)

if __name__ == '__main__':
    unittest.main()