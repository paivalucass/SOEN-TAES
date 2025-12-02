def check_str(string):
    import re
    pattern = '^[aeiouAEIOU].*[aeiouAEIOU]$'
    return bool(re.match(pattern, string))
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_str('annie'), True)

if __name__ == '__main__':
    unittest.main()