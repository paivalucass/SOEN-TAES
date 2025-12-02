def check_dict_case(dictionary):
    keys = dictionary.keys()
    if not keys:
        return False
    return all(str(key).islower() for key in keys) or all(str(key).isupper() for key in keys)
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