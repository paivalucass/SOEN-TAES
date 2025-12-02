import math
def count_divisors(n) :
    if n < 1:
        return "Error: Input must be a positive integer"
    if n == 1:
        return False

    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:  # Check for perfect square
                count += 1
            else:
                count += 2
    return count % 2 == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_divisors(10) % 2, 0)

if __name__ == '__main__':
    unittest.main()