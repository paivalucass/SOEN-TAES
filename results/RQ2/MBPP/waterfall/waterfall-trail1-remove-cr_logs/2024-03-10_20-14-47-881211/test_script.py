def power_base_sum(base, power):
    if base < 0:
        return "Invalid input for base"
    if power < 0:
        return "Invalid input for power"
    if base == 0:
        return 0
    if power == 0:
        return 1
    result = base ** power
    return sum(int(digit) for digit in str(result))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()