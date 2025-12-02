def drop_empty(dict1):
    '''
    Write a function to drop empty items from a given dictionary.
    assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
    '''
    # Filter out empty values from the dictionary
    new_dict = {key: value for key, value in dict1.items() if value is not None and value != ''}
    return new_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}), {'c1': 'Red', 'c2': 'Green'})

if __name__ == '__main__':
    unittest.main()