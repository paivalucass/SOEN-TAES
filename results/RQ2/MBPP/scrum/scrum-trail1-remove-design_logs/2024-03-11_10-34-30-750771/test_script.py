def round_and_sum(number_list):
    rounded_list = [round(num) for num in number_list]
    total_sum = sum(rounded_list)
    return total_sum * len(number_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]), 243)

if __name__ == '__main__':
    unittest.main()