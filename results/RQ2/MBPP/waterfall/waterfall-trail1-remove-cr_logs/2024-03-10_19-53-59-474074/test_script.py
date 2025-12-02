def amicable_numbers_sum(limit):
    '''Write a function to sum all amicable numbers from 1 to a specified number.'''
    sum_amicable = 0
    for num in range(1, limit + 1):
        divisor_sum = sum([i for i in range(1, num) if num % i == 0])
        if divisor_sum != num and sum([i for i in range(1, divisor_sum) if divisor_sum % i == 0]) == num:
            sum_amicable += num
    return sum_amicable
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()