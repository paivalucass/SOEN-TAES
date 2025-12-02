def find_substring(str_list, sub_str):
    '''Function to check if a string is present as a substring in a given list of string values.
    :param str_list: list of string values
    :param sub_str: substring to search for
    :return: True if the substring is present, otherwise False
    '''

    # Input validation
    if str_list is None or len(str_list) == 0 or sub_str is None or len(sub_str) == 0:
        return False  # If input list of string values or substring is null or empty, return False

    # Efficient string search algorithm for performance optimization
    for string in str_list:
        if sub_str in string:
            return True  # Return True if the substring is present in any of the string values

    return False  # Return False if the substring is not present in any of the string values

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_substring(["red", "black", "white", "green", "orange"], "ack"), True)

if __name__ == '__main__':
    unittest.main()