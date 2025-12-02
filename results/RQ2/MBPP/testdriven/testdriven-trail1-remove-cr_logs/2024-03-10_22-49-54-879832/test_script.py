def power_base_sum(base, power):
    if not isinstance(base, int) or not isinstance(power, int):
        return "Error: Both base and power should be integers"
    
    if base < 0:
        return "Error: Base cannot be negative"
    
    if power < 0:
        return "Error: Power cannot be negative"
    
    result = base ** power
    return sum(int(digit) for digit in str(result))
import unittest

class Test(unittest.TestCase):
    def test_power_base_sum(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()