def add_dict_to_tuple(test_tup, test_dict):
    if not test_tup:
        raise AssertionError
    temp_list = list(test_tup)
    temp_list.append(test_dict)
    output_tuple = tuple(temp_list)
    return output_tuple
import unittest

class Test(unittest.TestCase):
    def test_add_dict_to_tuple(self):
        self.assertEqual(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3}), (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3}))

if __name__ == '__main__':
    unittest.main()