def number_ctr(input_string):
    '''Write a python function to count number of digits in a given string.'''
    count = 0
    for char in input_string:
        if char.isdigit():
            count += 1
    return count

assert number_ctr('program2bedone') == 1
import unittest

class Test(unittest.TestCase):
    def test_number_ctr(self):
        self.assertEqual(number_ctr('program2bedone'), 1)

if __name__ == '__main__':
    unittest.main()