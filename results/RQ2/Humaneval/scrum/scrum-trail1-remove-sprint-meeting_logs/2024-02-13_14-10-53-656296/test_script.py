def check_dict_case(dict):
    if len(dict) == 0:
        return False
    keys = list(dict.keys())
    first_key_case = keys[0].islower()
    for key in keys[1:]:
        if key.islower() != first_key_case:
            return False
    return True
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