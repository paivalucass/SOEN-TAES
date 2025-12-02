def amicable_numbers_sum(limit):
    '''Function to sum all amicable numbers from 1 to a specified number'''
    if not isinstance(limit, int):
        return "Error: Invalid input, limit must be a numeric value"
    if limit < 0:
        return "Error: Invalid input, limit cannot be negative"
    if limit > 999:
        return "Error: Limit exceeds maximum allowed value of 999"

    def get_divisors_sum(number):
        divisors_sum = 0
        for i in range(1, number):
            if number % i == 0:
                divisors_sum += i
        return divisors_sum

    amicable_numbers = set()
    for a in range(1, limit):
        b = get_divisors_sum(a)
        if a != b and get_divisors_sum(b) == a and b < limit:
            amicable_numbers.add(a)
            amicable_numbers.add(b)

    return sum(amicable_numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()