def empty_dit(dictionary_list):
    '''This function checks whether all dictionaries in a list are empty or not.'''
    # Check if input is a list
    if not isinstance(dictionary_list, list):
        raise ValueError("Input data is not a list")

    # Check if input list contains non-dictionary elements
    for dictionary in dictionary_list:
        if not isinstance(dictionary, dict):
            raise ValueError("Input data contains non-dictionary elements")

    return all(not bool(dictionary) for dictionary in dictionary_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_dit([{}, {}, {}]), True)

if __name__ == '__main__':
    unittest.main()