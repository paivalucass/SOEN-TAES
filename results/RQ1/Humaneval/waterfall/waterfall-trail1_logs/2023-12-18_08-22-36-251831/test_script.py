def check_dict_case(dictionary):
    if len(dictionary) == 0:
        return False
    lowercase_keys = all(key.islower() and isinstance(key, str) for key in dictionary.keys() if isinstance(key, str))
    uppercase_keys = all(key.isupper() and isinstance(key, str) for key in dictionary.keys() if isinstance(key, str))
    return lowercase_keys or uppercase_keys

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