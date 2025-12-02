def check_dict_case(input_dict):
    if not isinstance(input_dict, dict) or len(input_dict) == 0:
        return False
    keys = list(input_dict.keys())
    if all(isinstance(key, str) for key in keys) and (all(key.islower() for key in keys) or all(key.isupper() for key in keys)):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_dict_case({"a":"apple", "b":"banana"}), True)
        self.assertEqual(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}), False)
        self.assertEqual(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}), False)
        self.assertEqual(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}), False)
        self.assertEqual(check_dict_case({"STATE":"NC", "ZIP":"12345"}), True)

if __name__ == '__main__':
    unittest.main()