def is_dict_empty(input_dict):
    '''This function checks if a dictionary is empty
    Args:
        input_dict: A dictionary to be checked for emptiness
    Returns:
        True if the dictionary is empty, False otherwise
    '''
    if not isinstance(input_dict, dict):  # input validation for dictionary type
        raise TypeError("Input is not a dictionary type")

    if not input_dict:  # check if the dictionary is empty
        return True
    else:
        return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(my_dict({10}), False)

if __name__ == '__main__':
    unittest.main()