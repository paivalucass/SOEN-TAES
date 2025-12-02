def extract_string(input_list, length):
    """
    Function to extract strings of specified length from a given list of strings.

    :param input_list: List of strings
    :param length: Length of strings to be extracted
    :return: List of strings with specified length
    :raises ValueError: If length input is not a positive integer
    :raises ValueError: If input list is empty or does not contain any strings of the specified length
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length input must be a positive integer")

    if not isinstance(input_list, list) or not all(isinstance(item, str) for item in input_list):
        raise ValueError("Input list must be a list of strings")

    result = [string for string in input_list if len(string) == length]

    if not result:
        raise ValueError("No strings of specified length found in the input list")

    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()