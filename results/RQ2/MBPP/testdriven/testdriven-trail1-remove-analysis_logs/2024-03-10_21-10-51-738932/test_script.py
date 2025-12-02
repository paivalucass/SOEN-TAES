def amicable_numbers_sum(limit):
    '''Write a function to sum all amicable numbers from 1 to a specified number.'''
    # Write your code here
    amicable_numbers = []
    for num in range(1, limit):
        if is_amicable(num):
            amicable_numbers.append(num)
    return sum(amicable_numbers)

def is_amicable(n):
    sum_divisors = sum(get_divisors(n))
    if sum_divisors == n:
        return False
    return n == sum(get_divisors(sum_divisors))

def get_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.extend([i, n//i])
    return divisors

assert amicable_numbers_sum(999)==504
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()