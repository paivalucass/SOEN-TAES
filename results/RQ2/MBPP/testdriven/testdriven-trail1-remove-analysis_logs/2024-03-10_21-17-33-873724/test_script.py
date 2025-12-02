def check_char(input_string):
    '''
    Function to check whether the given string starts and ends with the same character or not.
    '''
    if len(input_string) < 1:  # Check if the string is empty
        return "Valid"
    elif input_string[0] == input_string[-1]:  # Check if the first and last character are the same
        return "Valid"
    else:
        return "Invalid"  # If the conditions are not met, return "Invalid"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_char('abba'), "Valid")

if __name__ == '__main__':
    unittest.main()