def power_base_sum(base, power):
    if not isinstance(base, int) or not isinstance(power, int) or base < 0 or power < 0:
        return "Error: Both base and power should be positive integers."

    result = pow(base, power)
    sum_of_digits = sum(int(digit) for digit in str(result))
    return sum_of_digits
import unittest

class Test(unittest.TestCase):
    def test_power_base_sum(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()