def check_dict_case(dict):
    if not dict:
        return False
    keys = list(dict.keys())
    first_key = keys[0]
    if isinstance(first_key, int):
        return False
    if first_key.islower():
        for key in keys:
            if not key.islower():
                return False
    elif first_key.isupper():
        for key in keys:
            if not key.isupper():
                return False
    else:
        return False
    return True
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