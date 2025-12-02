def check_dict_case(input_dict):
    if not isinstance(input_dict, dict):
        raise Exception("Input is not a dictionary")
    if not bool(input_dict):
        return False

    all_keys_lower_case = all(key.islower() and isinstance(key, str) for key in input_dict.keys())
    all_keys_upper_case = all(key.isupper() and isinstance(key, str) for key in input_dict.keys())

    return all_keys_lower_case or all_keys_upper_case

import unittest

class Test(unittest.TestCase):
    def test_check_dict_case(self):
        self.assertEqual(check_dict_case({"a":"apple", "b":"banana"}), True)
        self.assertEqual(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}), False)
        self.assertEqual(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}), False)
        self.assertEqual(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}), False)
        self.assertEqual(check_dict_case({"STATE":"NC", "ZIP":"12345"}), True)

if __name__ == '__main__':
    unittest.main()