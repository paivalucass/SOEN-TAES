def check_str(string):
    if not isinstance(string, str) or not string:
        return False

    pattern = r'^[aeiouAEIOU]'

    if re.match(pattern, string):
        return True
    else:
        return False
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_str('annie'))

if __name__ == '__main__':
    unittest.main()