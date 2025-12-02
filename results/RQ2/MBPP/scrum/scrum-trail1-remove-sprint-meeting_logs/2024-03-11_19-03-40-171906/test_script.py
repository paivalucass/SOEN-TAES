def add_dict_to_tuple(test_tup: tuple, test_dict: dict) -> tuple:
    if not isinstance(test_tup, tuple) or not isinstance(test_dict, dict):
        raise ValueError("Input types should be tuple and dictionary")
    
    new_tuple = test_tup + (test_dict,)
    return new_tuple
import unittest

class Test(unittest.TestCase):
    def test_add_dict_to_tuple(self):
        self.assertEqual(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3}), (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3}))

if __name__ == '__main__':
    unittest.main()