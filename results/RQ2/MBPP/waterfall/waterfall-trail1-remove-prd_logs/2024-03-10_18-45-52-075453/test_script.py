def power_base_sum(base, power):
    """
    This function calculates the sum of the digits of the result of raising the base to the power.
    :param base: The base number
    :param power: The power to raise the base to
    :return: The sum of the digits of the result
    """
    if not isinstance(base, (int, float)) or not isinstance(power, (int, float)):
        raise ValueError("Base and power must be valid numbers")

    if power < 0 or (power == 0 and base != 0):
        raise ValueError("Power must be a non-negative integer")

    result = base ** power
    digit_sum = sum(map(int, str(result)))
    return digit_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()