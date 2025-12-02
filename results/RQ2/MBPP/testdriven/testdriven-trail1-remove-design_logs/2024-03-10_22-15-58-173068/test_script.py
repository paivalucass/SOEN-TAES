def add_dict_to_tuple(test_tup, test_dict):
    if not isinstance(test_dict, dict):
        return "Error: Invalid input data"
    
    return test_tup + (test_dict,) if test_tup else (test_dict,)
import unittest

class Test(unittest.TestCase):
    def test_add_dict_to_tuple(self):
        self.assertEqual(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3}), (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3}))

if __name__ == '__main__':
    unittest.main()