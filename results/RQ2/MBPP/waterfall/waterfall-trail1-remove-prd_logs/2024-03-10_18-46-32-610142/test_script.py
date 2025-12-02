def check_str(string):
    import re
    pattern = r'^[aeiouAEIOU]'
    if re.match(pattern, string):
        return True
    else:
        return False
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_str('annie'), True)

if __name__ == '__main__':
    unittest.main()