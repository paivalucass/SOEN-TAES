def amicable_numbers_sum(limit):
    '''Write a function to sum all amicable numbers from 1 to a specified number.
    assert amicable_numbers_sum(999)==504'''

    if not isinstance(limit, int) or limit < 1:
        return "Invalid Input"
    
    def calculate_sum_of_divisors(number):
        sum_of_divisors = 0
        for i in range(1, number):
            if number % i == 0:
                sum_of_divisors += i
        return sum_of_divisors

    amicable_sum = 0
    for num in range(1, limit+1):
        div_sum = calculate_sum_of_divisors(num)
        if num != div_sum and calculate_sum_of_divisors(div_sum) == num:
            amicable_sum += num

    return amicable_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()