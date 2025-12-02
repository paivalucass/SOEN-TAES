import re

def remove_dirty_chars(string, chars_to_remove):
    pattern = re.compile('[' + chars_to_remove + ']')
    return pattern.sub('', string)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()