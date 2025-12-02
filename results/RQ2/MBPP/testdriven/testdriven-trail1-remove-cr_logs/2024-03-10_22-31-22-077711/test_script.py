def sum_of_divisors(n):
    return sum([i for i in range(1, n) if n % i == 0])

def amicable_numbers_sum(limit):
    amicable_sum = 0
    for a in range(1, limit):
        b = sum_of_divisors(a)
        if a != b and sum_of_divisors(b) == a:
            amicable_sum += a
    return amicable_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()