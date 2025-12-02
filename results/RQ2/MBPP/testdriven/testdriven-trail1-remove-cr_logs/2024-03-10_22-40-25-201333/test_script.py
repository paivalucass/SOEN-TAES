def round_and_sum(list1):
    rounded_numbers = [round(num) for num in list1]
    total_sum = sum(rounded_numbers)
    result = total_sum * len(list1)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]), 243)

if __name__ == '__main__':
    unittest.main()