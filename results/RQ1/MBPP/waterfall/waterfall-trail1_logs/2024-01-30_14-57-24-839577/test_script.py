def add_dict_to_tuple(test_tup, test_dict):
    if not isinstance(test_tup, tuple):
        raise ValueError("The first argument should be a tuple.")
    if not isinstance(test_dict, dict):
        raise ValueError("The second argument should be a dictionary.")

    updated_tuple = list(test_tup)
    updated_tuple.append(test_dict)
    return tuple(updated_tuple)
import unittest

class Test(unittest.TestCase):
    def test_add_dict_to_tuple(self):
        self.assertEqual(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3}), (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3}))

if __name__ == '__main__':
    unittest.main()