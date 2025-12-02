def divisor(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"

    count = 0
    sqrt_n = int(n ** 0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i == sqrt_n and n / i == i:
                count += 1
            else:
                count += 2
    return count

# Test Cases:
assert divisor(15) == 4
assert divisor(0) == "Error: Input must be a positive integer"
assert divisor(-15) == "Error: Input must be a positive integer"
assert divisor(1000000) == 100
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisor(15), 4)

if __name__ == '__main__':
    unittest.main()