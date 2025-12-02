def check_str(string):
    pattern = '^[aeiou]'
    result = re.match(pattern, string, re.IGNORECASE)
    return bool(result)
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_str('annie'))

if __name__ == '__main__':
    unittest.main()