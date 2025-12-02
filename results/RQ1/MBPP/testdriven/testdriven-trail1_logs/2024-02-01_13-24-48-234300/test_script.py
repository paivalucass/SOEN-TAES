import re

def number_ctr(input_string):
    '''
    Function to count the number of digits in a given string.
    '''
    if not isinstance(input_string, str):
        raise ValueError("Input is not a valid string")

    pattern = r'\d'
    digit_count = len(re.findall(pattern, input_string))
    return digit_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_ctr('program2bedone'), 1)

if __name__ == '__main__':
    unittest.main()