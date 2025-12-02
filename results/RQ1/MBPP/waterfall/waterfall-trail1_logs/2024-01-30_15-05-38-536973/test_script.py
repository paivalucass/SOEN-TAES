import re
def text_match_zero_one(text):
    pattern = r'ab+'
    if re.search(pattern, text):
        return True
    else:
        return False
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_zero_one('ac'), False)

if __name__ == '__main__':
    unittest.main()