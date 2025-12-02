def check_dict_case(dict):
  if len(dict) == 0:
    return False
  keys = list(dict.keys())
  first_key = keys[0]
  if isinstance(first_key, str) and first_key.islower():
    for key in keys:
      if not (isinstance(key, str) and key.islower()):
        return False
    return True
  elif isinstance(first_key, str) and first_key.isupper():
    for key in keys:
      if not (isinstance(key, str) and key.isupper()):
        return False
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