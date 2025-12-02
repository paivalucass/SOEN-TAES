def add_dict_to_tuple(test_tup, test_dict):
    keys = test_dict.keys()
    values = test_dict.values()
    result = test_tup + (test_dict,)
    return result
import unittest

class Test(unittest.TestCase):
    def test_add_dict_to_tuple(self):
        self.assertEqual(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3}), (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3}))

if __name__ == '__main__':
    unittest.main()