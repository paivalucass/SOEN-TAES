def check_dict_case(input_dict):
    if not isinstance(input_dict, dict) or len(input_dict) == 0:
        return False
    
    lower_case_keys = all(key.islower() for key in input_dict.keys() if isinstance(key, str))
    upper_case_keys = all(key.isupper() for key in input_dict.keys() if isinstance(key, str))
    
    return lower_case_keys or upper_case_keys
import unittest

class Test(unittest.TestCase):
    def test_check_dict_case(self):
        self.assertEqual(check_dict_case({"a":"apple", "b":"banana"}), True)
        self.assertEqual(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}), False)
        self.assertEqual(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}), False)
        self.assertEqual(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}), False)
        self.assertEqual(check_dict_case({"STATE":"NC", "ZIP":"12345" }), True)

if __name__ == '__main__':
    unittest.main()