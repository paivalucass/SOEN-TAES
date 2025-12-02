def power_base_sum(base, power):
    result = str(base ** power)
    return sum(int(digit) for digit in result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()