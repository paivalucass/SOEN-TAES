import unittest
import re

class TestStringMethods(unittest.TestCase):
    def test_start_with_vowel(self):
        self.assertTrue(check_str("apple"))
        self.assertFalse(check_str("banana"))
        self.assertTrue(check_str("orange"))
        self.assertFalse(check_str("pear"))

if __name__ == '__main__':
    unittest.main()

def check_str(string):
    vowel_regex = '^[aeiouAEIOU].*'
    if re.match(vowel_regex, string):
        return True
    else:
        return False
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_str('annie'))
        self.assertFalse(check_str('hello'))

if __name__ == '__main__':
    unittest.main()