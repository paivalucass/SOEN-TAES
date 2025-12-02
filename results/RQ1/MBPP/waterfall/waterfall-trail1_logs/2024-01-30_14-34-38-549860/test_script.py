def drop_empty(dict1):
    if not isinstance(dict1, dict):
        raise ValueError("Input is not a dictionary")
    
    return {key: value for key, value in dict1.items() if value}
import unittest

class Test(unittest.TestCase):
    def test_drop_empty(self):
        self.assertEqual(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}), {'c1': 'Red', 'c2': 'Green'})

if __name__ == '__main__':
    unittest.main()