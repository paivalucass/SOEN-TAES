def return_sum(input_dict):
    '''Write function to find the sum of all items in the given dictionary.'''
    try:
        if not isinstance(input_dict, dict):
            raise TypeError("Input is not a dictionary")
        
        total_sum = sum(input_dict.values())
        return total_sum
    except ValueError as ve:
        return f"Error: {ve}"
    except TypeError as te:
        return f"Error: {te}"

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()