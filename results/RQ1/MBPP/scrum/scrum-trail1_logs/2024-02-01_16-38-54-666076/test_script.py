def check_str(string):
    import re
    pattern = r'^[aeiouAEIOU]'
    return bool(re.match(pattern, string))
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_str('annie'))

if __name__ == '__main__':
    unittest.main()