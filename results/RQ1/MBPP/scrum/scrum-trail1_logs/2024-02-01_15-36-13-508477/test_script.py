def round_and_sum(list1):
    '''Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.'''
    rounded_numbers = [round(num) for num in list1]
    total_sum = sum(rounded_numbers)
    multiplied_sum = total_sum * len(list1)
    return multiplied_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]), 243)

if __name__ == '__main__':
    unittest.main()