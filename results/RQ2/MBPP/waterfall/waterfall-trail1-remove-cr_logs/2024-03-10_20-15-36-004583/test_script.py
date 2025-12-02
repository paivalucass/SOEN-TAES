def check_str(string):
    if not isinstance(string, str) or string.islower() == False:
        raise ValueError("Input is not a valid string or contains uppercase letters")
    
    pattern = r'^[aeiou]'
    return bool(re.match(pattern, string))
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_str('annie'), 1)

if __name__ == '__main__':
    unittest.main()