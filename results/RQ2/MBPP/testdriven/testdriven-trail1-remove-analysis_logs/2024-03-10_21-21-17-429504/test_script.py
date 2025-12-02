def drop_empty(dict1):
    if not isinstance(dict1, dict):
        raise ValueError("Input must be a dictionary")

    new_dict = {}
    for key, value in dict1.items():
        if value is not None and value != "":
            new_dict[key] = value
    return new_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}), {'c1': 'Red', 'c2': 'Green'})

if __name__ == '__main__':
    unittest.main()