def drop_empty(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input is not a dictionary")

    result_dict = {key: value for key, value in input_dict.items() if value not in [None, '', [], {}]}

    return result_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}), {'c1': 'Red', 'c2': 'Green'})

if __name__ == '__main__':
    unittest.main()