def power_base_sum(base, power):
    '''
    Write a function that takes base and power as arguments and calculates the sum of all digits of the base to the specified power.
    Ensure that the input base or power is not negative or zero.
    Add test cases to cover various scenarios such as positive base and power, negative base and power, and zero base and power.
    '''
    if base <= 0 or power <= 0:
        return "Base and power must be positive numbers"

    result = str(base ** power)
    digit_sum = 0
    for digit in result:
        digit_sum += int(digit)
    return digit_sum
import unittest

class Test(unittest.TestCase):
    def test_power_base_sum(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()