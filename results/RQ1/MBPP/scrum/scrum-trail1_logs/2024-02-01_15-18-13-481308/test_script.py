def sum_div(number):
    '''Write a function to return the sum of all divisors of a number.'''
    # Validate input
    if not isinstance(number, int) or number <= 0:
        return "Invalid input"

    # Calculate the sum of divisors
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    return divisor_sum

assert sum_div(8)==7
import unittest

class Test(unittest.TestCase):
    def test_sum_div(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()