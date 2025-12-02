def frequency(input_list, number):
    if not input_list or not all(isinstance(x, int) for x in input_list):
        return "Invalid input list"
    
    if not isinstance(number, int) or number <= 0:
        return "Invalid input number"

    frequency_count = input_list.count(number)
    return frequency_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency([1, 2, 3], 4), 0)

if __name__ == '__main__':
    unittest.main()