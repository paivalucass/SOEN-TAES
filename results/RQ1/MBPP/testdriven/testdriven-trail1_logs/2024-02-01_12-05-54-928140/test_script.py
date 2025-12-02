def amicable_numbers_sum(limit):
    '''Function to sum all amicable numbers from 1 to a specified number'''
    
    # Function to find all divisors of a number
    def find_divisors(num):
        divisors = [1]
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                divisors.extend([i, num//i])
        return divisors
    
    # Function to find the sum of divisors of a number
    def sum_of_divisors(num):
        return sum(find_divisors(num))
    
    # Function to find amicable numbers within a limit and their sum
    def find_amicable_numbers(limit):
        amicable_sum = 0
        for i in range(2, limit+1):
            sum1 = sum_of_divisors(i)
            if sum1 != i and sum_of_divisors(sum1) == i:
                amicable_sum += i
        return amicable_sum
    
    # Error handling for unexpected input
    if not isinstance(limit, int) or limit < 1:
        return "Invalid input. Please enter a positive integer."
    
    # Call the function to find amicable numbers and return their sum
    return find_amicable_numbers(limit)

assert amicable_numbers_sum(999)==504
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()