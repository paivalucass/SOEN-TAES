def check_dict_case(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input is not a dictionary")

    keys = list(input_dict.keys())
    if len(keys) == 0:
        return False
    if any(not isinstance(key, str) for key in keys):
        return False
    return all(key.islower() for key in keys) or all(key.isupper() for key in keys)
import unittest

class Test(unittest.TestCase):
    def test_check_dict_case(self):
        self.assertTrue(check_dict_case({"a":"apple", "b":"banana"}))
        self.assertFalse(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
        self.assertFalse(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
        self.assertFalse(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
        self.assertTrue(check_dict_case({"STATE":"NC", "ZIP":"12345"}))

if __name__ == '__main__':
    unittest.main()