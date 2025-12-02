def power_base_sum(base, power):
    '''Write a function that takes base and power as arguments and calculates the sum of all digits of the base to the specified power.'''
    result = calculate_power(base, power)
    return sum_of_digits(result)

def calculate_power(base, power):
    return base ** power

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

assert power_base_sum(2,100)==115
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()