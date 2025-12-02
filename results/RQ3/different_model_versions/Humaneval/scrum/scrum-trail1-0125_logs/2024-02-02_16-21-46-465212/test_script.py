def check_dict_case(dict):
    if not dict:
        return False
    
    upper_count = 0
    lower_count = 0
    
    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if key.isupper():
            upper_count += 1
        elif key.islower():
            lower_count += 1
        else:
            return False
    
    if upper_count == 0 or lower_count == 0:
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