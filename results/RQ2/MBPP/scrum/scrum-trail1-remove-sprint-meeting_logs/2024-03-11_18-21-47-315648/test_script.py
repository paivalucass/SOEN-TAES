def amicable_numbers_sum(limit):
    '''
    Write a function to sum all amicable numbers from 1 to a specified number.
    assert amicable_numbers_sum(999)==504
    '''

    def calculate_divisors(num):
        divisors = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        return divisors

    def verify_amicable_numbers_sum(num1, num2):
        sum1 = sum(calculate_divisors(num1)) - num1
        sum2 = sum(calculate_divisors(num2)) - num2
        if sum1 == num2 and sum2 == num1:
            return True
        else:
            return False

    if not isinstance(limit, int) or limit < 1:
        raise ValueError("Limit must be a positive integer")

    amicable_sum = 0
    for i in range(1, limit + 1):
        for j in range(i + 1, limit + 1):
            if verify_amicable_numbers_sum(i, j):
                amicable_sum += i + j

    return amicable_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()