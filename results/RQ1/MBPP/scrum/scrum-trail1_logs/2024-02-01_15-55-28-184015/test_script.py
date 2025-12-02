def drop_empty(dict1):
    if not isinstance(dict1, dict):
        raise TypeError("Input must be a dictionary")
    
    def is_empty(value):
        return value is None or value == ''
    
    def remove_empty_items(d):
        return {k: v for k, v in d.items() if not is_empty(v)}
    
    return remove_empty_items(dict1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}), {'c1': 'Red', 'c2': 'Green'})

if __name__ == '__main__':
    unittest.main()