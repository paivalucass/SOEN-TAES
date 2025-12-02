def power_base_sum(base, power):
    # Calculate the sum of all digits of the base raised to the specified power
    if base <= 0 or power < 0:
        return "Error: Invalid input"
    result = sum(int(digit) for digit in str(base ** power))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()