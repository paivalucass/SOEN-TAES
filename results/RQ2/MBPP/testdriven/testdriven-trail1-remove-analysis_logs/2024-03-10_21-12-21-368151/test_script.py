def next_power_of_2(number_to_check):
    if not isinstance(number_to_check, int):
        return "Error: Input is not an integer"
    elif number_to_check <= 0:
        return 1
    else:
        return 2**(number_to_check-1).bit_length()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()