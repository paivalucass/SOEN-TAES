def check_dict_case(dict):
    if len(dict) == 0:
        return False
    keys = dict.keys()
    if all(isinstance(key, str) and key.islower() for key in keys) or all(isinstance(key, str) and key.isupper() for key in keys):
        return True
    return False
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(check_dict_case({"a":"apple", "b":"banana"}), True)

    def test2(self):
        self.assertEqual(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}), False)

    def test3(self):
        self.assertEqual(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}), False)

    def test4(self):
        self.assertEqual(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}), False)

    def test5(self):
        self.assertEqual(check_dict_case({"STATE":"NC", "ZIP":"12345"}), True)


if __name__ == '__main__':
    unittest.main()