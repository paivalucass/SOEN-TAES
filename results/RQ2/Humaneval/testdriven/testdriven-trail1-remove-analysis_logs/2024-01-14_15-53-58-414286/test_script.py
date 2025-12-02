def check_dict_case(input_dict):
    if not isinstance(input_dict, dict) or not input_dict:
        return False

    keys = input_dict.keys()
    if any(not isinstance(key, str) for key in keys):
        return False

    lowercase_keys = all(key.islower() for key in keys)
    uppercase_keys = all(key.isupper() for key in keys)

    return lowercase_keys or uppercase_keys
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(check_dict_case({"a":"apple", "b":"banana"}))
    def test2(self):
        self.assertFalse(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
    def test3(self):
        self.assertFalse(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
    def test4(self):
        self.assertFalse(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
    def test5(self):
        self.assertTrue(check_dict_case({"STATE":"NC", "ZIP":"12345" }))

if __name__ == '__main__':
    unittest.main()