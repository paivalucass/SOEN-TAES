def drop_empty(dict1):
    if not isinstance(dict1, dict):
        raise ValueError('Input is not a dictionary')
    if not dict1:
        raise ValueError('Input dictionary is empty')
    
    updated_dict = {}
    for key, value in dict1.items():
        if value is not None:
            updated_dict[key] = value
    return updated_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}), {'c1': 'Red', 'c2': 'Green'})

if __name__ == '__main__':
    unittest.main()