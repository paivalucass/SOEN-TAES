def count_divisors(num):
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Input must be a positive integer")

    divisor_count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_count += 1
            if i != num // i:
                divisor_count += 1

    return divisor_count % 2 == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_divisors(10) % 2, 0)

if __name__ == '__main__':
    unittest.main()